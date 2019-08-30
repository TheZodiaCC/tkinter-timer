import tkinter as tk
from tkinter import *
import threading
import time


class Timer:

    def __init__(self, root):

        self.dead = False
        self.sec = 0
        self.mins = 0
        self.hours = 0

        root.title("Tkinter Timer")
        root.resizable(width=False, height=False)

        self.i = IntVar()
        self.b = IntVar()
        self.c = IntVar()

        self.menu()
        self.grid()

    def menu(self):
        menubar = tk.Menu(root)
        root.config(menu=menubar)

        dropdown = tk.Menu(menubar, tearoff=0)
        dropdown.add_command(label="Timer", command=self.about)
        menubar.add_cascade(label="About", menu=dropdown)

    def grid(self):
        self.start = tk.Button(root, text="Start", command=self.start)
        self.start.grid(row=1, column=0, sticky="NWNESWSE")
        self.stop = tk.Button(root, text="Stop", command=self.stop)
        self.stop.grid(row=1, column=1, sticky="NWNESWSE")
        self.reset = tk.Button(root, text="Reset", command=self.reset)
        self.reset.grid(row=1, column=2, sticky="NWNESWSE")

        eng_label = Label(root, textvariable=self.c)
        eng_label.grid(row=0, column=0, sticky="NWNESWSE")
        eng_label = Label(root, textvariable=self.b)
        eng_label.grid(row=0, column=1, sticky="NWNESWSE")
        eng_label = Label(root, textvariable=self.i)
        eng_label.grid(row=0, column=2, sticky="NWNESWSE")

    def count(self):
        self.dead = False

        while(self.dead == False):

            self.sec += 1
            self.i.set(self.sec)
            time.sleep(1)

            if self.sec >= 59:
                self.sec = 0
                self.mins += 1
                self.b.set(self.mins)
            else:
                pass

            if self.mins == 60:
                self.mins = 0
                self.hours += 1
                self.b.set(self.mins)
                self.c.set(self.hours)

    def start(self):
        t1 = threading.Thread(target=self.count)
        t1.start()

    def stop(self):
        self.dead = True

    def reset(self):
        self.dead = True
        self.sec = 0
        self.mins = 0
        self.hours = 0
        self.i.set(self.sec)
        self.b.set(self.mins)
        self.c.set(self.hours)

    def about(self):
        about = tk.Tk()

        about.geometry("250x50")
        about.title("About Timer")
        about.resizable(width=False, height=False)

        tk.Label(about, text="Tkinter Timer ~ 30.08.2019", font="20").pack(fill=tk.BOTH)
        tk.Label(about, text="Created by Zodiac", font="20").pack(fill=tk.BOTH)

        about.mainloop()


if __name__ == "__main__":

    root = tk.Tk()
    timer = Timer(root)
    root.mainloop()

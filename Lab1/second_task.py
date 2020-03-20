from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog as fd
import re
import random
import math
from math import cos
from math import sin


def size_and_title(self):
    self.root.title("Second Task")
    self.root.geometry('630x400+400+200')


def val(lm):
    values = re.findall(r"-?\d*\.\d+|-?\d+", lm)
    return values


def check(elem):
    if not elem.get().replace(".", "").replace(',', '').lstrip("+-").strip().isdigit():
        mb.showerror(title="Digit Error", message="Values should be digits in integer or float form")
        return False
    return True


def run(wd, sl):
    if check(wd):
        x = math.radians(float(val(wd.get())[0]))
        a = round(sin(x), ndigits=4)
        b = round(cos(x), ndigits=4)
        if a > 0:
            sl.config(text='y= ' + str(b / a + a ** (1 / 3)))
        elif a == 0:
            sl.config(text='y= ' + str(b ** 2 / 0.15))
        else:
            sl.config(text='y= ' + str(b / a + b ** (1 / 3)))
    return None


def file(self):
    def change_state(wd, state):
        wd.config(state=state)

    lb1 = Label(self.ffr1, text="x = ", font="Times 14")
    lb2 = Label(self.ffr1, text=" ", font="Times 14")

    lb1.grid(column=0, row=0)
    lb2.grid(column=0, row=1)

    e1 = Entry(self.ffr1, width=20, bg="white", state='disabled')

    e1.bind('<Button-1>', lambda event, wd=e1, state="normal": change_state(wd, state))
    e1.bind('<Return>', lambda event, wd=e1, state="readonly": change_state(wd, state))

    e1.grid(row=0, column=1, columnspan=2)

    self.ffr1.grid(row=0, column=0, padx=10, pady=10)

    lb2 = Label(self.ffr2, text="if sin(x) <>= 0: ", font="Times 14")

    lb2.grid(column=0, row=0, sticky=W)
    self.llbb1.grid(column=0, row=1, sticky=W)

    self.ffr2.grid(row=0, column=2, padx=10, pady=10)

    but1 = Button(self.ffile_frame, text="Run", font="Times 14", command=lambda wd=e1, sl=self.llbb1: run(wd, sl))

    but1.grid(row=1, column=1)

    self.ffile_frame.pack(anchor=W)


def generated(self):
    def generation():
        e1.delete(0, END)
        e1.insert(0, str(random.randrange(-360, 360)))
        return None

    lb1 = Label(self.ggfr1, text="x = ", font="Times 14")
    lb2 = Label(self.ggfr1, text=" ", font="Times 14")

    lb1.grid(column=0, row=0)
    lb2.grid(column=0, row=1)

    e1 = Entry(self.ggfr1, width=20, bg="white")

    e1.grid(row=0, column=1, columnspan=2)

    self.ggfr1.grid(row=0, column=0, padx=10, pady=10)

    lb2 = Label(self.ggfr2, text="if sin(x) <>= 0: ", font="Times 14")

    self.llbb2.grid(column=0, row=1, sticky=W)
    lb2.grid(column=0, row=0, sticky=W)

    self.ggfr2.grid(row=0, column=1, padx=10, pady=10)

    but1 = Button(self.ggenerated_frame, text="Run", font="Times 14", command=lambda wd=e1, sl=self.llbb2: run(wd, sl))
    but2 = Button(self.ggenerated_frame, text="Generate", font="Times 14", command=generation)

    but1.grid(row=1, column=1)
    but2.grid(row=1, column=0)

    self.ggenerated_frame.pack(anchor=W)


def from_file(self):
    def open_file():
        fl = fd.askopenfile(mode='r', filetypes=[('Text Files', '*.txt')])
        if fl is not None:
            content = fl.read()
            items = re.findall(r'[a-zA-Z]', content)
            values = re.findall(r"-?\d*\.\d+|-?\d+", content)
            x = 0
            for i in range(len(items) if len(items) <= len(values) else len(values)):
                if items[i].lower() == 'x':
                    x = math.radians(float(values[i]))

            a = round(sin(x), ndigits=4)
            b = round(cos(x), ndigits=4)

            if a > 0:
                self.llbb3.config(text='y= ' + str(b / a + a ** (1 / 3)))
            elif a == 0:
                self.llbb3.config(text='y= ' + str(b ** 2 / 0.15))
            else:
                self.llbb3.config(text='y= ' + str(b / a + b ** (1 / 3)))

    lb1 = Label(self.ffrom_fl, text="Please make *.txt file like x = something, y = ... Else x = 0", font="Times 14")

    lb1.grid(row=0, column=0, columnspan=20, padx=10, pady=10)

    lb2 = Label(self.fflfr1, text="if sin(x) <>= 0: ", font="Times 14")

    self.llbb3.grid(column=0, row=1, sticky=W)
    lb2.grid(column=0, row=0, sticky=W)

    self.fflfr1.grid(row=1, column=0, padx=10, pady=10, sticky=W)

    but1 = Button(self.ffrom_fl, text="Search", font="Times 14", command=lambda: open_file())

    but1.grid(row=5, column=0, sticky=(N, W, S, E), padx=10)

    self.ffrom_fl.pack(anchor=W)

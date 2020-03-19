import os
from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog as fd
import re
import random
from functools import reduce

val = []
m = 45


def check(lst):
    global val
    val = re.findall(r"[-+]?\d*\.\d+|\d+", lst.get())
    for i in val:
        if not i.replace(".", "").isdigit():
            mb.showerror(title="Digit Error", message="Values should be digits in integer or float form")
            return False
    global m
    if len(val) < m:
        ask = mb.askquestion(title="warning",
                             message="number ov values less then m = 35 change to current {} ?".format(len(val)))
        if ask == 'yes':
            m = len(val)
        else:
            return None
    return True


def run(wd, self):
    if check(wd):
        n = [float(i) for i in val]
        self.config(text='y1= ' + str(reduce(lambda x, y: x * y, n) / sum(n)))
    return None



def size_and_title(self):
    self.root.title("Second Task")
    self.root.geometry('600x300+600+400')


def file(self):
    def change_state(wd, state):
        wd.config(state=state)



    lb1 = Label(self.fr1, text="x = ", font="Times 14").grid(column=0, row=0)
    lb2 = Label(self.fr1, text=" ", font="Times 14").grid(column=0, row=1)

    e1 = Entry(self.fr1, width=20, bg="white", state='disabled')
    e1.bind('<Button-1>', lambda event, wd=e1, state="normal": change_state(wd, state))
    e1.bind('<Return>', lambda event, wd=e1, state="readonly": change_state(wd, state))
    e1.grid(row=0, column=1, columnspan=2)

    self.fr1.grid(row=0, column=0, padx=10, pady=10)

    self.lbb1.grid(column=0, row=1, sticky=W)
    lb2 = Label(self.fr2, text="y1 = s^(a/b + c) + d^(c/b + a)", font="Times 14").grid(column=0, row=0, sticky=W)
    self.fr2.grid(row=0, column=2, padx=10, pady=10)
    but1 = Button(self.file_frame, text="Run", font="Times 14", command=lambda self=self.lbb1, wd=e1: run(wd, self))
    but1.grid(row=1, column=1)
    self.file_frame.pack(anchor=W)


def generated(self):
    # def check(lst):
    #     for i in lst:
    #         if not i.get().strip().replace(".", "").isdigit():
    #             mb.showerror(title="Digit Error", message="Values should be digits in integer or float form")
    #             return False
    #     return True
    #
    # def run():
    #     if check([e1]):
    #         x = float(e1.get())
    #         self.lbb2.config(text='y1= ' + str(x))
    #     return None

    def generation():
        e1.delete(0, END)
        e1.insert(0, [str(random.random()) + ',' for i in range(m)])
        return None

    lb1 = Label(self.gfr1, text="x = ", font="Times 14").grid(column=0, row=0)
    lb2 = Label(self.gfr1, text=" ", font="Times 14").grid(column=0, row=1)

    e1 = Entry(self.gfr1, width=20, bg="white")
    e1.grid(row=0, column=1, columnspan=2)

    self.gfr1.grid(row=0, column=0, padx=10, pady=10)

    self.lbb2.grid(column=0, row=1, sticky=W)
    lb2 = Label(self.gfr2, text="y1 = s^(a/b + c) + d^(c/b + a)", font="Times 14").grid(column=0, row=0, sticky=W)

    self.gfr2.grid(row=0, column=1, padx=10, pady=10)

    but1 = Button(self.generated_frame, text="Run", font="Times 14", command=lambda self=self.lbb2, wd=e1: run(wd, self))
    but1.grid(row=1, column=1)

    but2 = Button(self.generated_frame, text="I love U", font="Times 14", command=generation)
    but2.grid(row=1, column=0)

    self.generated_frame.pack(anchor=W)
    self.generated_frame.pack(anchor=W)


def from_file(self):
    def open_file():
        global m
        file = fd.askopenfile(mode='r', filetypes=[('Python Files', '*.txt')])
        if file is not None:
            content = re.findall(r"[-+]?\d*\.\d+|\d+",file.read())
            lk = len(content)
            for i in content:
                if not i.replace(".", "").isdigit():
                    mb.showerror(title="Digit Error", message="Values should be digits in integer or float form")
            if len(content) < m:
                ask = mb.askquestion(title="warning",
                                     message="number ov values less then m = 35 generate others?")
                if ask == 'yes':
                    for i in range(m - lk):
                        content.append(random.random())
                    fl = open(file.name, 'w')
                    for i in range(lk, m):
                        fl.write(str(content[i])+',')
                    fl.close()

                else:
                    return None
            print(content)
            content = [float(i) for i in content]
            self.lbb3.config(text='y1= ' + str(reduce(lambda x, y: x * y, content) / sum(content)))


    lb1 = Label(self.from_fl, text="something", font="Times 14")
    lb1.grid(row=0, column=0, padx=10, pady=10)
    self.lbb3.grid(column=0, row=1, sticky=W)
    lb2 = Label(self.flfr1, text="y1 = s^(a/b + c) + d^(c/b + a)", font="Times 14").grid(column=0, row=0, sticky=W)
    self.flfr1.grid(row=1, column=0, padx=10, pady=10)

    but1 = Button(self.from_fl, text="Run", font="Times 14", command=lambda: open_file())
    but1.grid(row=2, column=1)
    self.from_fl.pack(anchor=W)

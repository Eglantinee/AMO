from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog as fd
import re
import random


def ret(val):
    res = re.findall(r"-?\d*\.\d+|-?\d+", val.get())
    return res[0]


def check_d(elem):
    if not str(elem).replace(".", "").replace(',', '').lstrip("+-").strip().isdigit():
        return False
    return True


def check(lst):
    for i in lst:
        if not i.get().replace(".", "").replace(',', '').lstrip("+-").replace(" ", '').isdigit():
            mb.showerror(title="Digit Error", message="Values should be digits in integer or float form")
            return False
    return True


def run(lst, self):
    if check(lst):
        if float(ret(lst[1])) != 0:
            a = float(ret(lst[0]))
            b = float(ret(lst[1]))
            c = float(ret(lst[2]))
            d = float(ret(lst[3]))
            s = float(ret(lst[4]))
            res = 0
            try:
                res = s ** (a / b + c) + d ** (c / b + a)
            except OverflowError:
                mb.showerror(title="OverflowError", message="Result is out of integer range")
            self.config(text='y1= ' + str(res))
        else:
            mb.showerror(title="Digit Error", message="b should not be equal 0")
    return None


def size_and_title(self):
    self.root.title("First Task")
    self.root.geometry('630x400+400+200')


def file(self):

    def change_state(wd, state):
        wd.config(state=state)

    lb1 = Label(self.fr1, text="a = ", font="Times 14")
    lb2 = Label(self.fr1, text="b = ", font="Times 14")
    lb3 = Label(self.fr1, text="c = ", font="Times 14")
    lb4 = Label(self.fr1, text="d = ", font="Times 14")
    lb5 = Label(self.fr1, text="s = ", font="Times 14")

    lb1.grid(column=0, row=0)
    lb2.grid(column=0, row=1)
    lb3.grid(column=0, row=2)
    lb4.grid(column=0, row=3)
    lb5.grid(column=0, row=4)

    e1 = Entry(self.fr1, width=20, bg="white", state='disabled')
    e2 = Entry(self.fr1, width=20, bg="white", state='disabled')
    e3 = Entry(self.fr1, width=20, bg="white", state='disabled')
    e4 = Entry(self.fr1, width=20, bg="white", state='disabled')
    e5 = Entry(self.fr1, width=20, bg="white", state='disabled')

    e1.bind('<Button-1>', lambda event, wd=e1, state="normal": change_state(wd, state))
    e1.bind('<Return>', lambda event, wd=e1, state="readonly": change_state(wd, state))
    e2.bind('<Button-1>', lambda event, wd=e2, state="normal": change_state(wd, state))
    e2.bind('<Return>', lambda event, wd=e2, state="readonly": change_state(wd, state))
    e3.bind('<Button-1>', lambda event, wd=e3, state="normal": change_state(wd, state))
    e3.bind('<Return>', lambda event, wd=e3, state="readonly": change_state(wd, state))
    e4.bind('<Button-1>', lambda event, wd=e4, state="normal": change_state(wd, state))
    e4.bind('<Return>', lambda event, wd=e4, state="readonly": change_state(wd, state))
    e5.bind('<Button-1>', lambda event, wd=e5, state="normal": change_state(wd, state))
    e5.bind('<Return>', lambda event, wd=e5, state="readonly": change_state(wd, state))

    e1.grid(row=0, column=1, columnspan=2)
    e2.grid(row=1, column=1, columnspan=2)
    e3.grid(row=2, column=1, columnspan=2)
    e4.grid(row=3, column=1, columnspan=2)
    e5.grid(row=4, column=1, columnspan=2)

    self.fr1.grid(row=0, column=0, padx=10, pady=10)

    lb2 = Label(self.fr2, text="y1 = s^(a/b + c) + d^(c/b + a)", font="Times 14")
    lb3 = Label(self.fr2, text=" ", font="Times 14")
    lb4 = Label(self.fr2, text=" ", font="Times 14")
    lb5 = Label(self.fr2, text=" ", font="Times 14")

    self.lbb1.grid(column=0, row=1, sticky=W)
    lb2.grid(column=0, row=0, sticky=W)
    lb3.grid(column=0, row=2)
    lb4.grid(column=0, row=3)
    lb5.grid(column=0, row=4)

    self.fr2.grid(row=0, column=2, padx=10, pady=10)

    but1 = Button(self.file_frame, text="Run", font="Times 14",
                  command=lambda lst=(e1, e2, e3, e4, e5), sl=self.lbb1: run(lst, sl))

    but1.grid(row=1, column=1)

    self.file_frame.pack(anchor=W)


def generated(self):

    def generation():
        for i in (e1, e2, e3, e4, e5):
            i.delete(0, END)
            i.insert(0, str(random.randrange(0, 10)))
        return None

    lb1 = Label(self.gfr1, text="a = ", font="Times 14")
    lb2 = Label(self.gfr1, text="b = ", font="Times 14")
    lb3 = Label(self.gfr1, text="c = ", font="Times 14")
    lb4 = Label(self.gfr1, text="d = ", font="Times 14")
    lb5 = Label(self.gfr1, text="s = ", font="Times 14")

    lb1.grid(column=0, row=0)
    lb2.grid(column=0, row=1)
    lb3.grid(column=0, row=2)
    lb4.grid(column=0, row=3)
    lb5.grid(column=0, row=4)

    e1 = Entry(self.gfr1, width=20, bg="white")
    e2 = Entry(self.gfr1, width=20, bg="white")
    e3 = Entry(self.gfr1, width=20, bg="white")
    e4 = Entry(self.gfr1, width=20, bg="white")
    e5 = Entry(self.gfr1, width=20, bg="white")

    e1.grid(row=0, column=1, columnspan=2)
    e2.grid(row=1, column=1, columnspan=2)
    e3.grid(row=2, column=1, columnspan=2)
    e4.grid(row=3, column=1, columnspan=2)
    e5.grid(row=4, column=1, columnspan=2)

    self.gfr1.grid(row=0, column=0, padx=10, pady=10)

    lb2 = Label(self.gfr2, text="y1 = s^(a/b + c) + d^(c/b + a)", font="Times 14")
    lb3 = Label(self.gfr2, text=" ", font="Times 14")
    lb4 = Label(self.gfr2, text=" ", font="Times 14")
    lb5 = Label(self.gfr2, text=" ", font="Times 14")

    self.lbb2.grid(column=0, row=1, sticky=W)
    lb2.grid(column=0, row=0, sticky=W)
    lb3.grid(column=0, row=2)
    lb4.grid(column=0, row=3)
    lb5.grid(column=0, row=4)

    self.gfr2.grid(row=0, column=1, padx=10, pady=10)

    but1 = Button(self.generated_frame, text="Run", font="Times 14",
                  command=lambda lst=(e1, e2, e3, e4, e5), sl=self.lbb2: run(lst=lst, self=sl))
    but2 = Button(self.generated_frame, text="Generate", font="Times 14", command=generation)

    but1.grid(row=1, column=1)
    but2.grid(row=1, column=0)

    self.generated_frame.pack(anchor=W)


def from_file(self):
    def open_file():
        fl = fd.askopenfile(mode='r', filetypes=[('Text Files', '*.txt')])
        if fl is not None:
            content = fl.read()
            items = re.findall(r'[a-zA-Z]', content)
            values = re.findall(r"-?\d*\.\d+|-?\d+", content)
            a, b, c, d, s = 0, 1, 0, 0, 0
            for i in range(len(items)):
                if items[i].lower() == 'a':
                    a = float(values[i])
                elif items[i].lower() == 'b':
                    if float(values[i]) == 0:
                        mb.showerror(title="Error", message="b should not be equal 0")
                    else:
                        b = float(values[i])
                elif items[i].lower() == 'c':
                    c = float(values[i])
                elif items[i].lower() == 'd':
                    d = float(values[i])
                elif items[i].lower() == 's':
                    s = float(values[i])

            res = 0

            try:
                res = s ** (a / b + c) + d ** (c / b + a)
            except OverflowError:
                mb.showerror(title="OverflowError", message="Result is out of integer range")

            self.lbb3.config(text='y1= ' + str(round(res, ndigits=4)))

    lb1 = Label(self.from_fl, text="Create *.txt file like a=1, b=2 ... Else a,s,c,d=0, b=1", font="Times 14")
    lb2 = Label(self.flfr1, text="y1 = s^(a/b + c) + d^(c/b + a)", font="Times 14")
    lb3 = Label(self.flfr1, text=" ", font="Times 14")
    lb4 = Label(self.flfr1, text=" ", font="Times 14")
    lb5 = Label(self.flfr1, text=" ", font="Times 14")

    lb1.grid(row=0, column=0, columnspan=20, padx=10, pady=10)
    self.lbb3.grid(column=0, row=1, sticky=W)
    lb2.grid(column=0, row=0, sticky=W)
    lb3.grid(column=0, row=2)
    lb4.grid(column=0, row=3)
    lb5.grid(column=0, row=4)

    self.flfr1.grid(row=1, column=0, padx=10, pady=10, sticky=W)

    but1 = Button(self.from_fl, text="Search", font="Times 14", command=open_file)

    but1.grid(row=2, column=1)

    self.from_fl.pack(anchor=W)

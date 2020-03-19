from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog as fd
import re
import random


def size_and_title(self):
    self.root.title("first")
    self.root.geometry('600x400+600+400')


def file(self):
    def change_state(wd, state):
        wd.config(state=state)

    def check(lst):
        for i in lst:
            if not i.get().strip().replace(".", "").isdigit():
                mb.showerror(title="Digit Error", message="Values should be digits in integer or float form")
                return False
        return True

    def run():
        if check([e1, e2, e3, e4, e5]):
            if float(e2.get()) != 0:
                a = float(e1.get())
                b = float(e2.get())
                c = float(e3.get())
                d = float(e4.get())
                s = float(e5.get())
                self.lbb1.config(text='y1= ' + str(s ** (a / b + c) + d ** (c / b + a)))
            else:
                mb.showerror(title="Digit Error", message="b should not be equal 0")
        return None

    lb1 = Label(self.fr1, text="a = ", font="Times 14").grid(column=0, row=0)
    lb2 = Label(self.fr1, text="b = ", font="Times 14").grid(column=0, row=1)
    lb3 = Label(self.fr1, text="c = ", font="Times 14").grid(column=0, row=2)
    lb4 = Label(self.fr1, text="d = ", font="Times 14").grid(column=0, row=3)
    lb5 = Label(self.fr1, text="s = ", font="Times 14").grid(column=0, row=4)

    e1 = Entry(self.fr1, width=20, bg="white", state='disabled')
    e1.bind('<Button-1>', lambda event, wd=e1, state="normal": change_state(wd, state))
    e1.bind('<Return>', lambda event, wd=e1, state="readonly": change_state(wd, state))
    e1.grid(row=0, column=1, columnspan=2)

    e2 = Entry(self.fr1, width=20, bg="white", state='disabled')
    e2.bind('<Button-1>', lambda event, wd=e2, state="normal": change_state(wd, state))
    e2.bind('<Return>', lambda event, wd=e2, state="readonly": change_state(wd, state))
    e2.grid(row=1, column=1, columnspan=2)

    e3 = Entry(self.fr1, width=20, bg="white", state='disabled')
    e3.bind('<Button-1>', lambda event, wd=e3, state="normal": change_state(wd, state))
    e3.bind('<Return>', lambda event, wd=e3, state="readonly": change_state(wd, state))
    e3.grid(row=2, column=1, columnspan=2)

    e4 = Entry(self.fr1, width=20, bg="white", state='disabled')
    e4.bind('<Button-1>', lambda event, wd=e4, state="normal": change_state(wd, state))
    e4.bind('<Return>', lambda event, wd=e4, state="readonly": change_state(wd, state))
    e4.grid(row=3, column=1, columnspan=2)

    e5 = Entry(self.fr1, width=20, bg="white", state='disabled')
    e5.bind('<Button-1>', lambda event, wd=e5, state="normal": change_state(wd, state))
    e5.bind('<Return>', lambda event, wd=e5, state="readonly": change_state(wd, state))
    e5.grid(row=4, column=1, columnspan=2)

    self.fr1.grid(row=0, column=0, padx=10, pady=10)

    self.lbb1.grid(column=0, row=1, sticky=W)
    lb2 = Label(self.fr2, text="y1 = s^(a/b + c) + d^(c/b + a)", font="Times 14").grid(column=0, row=0, sticky=W)
    lb3 = Label(self.fr2, text=" ", font="Times 14").grid(column=0, row=2)
    lb4 = Label(self.fr2, text=" ", font="Times 14").grid(column=0, row=3)
    lb5 = Label(self.fr2, text=" ", font="Times 14").grid(column=0, row=4)

    self.fr2.grid(row=0, column=2, padx=10, pady=10)
    but1 = Button(self.file_frame, text="Run", font="Times 14", command=run)
    but1.grid(row=1, column=1)
    self.file_frame.pack(anchor=W)


def generated(self):
    def check(lst):
        for i in lst:
            if not i.get().strip().replace(".", "").isdigit():
                mb.showerror(title="Digit Error", message="Values should be digits in integer or float form")
                return False
        return True

    def run():
        if check([e1, e2, e3, e4, e5]):
            if float(e2.get()) != 0:
                a = float(e1.get())
                b = float(e2.get())
                c = float(e3.get())
                d = float(e4.get())
                s = float(e5.get())
                self.lbb2.config(text='y1= ' + str(s ** (a / b + c) + d ** (c / b + a)))
            else:
                mb.showerror(title="Digit Error", message="b should not be equal 0")
        return None

    def generation():
        for i in (e1, e2, e3, e4, e5):
            i.delete(0, END)
            i.insert(0, str(random.randrange(0, 10)))
        return None

    lb1 = Label(self.gfr1, text="a = ", font="Times 14").grid(column=0, row=0)
    lb2 = Label(self.gfr1, text="b = ", font="Times 14").grid(column=0, row=1)
    lb3 = Label(self.gfr1, text="c = ", font="Times 14").grid(column=0, row=2)
    lb4 = Label(self.gfr1, text="d = ", font="Times 14").grid(column=0, row=3)
    lb5 = Label(self.gfr1, text="s = ", font="Times 14").grid(column=0, row=4)

    e1 = Entry(self.gfr1, width=20, bg="white")
    e1.grid(row=0, column=1, columnspan=2)

    e2 = Entry(self.gfr1, width=20, bg="white")
    e2.grid(row=1, column=1, columnspan=2)

    e3 = Entry(self.gfr1, width=20, bg="white")
    e3.grid(row=2, column=1, columnspan=2)

    e4 = Entry(self.gfr1, width=20, bg="white")
    e4.grid(row=3, column=1, columnspan=2)

    e5 = Entry(self.gfr1, width=20, bg="white")
    e5.grid(row=4, column=1, columnspan=2)

    self.gfr1.grid(row=0, column=0, padx=10, pady=10)

    self.lbb2.grid(column=0, row=1, sticky=W)
    lb2 = Label(self.gfr2, text="y1 = s^(a/b + c) + d^(c/b + a)", font="Times 14").grid(column=0, row=0, sticky=W)
    lb3 = Label(self.gfr2, text=" ", font="Times 14").grid(column=0, row=2)
    lb4 = Label(self.gfr2, text=" ", font="Times 14").grid(column=0, row=3)
    lb5 = Label(self.gfr2, text=" ", font="Times 14").grid(column=0, row=4)
    self.gfr2.grid(row=0, column=1, padx=10, pady=10)

    but1 = Button(self.generated_frame, text="Run", font="Times 14", command=run)
    but1.grid(row=1, column=1)

    but2 = Button(self.generated_frame, text="Generate", font="Times 14", command=generation)
    but2.grid(row=1, column=0)

    self.generated_frame.pack(anchor=W)
    self.generated_frame.pack(anchor=W)


def from_file(self):
    def open_file():
        file = fd.askopenfile(mode='r', filetypes=[('Python Files', '*.txt')])
        if file is not None:
            content = file.read()
            items = re.findall(r'[a-zA-Z]', content)
            values = re.findall(r"[-+]?\d*\.\d+|\d+", content)
            print(items, values)
            a, b, c, d, s = 0, 1, 0, 0, 0
            for i in range(len(items)):
                if items[i].lower() == 'a' and values[i].replace(".", "").isdigit() is True:
                    print("enter")
                    a = float(values[i])
                elif items[i].lower() == 'b' and values[i].replace(".", "").isdigit() is True:
                    if float(values[i]) == 0:
                        mb.showerror(title="Error", message="b should not be equal 0")
                    else:
                        b = float(values[i])
                elif items[i].lower() == 'c' and values[i].replace(".", "").isdigit() is True:
                    c = float(values[i])
                elif items[i].lower() == 'd' and values[i].replace(".", "").isdigit() is True:
                    d = float(values[i])
                elif items[i].lower() == 's' and values[i].replace(".", "").isdigit() is True:
                    s = float(values[i])
            print(a, b, c, d, s)

    lb1 = Label(self.from_fl, text="something", font="Times 14")
    lb1.grid(row=0, column=0, padx=10, pady=10)
    self.lbb3.grid(column=0, row=1, sticky=W)
    lb2 = Label(self.flfr1, text="y1 = s^(a/b + c) + d^(c/b + a)", font="Times 14").grid(column=0, row=0, sticky=W)
    lb3 = Label(self.flfr1, text=" ", font="Times 14").grid(column=0, row=2)
    lb4 = Label(self.flfr1, text=" ", font="Times 14").grid(column=0, row=3)
    lb5 = Label(self.flfr1, text=" ", font="Times 14").grid(column=0, row=4)
    self.flfr1.grid(row=1, column=0, padx=10, pady=10)

    but1 = Button(self.from_fl, text="Run", font="Times 14", command=lambda: open_file())
    but1.grid(row=2, column=1)
    self.from_fl.pack(anchor=W)

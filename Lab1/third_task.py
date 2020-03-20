from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog as fd
import re
import random
from functools import reduce

val = []
m = 45


def size_and_title(self):
    self.root.title("Third Task")
    self.root.geometry('630x400+400+200')


def check(elem):
    if not elem.get().replace(".", "").replace(',', '').replace(" ", "").replace("-", "").replace('+', "").isdigit():
        mb.showerror(title="Digit Error", message="Values should be digits in integer or float form")
        return False

    global m
    global val

    val = re.findall(r"-?\d*\.\d+|-?\d+", elem.get())
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
        if sum(n) == 0:
            mb.showerror(title="ZeroDivisionError", message="All values are zeros")
        else:
            self.config(text='y1= ' + str(reduce(lambda x, y: x * y, n) / sum(n)))
    return None


def file(self):
    def change_state(wd, state):
        wd.config(state=state)

    lb1 = Label(self.fffr1, text="n = ", font="Times 14")
    lb2 = Label(self.fffr1, text=" ", font="Times 14")

    lb1.grid(column=0, row=0)
    lb2.grid(column=0, row=1)

    e1 = Entry(self.fffr1, width=20, bg="white", state='disabled')

    e1.bind('<Button-1>', lambda event, wd=e1, state="normal": change_state(wd, state))
    e1.bind('<Return>', lambda event, wd=e1, state="readonly": change_state(wd, state))

    e1.grid(row=0, column=1, columnspan=2)

    self.fffr1.grid(row=0, column=0, padx=10, pady=10)

    lb2 = Label(self.fffr2, text="(n1*n2*...*nm) / (n1+n2+...+nm)", font="Times 14")

    self.lllbb1.grid(column=0, row=1, sticky=W)
    lb2.grid(column=0, row=0, sticky=W)

    self.fffr2.grid(row=0, column=2, padx=10, pady=10)

    but1 = Button(self.fffile_frame, text="Run", font="Times 14", command=lambda sl=self.lllbb1, wd=e1: run(wd, sl))

    but1.grid(row=1, column=1)

    self.fffile_frame.pack(anchor=W)


def generated(self):
    # noinspection PyUnusedLocal
    global m
    m = 45
    res = []

    def generation(lbs):
        nonlocal res
        if len(res):
            res.clear()
        lst = []
        for i in range(1, m + 1):
            lst.append(round(random.random(), ndigits=4))
            res = [i for i in lst]
            if i % 5 == 0:
                print(i, i // 5)
                if i // 5 == 1:
                    lbs[0].config(text='n= ' + str(lst).replace("[", "").replace("]", ","))
                    lst.clear()
                else:
                    print(lst)
                    lbs[i // 5 - 1].config(text="    " + str(lst).replace("[", "").replace("]", ","))
                    lbs[i // 5 - 1].grid()
                    lst.clear()
        self.root.geometry('700x500+600+400')
        return res

    def result():
        nonlocal res
        fn_res = reduce(lambda x, y: x * y, res) / sum(res)
        self.lllbb2.config(text='res= ' + str(fn_res))

    lb1 = Label(self.gggfr1, text="n= ", font="Times 14")
    lb2 = Label(self.gggfr1, font='Times 14')
    lb3 = Label(self.gggfr1, font="Times 14")
    lb4 = Label(self.gggfr1, font="Times 14")
    lb5 = Label(self.gggfr1, font="Times 14")
    lb6 = Label(self.gggfr1, font="Times 14")
    lb7 = Label(self.gggfr1, font="Times 14")
    lb8 = Label(self.gggfr1, font="Times 14")
    lb9 = Label(self.gggfr1, font="Times 14")

    lb1.grid(column=0, row=0)
    lb2.grid(column=0, row=1)
    lb3.grid(column=0, row=2)
    lb4.grid(column=0, row=2)
    lb5.grid(column=0, row=2)
    lb6.grid(column=0, row=2)
    lb7.grid(column=0, row=2)
    lb8.grid(column=0, row=2)
    lb9.grid(column=0, row=2)

    lb3.grid_forget()
    lb4.grid_forget()
    lb5.grid_forget()
    lb6.grid_forget()
    lb7.grid_forget()
    lb8.grid_forget()
    lb9.grid_forget()

    self.gggfr1.grid(row=0, column=0, padx=10, pady=10, sticky=(W, N))

    lb22 = Label(self.gggfr2, text="(n1*n2*...*nm) / (n1+n2+...+nm)", font="Times 14")

    self.lllbb2.grid(column=0, row=1, sticky=W)
    lb22.grid(column=0, row=0, sticky=W)

    self.gggfr2.grid(row=0, column=7, padx=10, pady=10, sticky=(N, W))

    but1 = Button(self.gggenerated_frame, text="Run", font="Times 14", command=result)
    but2 = Button(self.gggenerated_frame, text="Generation", font="Times 14",
                  command=lambda lbs=(lb1, lb2, lb3, lb4, lb5, lb6, lb7, lb8, lb9): generation(lbs=lbs))

    but1.grid(row=1, column=1)
    but2.grid(row=1, column=0)

    self.gggenerated_frame.pack(anchor=W)


def from_file(self):
    def open_file():
        global m
        fl = fd.askopenfile(mode='r', filetypes=[('Text Files', '*.txt')])
        if fl:
            ffl = open(fl.name, 'r')
            st = ffl.read()
            content = re.findall(r"-?\d*\.\d+|-?\d+", st)
            if len(content):
                lk = len(content)
                if not st.replace(".", "").replace(',', '').replace(" ", "").replace("-", "").replace('+', "").replace(
                        '\n', "").isdigit():
                    mb.showerror(title="Digit Error", message="Values should be digits in integer or float form")
                    ask = mb.askquestion(title="",
                                         message="Do you want to generate values?")
                    if ask == 'yes':
                        for i in range(m):
                            content.append(random.random())
                        fl = open(fl.name, 'w')
                        for i in range(m):
                            fl.write(str(content[i]) + ',')
                        fl.close()
                if len(content) < m:
                    ask = mb.askquestion(title="warning",
                                         message="number ov values less then m = 35 generate others?")
                    if ask == 'yes':
                        for i in range(m - lk):
                            content.append(random.random())
                        fl = open(fl.name, 'a')
                        for i in range(lk, m):
                            fl.write(str(content[i]) + ',')
                        fl.close()
            else:
                ask = mb.askquestion(title="Warning",
                                     message="File is empty, generate values?")
                if ask == 'yes':
                    for i in range(m):
                        content.append(random.random())
                    fl = open(fl.name, 'w')
                    for i in range(m):
                        fl.write(str(content[i]) + ',')
                    fl.close()
            content = [float(i) for i in content]
            self.lllbb3.config(text='y1= ' + str(reduce(lambda x, y: x * y, content) / sum(content)))
            return None

    lb1 = Label(self.fffrom_fl, text="Please create *.txt file with content like 1, 20.255, ...", font="Times 14")

    lb1.grid(row=0, column=0, padx=10, pady=10)

    self.lllbb3.grid(column=0, row=1, sticky=W)

    lb2 = Label(self.ffflfr1, text="(n1*n2*...*nm) / (n1+n2+...+nm)", font="Times 14")

    lb2.grid(column=0, row=0, sticky=W)

    self.ffflfr1.grid(row=1, column=0, padx=10, pady=10, sticky=W)

    but1 = Button(self.fffrom_fl, text="Search", font="Times 14", command=open_file)

    but1.grid(row=20, column=0, sticky=(N, W, S, E), padx=10, columnspan=5)

    self.fffrom_fl.pack(anchor=W)

import math
import time
from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog as fd
import re
import random

start_time = 0


def quick_sort(x):
    # global start_time
    # start_time = time.time()
    if len(x) < 2:
        return x
    else:
        pivot = x[len(x) // 2]
        less = [i for i in x[1:] if i <= pivot]
        greater = [i for i in x[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


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
                res = math.pow(s, (a / b + c)) + math.pow(d, (c / b + a))
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
    lb1 = Label(self.fr1, text="1 = ", font="Times 14")
    lb2 = Label(self.fr1, text="2 = ", font="Times 14")
    lb3 = Label(self.fr1, text="3 = ", font="Times 14")
    lb4 = Label(self.fr1, text="4 = ", font="Times 14")
    lb5 = Label(self.fr1, text="5 = ", font="Times 14")
    lb6 = Label(self.fr1, text="6 = ", font="Times 14")
    lb7 = Label(self.fr1, text="7 = ", font="Times 14")
    lb8 = Label(self.fr1, text="8 = ", font="Times 14")
    lb9 = Label(self.fr1, text="9 = ", font="Times 14")
    lb10 = Label(self.fr1, text="10 = ", font="Times 14")

    lb1.grid(column=0, row=0)
    lb2.grid(column=0, row=1)
    lb3.grid(column=0, row=2)
    lb4.grid(column=0, row=3)
    lb5.grid(column=0, row=4)
    lb6.grid(column=0, row=5)
    lb7.grid(column=0, row=6)
    lb8.grid(column=0, row=7)
    lb9.grid(column=0, row=8)
    lb10.grid(column=0, row=9)

    e1 = Entry(self.fr1, width=100, bg="white", state='normal')
    e2 = Entry(self.fr1, width=100, bg="white", state='normal')
    e3 = Entry(self.fr1, width=100, bg="white", state='normal')
    e4 = Entry(self.fr1, width=100, bg="white", state='normal')
    e5 = Entry(self.fr1, width=100, bg="white", state='normal')
    e6 = Entry(self.fr1, width=100, bg="white", state='normal')
    e7 = Entry(self.fr1, width=100, bg="white", state='normal')
    e8 = Entry(self.fr1, width=100, bg="white", state='normal')
    e9 = Entry(self.fr1, width=100, bg="white", state='normal')
    e10 = Entry(self.fr1, width=100, bg="white", state='normal')

    e1.grid(row=0, column=1, columnspan=2)
    e2.grid(row=1, column=1, columnspan=2)
    e3.grid(row=2, column=1, columnspan=2)
    e4.grid(row=3, column=1, columnspan=2)
    e5.grid(row=4, column=1, columnspan=2)
    e6.grid(row=5, column=1, columnspan=2)
    e7.grid(row=6, column=1, columnspan=2)
    e8.grid(row=7, column=1, columnspan=2)
    e9.grid(row=8, column=1, columnspan=2)
    e10.grid(row=9, column=1, columnspan=2)

    self.fr1.grid(row=0, column=0, padx=10, pady=10)
    self.lbb1.grid(column=0, row=1, sticky=W)

    but1 = Button(self.file_frame, text="Run", font="Times 14",
                  command=lambda lst=(e1, e2, e3, e4, e5), sl=self.lbb1: run(lst, sl))

    but1.grid(row=1, column=0, sticky=N)

    self.file_frame.pack(anchor=W)


def generated(self):

    res = []

    def generation():
        lst = [e11, e12, e13, e14, e15, e16, e17, e18, e19, e20]
        lst2 = [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10]
        nonlocal res
        if check(lst):
            em = list()
            for i in lst:
                em.append(re.findall(r"-?\d+", i.get()))
            em = [int(i[0]) for i in em]
            for i in em:
                if i <= 0:
                    mb.showerror(title="Incorrect amount", message="n should be > 0")
                    return
                else:
                    continue
            k = 0
            for i in lst2:
                i.delete(0, END)
                j = k
                while j <= len(em):
                    if em[j] > 10000:
                        a = [random.randrange(-em[j], em[j]) for i in range(em[j])]
                        res.append(a)
                        mb.showwarning(title="Too big value",
                                       message="n > 10000 so in entry will be shown only 10000 values \n"
                                               "Because app will be slow down")
                        i.insert(0, str(list(a[i] for i in range(10000))))
                        k += 1
                        break
                    else:
                        a = [random.randrange(-em[j], em[j]) for i in range(em[j])]
                        res.append(a)
                        i.insert(0, str(a))
                        k += 1
                        break
        return

    def g_run():
        nonlocal res
        t = []
        final = []
        if res:
            for i in res:
                start_time = time.time()
                final.append(quick_sort(i))
                t.append(time.time() - start_time)
        # print(final)
        print("exit norm")
        print(t)
        print(len(final[9]))
        res.clear()


    lb1 = Label(self.gfr1, text="1 = ", font="Times 14")
    lb2 = Label(self.gfr1, text="2 = ", font="Times 14")
    lb3 = Label(self.gfr1, text="3 = ", font="Times 14")
    lb4 = Label(self.gfr1, text="4 = ", font="Times 14")
    lb5 = Label(self.gfr1, text="5 = ", font="Times 14")
    lb6 = Label(self.gfr1, text="6 = ", font="Times 14")
    lb7 = Label(self.gfr1, text="7 = ", font="Times 14")
    lb8 = Label(self.gfr1, text="8 = ", font="Times 14")
    lb9 = Label(self.gfr1, text="9 = ", font="Times 14")
    lb10 = Label(self.gfr1, text="10 = ", font="Times 14")

    lb1.grid(column=0, row=0)
    lb2.grid(column=0, row=1)
    lb3.grid(column=0, row=2)
    lb4.grid(column=0, row=3)
    lb5.grid(column=0, row=4)
    lb6.grid(column=0, row=5)
    lb7.grid(column=0, row=6)
    lb8.grid(column=0, row=7)
    lb9.grid(column=0, row=8)
    lb10.grid(column=0, row=9)

    e1 = Entry(self.gfr1, width=100, bg="white", state='normal')
    e2 = Entry(self.gfr1, width=100, bg="white", state='normal')
    e3 = Entry(self.gfr1, width=100, bg="white", state='normal')
    e4 = Entry(self.gfr1, width=100, bg="white", state='normal')
    e5 = Entry(self.gfr1, width=100, bg="white", state='normal')
    e6 = Entry(self.gfr1, width=100, bg="white", state='normal')
    e7 = Entry(self.gfr1, width=100, bg="white", state='normal')
    e8 = Entry(self.gfr1, width=100, bg="white", state='normal')
    e9 = Entry(self.gfr1, width=100, bg="white", state='normal')
    e10 = Entry(self.gfr1, width=100, bg="white", state='normal')

    e1.grid(row=0, column=1, columnspan=2)
    e2.grid(row=1, column=1, columnspan=2)
    e3.grid(row=2, column=1, columnspan=2)
    e4.grid(row=3, column=1, columnspan=2)
    e5.grid(row=4, column=1, columnspan=2)
    e6.grid(row=5, column=1, columnspan=2)
    e7.grid(row=6, column=1, columnspan=2)
    e8.grid(row=7, column=1, columnspan=2)
    e9.grid(row=8, column=1, columnspan=2)
    e10.grid(row=9, column=1, columnspan=2)

    self.gfr1.grid(row=0, column=0, padx=10, pady=10)

    lb1 = Label(self.gfr2, text="n = ", font="Times 14")
    lb2 = Label(self.gfr2, text="n = ", font="Times 14")
    lb3 = Label(self.gfr2, text="n = ", font="Times 14")
    lb4 = Label(self.gfr2, text="n = ", font="Times 14")
    lb5 = Label(self.gfr2, text="n = ", font="Times 14")
    lb6 = Label(self.gfr2, text="n = ", font="Times 14")
    lb7 = Label(self.gfr2, text="n = ", font="Times 14")
    lb8 = Label(self.gfr2, text="n = ", font="Times 14")
    lb9 = Label(self.gfr2, text="n = ", font="Times 14")
    lb10 = Label(self.gfr2, text="n = ", font="Times 14")

    lb1.grid(column=3, row=0)
    lb2.grid(column=3, row=1)
    lb3.grid(column=3, row=2)
    lb4.grid(column=3, row=3)
    lb5.grid(column=3, row=4)
    lb6.grid(column=3, row=5)
    lb7.grid(column=3, row=6)
    lb8.grid(column=3, row=7)
    lb9.grid(column=3, row=8)
    lb10.grid(column=3, row=9)

    e11 = Entry(self.gfr2, width=10, bg="white", state='normal')
    e12 = Entry(self.gfr2, width=10, bg="white", state='normal')
    e13 = Entry(self.gfr2, width=10, bg="white", state='normal')
    e14 = Entry(self.gfr2, width=10, bg="white", state='normal')
    e15 = Entry(self.gfr2, width=10, bg="white", state='normal')
    e16 = Entry(self.gfr2, width=10, bg="white", state='normal')
    e17 = Entry(self.gfr2, width=10, bg="white", state='normal')
    e18 = Entry(self.gfr2, width=10, bg="white", state='normal')
    e19 = Entry(self.gfr2, width=10, bg="white", state='normal')
    e20 = Entry(self.gfr2, width=10, bg="white", state='normal')

    e11.grid(row=0, column=4, columnspan=1)
    e12.grid(row=1, column=4, columnspan=1)
    e13.grid(row=2, column=4, columnspan=1)
    e14.grid(row=3, column=4, columnspan=1)
    e15.grid(row=4, column=4, columnspan=1)
    e16.grid(row=5, column=4, columnspan=1)
    e17.grid(row=6, column=4, columnspan=1)
    e18.grid(row=7, column=4, columnspan=1)
    e19.grid(row=8, column=4, columnspan=1)
    e20.grid(row=9, column=4, columnspan=1)

    self.gfr2.grid(row=0, column=1, padx=10, pady=10)

    but1 = Button(self.generated_frame, text="Run", font="Times 14",
                  command=g_run)
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

from tkinter import *
import random

class Lab1:
    def __init__(self):
        self.root = Tk()
        self.file_frame = Frame(self.root)
        self.fr1 = LabelFrame(self.file_frame, text="Firs task", font="Serif 14")
        self.fr2 = LabelFrame(self.file_frame, text="Results", font="Serif 14")
        self.generated_frame = Frame(self.root)
        self.gfr1 = LabelFrame(self.generated_frame, text="Firs task", font="Serif 14")
        self.gfr2 = LabelFrame(self.generated_frame, text="Results", font="Serif 14")

    def main_window(self):
        self.root.title("lab1")
        self.root.geometry('500x300+600+400')
        var = IntVar()
        var.set(0)


        def rad():
            if var.get() == 0:
                self.file()
                self.generated_frame.pack_forget()
                self.gfr1.grid_forget()
            else:
                self.file_frame.pack_forget()
                self.fr1.grid_forget()
                self.fr2.grid_forget()
                self.generated()

        r1 = Radiobutton(text="File", variable=var, value=0, command=rad, font="Serif 14")
        r2 = Radiobutton(text="Generated", variable=var, value=1, font="Serif 14", command=rad)

        r1.pack(anchor=W)
        r2.pack(anchor=W)

        self.file()
        self.root.mainloop()

    def file(self):
        def change_state(wd, state):
            wd.config(state=state)

        lb1 = Label(self.fr1, text="a = ", font="Serif 14").grid(column=0, row=0)
        lb2 = Label(self.fr1, text="b = ", font="Serif 14").grid(column=0, row=1)
        lb3 = Label(self.fr1, text="c = ", font="Serif 14").grid(column=0, row=2)
        lb4 = Label(self.fr1, text="d = ", font="Serif 14").grid(column=0, row=3)
        lb5 = Label(self.fr1, text="s = ", font="Serif 14").grid(column=0, row=4)

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

        lb1 = Label(self.fr2, text="y1 = ", font="Serif 14").grid(column=0, row=0)
        lb2 = Label(self.fr2, text=" ", font="Serif 14").grid(column=0, row=1)
        lb3 = Label(self.fr2, text=" ", font="Serif 14").grid(column=0, row=2)
        lb4 = Label(self.fr2, text=" ", font="Serif 14").grid(column=0, row=3)
        lb5 = Label(self.fr2, text=" ", font="Serif 14").grid(column=0, row=4)

        self.fr2.grid(row=0, column=2, padx=10, pady=10)

        but1 = Button(self.file_frame, text="Run", font="Serif 14").grid(row=1, column=1)

        self.file_frame.pack(anchor=W)

    def generated(self):
        lb1 = Label(self.gfr1, text="a = ", font="Serif 14").grid(column=0, row=0)
        lb2 = Label(self.gfr1, text="b = ", font="Serif 14").grid(column=0, row=1)
        lb3 = Label(self.gfr1, text="c = ", font="Serif 14").grid(column=0, row=2)
        lb4 = Label(self.gfr1, text="d = ", font="Serif 14").grid(column=0, row=3)
        lb5 = Label(self.gfr1, text="s = ", font="Serif 14").grid(column=0, row=4)

        e1 = Entry(self.gfr1, width=20, bg="white", state='normal')
        e1.grid(row=0, column=1, columnspan=2)

        e2 = Entry(self.gfr1, width=20, bg="white")
        e2.insert(0, str(random.random()))
        # e2.config(state="readonly")
        e2.grid(row=1, column=1, columnspan=2)

        e3 = Entry(self.gfr1, width=20, bg="white", state='disabled')
        e3.grid(row=2, column=1, columnspan=2)

        e4 = Entry(self.gfr1, width=20, bg="white", state='disabled')
        e4.grid(row=3, column=1, columnspan=2)

        e5 = Entry(self.gfr1, width=20, bg="white", state='disabled')
        e5.grid(row=4, column=1, columnspan=2)

        self.gfr1.grid(row=0, column=0, padx=10, pady=10)

        # lb1 = Label(self.fr2, text="y1 = ", font="Serif 14").grid(column=0, row=0)
        # lb2 = Label(self.fr2, text=" ", font="Serif 14").grid(column=0, row=1)
        # lb3 = Label(self.fr2, text=" ", font="Serif 14").grid(column=0, row=2)
        # lb4 = Label(self.fr2, text=" ", font="Serif 14").grid(column=0, row=3)
        # lb5 = Label(self.fr2, text=" ", font="Serif 14").grid(column=0, row=4)
        #
        # self.fr2.grid(row=0, column=2, padx=10, pady=10)
        #
        # but1 = Button(self.file_frame, text="Run", font="Serif 14").grid(row=1, column=1)

        self.generated_frame.pack(anchor=W)


window = Lab1()
window.main_window()

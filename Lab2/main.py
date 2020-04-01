import os
import fnmatch
from tkinter import *
from tkinter import messagebox as mb
import first_task


class Lab1:
    def __init__(self):
        self.root = Tk()

        # Create Gui  for first task
        self.file_frame = Frame(self.root)
        self.fr1 = LabelFrame(self.file_frame,
                              text="First task",
                              font="Times 14")

        self.generated_frame = Frame(self.root)
        self.gfr1 = LabelFrame(self.generated_frame,
                               text="First task",
                               font="Times 14")
        self.gfr2 = LabelFrame(self.generated_frame,
                               text="Results",
                               font="Times 14")

        self.from_fl = Frame(self.root)

    def main_window(self):
        win = first_task
        self.root.title("lab1")
        self.root.geometry('910x500+400+200')

        var = IntVar()
        var.set(0)

        mainmenu = Menu(self.root)
        self.root.config(menu=mainmenu)

        filemenu = Menu(mainmenu, tearoff=0)
        filemenu.add_command(label="Exit", font="Times 14", command=sys.exit)
        mainmenu.add_cascade(label="Menu", font="Times 14", menu=filemenu)

        def rad():
            nonlocal win
            if var.get() == 0:
                win.file(self)
                self.generated_frame.pack_forget()
                self.gfr1.grid_forget()
                self.gfr2.grid_forget()
                self.from_fl.pack_forget()

            elif var.get() == 2:
                win.from_file(self)
                self.file_frame.pack_forget()
                self.fr1.grid_forget()
                self.generated_frame.pack_forget()
                self.gfr1.grid_forget()
                self.gfr2.grid_forget()

            else:
                win.generated(self)
                self.file_frame.pack_forget()
                self.fr1.grid_forget()
                self.from_fl.pack_forget()

        r1 = Radiobutton(text="By hands", variable=var,
                         value=0, command=rad, font="Times 14")
        r2 = Radiobutton(text="Generated", variable=var,
                         value=1, font="Times 14", command=rad)
        r3 = Radiobutton(text="From File", variable=var,
                         value=2, font="Times 14", command=rad)

        r1.pack(anchor=W)
        r2.pack(anchor=W)
        r3.pack(anchor=W)

        win.file(self)

        def on_closing():
            files = (fnmatch.filter(os.listdir(), "Result?.tx?"))
            if files:
                msg = str(files).replace("[", "").replace("]", "")
                y = mb.askquestion(title="Results",
                                   message="Remove file {} ?".format(msg))
                if y == 'yes':
                    for i in files:
                        os.remove(i)
            sys.exit()

        self.root.protocol("WM_DELETE_WINDOW", on_closing)
        self.root.mainloop()


window = Lab1()
window.main_window()

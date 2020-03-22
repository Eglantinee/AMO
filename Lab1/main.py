from tkinter import *
import first_task
import second_task
import third_task


class Lab1:
    def __init__(self):
        self.root = Tk()

        # Create Gui  for first task
        self.file_frame = Frame(self.root)
        self.fr1 = LabelFrame(self.file_frame, text="First task", font="Times 16")
        self.fr2 = LabelFrame(self.file_frame, text="Results", font="Times 14")

        self.generated_frame = Frame(self.root)
        self.gfr1 = LabelFrame(self.generated_frame, text="First task", font="Times 14")
        self.gfr2 = LabelFrame(self.generated_frame, text="Results", font="Times 14")

        self.from_fl = Frame(self.root)
        self.flfr1 = LabelFrame(self.from_fl, text="Results", font="Times 14")

        self.lbb1 = Label(self.fr2, text="y1 = ", font="Times 14")
        self.lbb2 = Label(self.gfr2, text="y1= ", font="Times 14")
        self.lbb3 = Label(self.flfr1, text="y1= ", font="Times 14")

        # Create Gui for second task
        self.ffile_frame = Frame(self.root)
        self.ffr1 = LabelFrame(self.ffile_frame, text="First task", font="Times 16")
        self.ffr2 = LabelFrame(self.ffile_frame, text="Results", font="Times 14")

        self.ggenerated_frame = Frame(self.root)
        self.ggfr1 = LabelFrame(self.ggenerated_frame, text="First task", font="Times 14")
        self.ggfr2 = LabelFrame(self.ggenerated_frame, text="Results", font="Times 14")

        self.ffrom_fl = Frame(self.root)
        self.fflfr1 = LabelFrame(self.ffrom_fl, text="Results", font="Times 14")

        self.llbb1 = Label(self.ffr2, text="res= ", font="Times 14")
        self.llbb2 = Label(self.ggfr2, text="res= ", font="Times 14")
        self.llbb3 = Label(self.fflfr1, text="res= ", font="Times 14")

        # Create GUI for last (third) task
        self.fffile_frame = Frame(self.root)
        self.fffr1 = LabelFrame(self.fffile_frame, text="First task", font="Times 16")
        self.fffr2 = LabelFrame(self.fffile_frame, text="Results", font="Times 14")

        self.gggenerated_frame = Frame(self.root)
        self.gggfr1 = LabelFrame(self.gggenerated_frame, text="First task", font="Times 14")
        self.gggfr2 = LabelFrame(self.gggenerated_frame, text="Results", font="Times 14")

        self.fffrom_fl = Frame(self.root)
        self.ffflfr1 = LabelFrame(self.fffrom_fl, text="Results", font="Times 14")

        self.lllbb1 = Label(self.fffr2, text="res= ", font="Times 14")
        self.lllbb2 = Label(self.gggfr2, text="res= ", font="Times 14")
        self.lllbb3 = Label(self.ffflfr1, text="res= ", font="Times 14")

    def main_window(self):
        win = first_task
        self.root.title("lab1")
        self.root.geometry('630x400+400+200')

        var = IntVar()
        var.set(0)

        def change_window(wind):
            nonlocal win
            win = wind
            win.size_and_title(self)
            nonlocal var
            var.set(0)
            rad()
            return win

        mainmenu = Menu(self.root)
        self.root.config(menu=mainmenu)

        filemenu = Menu(mainmenu, tearoff=0)
        filemenu.add_command(label="First Task", font="Times 14", command=lambda wind=first_task: change_window(wind))
        filemenu.add_command(label="Second Task", font="Times 14", command=lambda wind=second_task: change_window(wind))
        filemenu.add_command(label="Third Task", font="Times 14", command=lambda wind=third_task: change_window(wind))
        mainmenu.add_cascade(label="Tasks", font="Times 14", menu=filemenu)

        def rad():
            if win == first_task:
                self.ffile_frame.pack_forget()
                self.ffr1.grid_forget()
                self.ffr2.grid_forget()
                self.ggenerated_frame.pack_forget()
                self.ggfr1.grid_forget()
                self.ggfr2.grid_forget()
                self.ffrom_fl.pack_forget()
                self.fflfr1.grid_forget()

                self.fffile_frame.pack_forget()
                self.fffr1.grid_forget()
                self.fffr2.grid_forget()
                self.gggenerated_frame.pack_forget()
                self.gggfr1.grid_forget()
                self.gggfr2.grid_forget()
                self.fffrom_fl.pack_forget()
                self.ffflfr1.grid_forget()

                if var.get() == 0:
                    win.file(self)
                    self.generated_frame.pack_forget()
                    self.gfr1.grid_forget()
                    self.gfr2.grid_forget()
                    self.from_fl.pack_forget()
                    self.flfr1.grid_forget()

                    self.lbb1.configure(text="y1= ")
                    self.lbb2.configure(text="y1= ")
                    self.lbb3.configure(text='y1= ')

                elif var.get() == 2:
                    win.from_file(self)
                    self.file_frame.pack_forget()
                    self.fr1.grid_forget()
                    self.fr2.grid_forget()
                    self.generated_frame.pack_forget()
                    self.gfr1.grid_forget()
                    self.gfr2.grid_forget()

                    self.lbb1.configure(text="y1= ")
                    self.lbb2.configure(text="y1= ")
                    self.lbb3.configure(text='y1= ')

                else:
                    win.generated(self)
                    self.file_frame.pack_forget()
                    self.fr1.grid_forget()
                    self.fr2.grid_forget()
                    self.from_fl.pack_forget()
                    self.flfr1.grid_forget()

                    self.lbb1.configure(text="y1= ")
                    self.lbb2.configure(text="y1= ")
                    self.lbb3.configure(text='y1= ')
            elif win == second_task:
                self.file_frame.pack_forget()
                self.fr1.grid_forget()
                self.fr2.grid_forget()
                self.generated_frame.pack_forget()
                self.gfr1.grid_forget()
                self.gfr2.grid_forget()
                self.from_fl.pack_forget()
                self.flfr1.grid_forget()

                self.fffile_frame.pack_forget()
                self.fffr1.grid_forget()
                self.fffr2.grid_forget()
                self.gggenerated_frame.pack_forget()
                self.gggfr1.grid_forget()
                self.gggfr2.grid_forget()
                self.fffrom_fl.pack_forget()
                self.ffflfr1.grid_forget()

                if var.get() == 0:
                    win.file(self)
                    self.ggenerated_frame.pack_forget()
                    self.ggfr1.grid_forget()
                    self.ggfr2.grid_forget()
                    self.ffrom_fl.pack_forget()
                    self.fflfr1.grid_forget()

                    self.lllbb1.configure(text="f= ")
                    self.lllbb2.configure(text="f= ")
                    self.lllbb3.configure(text='f= ')

                elif var.get() == 2:
                    win.from_file(self)
                    self.ffile_frame.pack_forget()
                    self.ffr1.grid_forget()
                    self.ffr2.grid_forget()
                    self.ggenerated_frame.pack_forget()
                    self.ggfr1.grid_forget()
                    self.ggfr2.grid_forget()

                    self.llbb1.configure(text="res= ")
                    self.llbb2.configure(text="res= ")
                    self.llbb3.configure(text='res= ')

                else:
                    win.generated(self)
                    self.ffile_frame.pack_forget()
                    self.ffr1.grid_forget()
                    self.ffr2.grid_forget()
                    self.ffrom_fl.pack_forget()
                    self.fflfr1.grid_forget()

                    self.llbb1.configure(text="res= ")
                    self.llbb2.configure(text="res= ")
                    self.llbb3.configure(text='res= ')
            else:
                self.file_frame.pack_forget()
                self.fr1.grid_forget()
                self.fr2.grid_forget()
                self.generated_frame.pack_forget()
                self.gfr1.grid_forget()
                self.gfr2.grid_forget()
                self.from_fl.pack_forget()
                self.flfr1.grid_forget()

                self.ffile_frame.pack_forget()
                self.ffr1.grid_forget()
                self.ffr2.grid_forget()
                self.ggenerated_frame.pack_forget()
                self.ggfr1.grid_forget()
                self.ggfr2.grid_forget()
                self.ffrom_fl.pack_forget()
                self.fflfr1.grid_forget()

                if var.get() == 0:
                    win.file(self)
                    self.gggenerated_frame.pack_forget()
                    self.gggfr1.grid_forget()
                    self.gggfr2.grid_forget()
                    self.fffrom_fl.pack_forget()
                    self.ffflfr1.grid_forget()

                    self.lllbb1.configure(text="f= ")
                    self.lllbb2.configure(text="f= ")
                    self.lllbb3.configure(text='f= ')

                elif var.get() == 2:
                    win.from_file(self)
                    self.fffile_frame.pack_forget()
                    self.fffr1.grid_forget()
                    self.fffr2.grid_forget()
                    self.gggenerated_frame.pack_forget()
                    self.gggfr1.grid_forget()
                    self.gggfr2.grid_forget()

                    self.lllbb1.configure(text="f= ")
                    self.lllbb2.configure(text="f= ")
                    self.lllbb3.configure(text='f= ')

                else:
                    win.generated(self)
                    self.fffile_frame.pack_forget()
                    self.fffr1.grid_forget()
                    self.fffr2.grid_forget()
                    self.fffrom_fl.pack_forget()
                    self.ffflfr1.grid_forget()

                    self.lllbb1.configure(text="f= ")
                    self.lllbb2.configure(text="f= ")
                    self.lllbb3.configure(text='f= ')

        r1 = Radiobutton(text="By hands", variable=var, value=0, command=rad, font="Times 14")
        r2 = Radiobutton(text="Generated", variable=var, value=1, font="Times 14", command=rad)
        r3 = Radiobutton(text="From File", variable=var, value=2, font="Times 14", command=rad)

        r1.pack(anchor=W)
        r2.pack(anchor=W)
        r3.pack(anchor=W)

        win.file(self)
        self.root.mainloop()


window = Lab1()
window.main_window()

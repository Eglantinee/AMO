from tkinter import *
import first_task
import second_task
import third_task


class Lab1:
    def __init__(self):
        self.root = Tk()
        self.file_frame = Frame(self.root)
        self.fr1 = LabelFrame(self.file_frame, text="First task", font="Times 16")
        self.fr2 = LabelFrame(self.file_frame, text="Results", font="Times 14")
        self.generated_frame = Frame(self.root)
        self.gfr1 = LabelFrame(self.generated_frame, text="First task", font="Times 14")
        self.gfr2 = LabelFrame(self.generated_frame, text="Results", font="Times 14")
        self.from_fl = Frame(self.root)
        self.flfr1 = LabelFrame(self.from_fl, text="Results", font="Times 14")
        self.lbb1 = Label(self.fr2, text="y1 = ", font="Times 14")
        self.lbb2 = Label(self.gfr2, text="y1 = ", font="Times 14")
        self.lbb3 = Label(self.flfr1, text="y1 = ", font="Times 14")

    def main_window(self):
        win = second_task
        self.root.title("lab1")
        self.root.geometry('600x300+600+400')

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
        filemenu.add_command(label="First Task", command=lambda wind=first_task: change_window(wind))
        filemenu.add_command(label="Third Task", command=lambda wind=third_task: change_window(wind))
        filemenu.add_command(label="Сохранить...")
        filemenu.add_command(label="Выход")
        mainmenu.add_cascade(label="Файл", menu=filemenu)

        def rad():
            if var.get() == 0:
                win.file(self)
                self.generated_frame.pack_forget()
                self.gfr1.grid_forget()
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
                self.file_frame.pack_forget()
                self.fr1.grid_forget()
                self.fr2.grid_forget()
                self.from_fl.pack_forget()
                self.flfr1.grid_forget()
                self.lbb1.configure(text="y1= ")
                self.lbb2.configure(text="y1= ")
                self.lbb3.configure(text='y1= ')
                win.generated(self)

        r1 = Radiobutton(text="File", variable=var, value=0, command=rad, font="Times 14")
        r2 = Radiobutton(text="Generated", variable=var, value=1, font="Times 14", command=rad)
        r3 = Radiobutton(text="Generated", variable=var, value=2, font="Times 14", command=rad)

        r1.pack(anchor=W)
        r2.pack(anchor=W)
        r3.pack(anchor=W)

        win.file(self)
        self.root.mainloop()


window = Lab1()
window.main_window()

# todo 1: Catch large result
# todo 2: 3 characters after coma

# todo 4: mb check and run global functions?
# todo 5: remove repeatable code
# todo 6: make 3 window
# todo 7: make output from file

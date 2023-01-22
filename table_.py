# ****************tkinter GUI **********************************
from tkinter import Tk, Label, CENTER
from tkinter.ttk import Button, Style, Treeview


class Window(Tk):
    def __init__(self):
        super().__init__()
        self.e = None
        self.wm_title("form")
        self.geometry("550x420")

        style = Style()
        style.configure('2.TButton', font=('arial', 25))
        exit_button = Button(self,
                             text="show tabel",
                             style="2.TButton",
                             command=self.receive)
        exit_button.place(x=130, y=350, width=230, height=50)

        # show a label
        self.label = Label(self,
                           text='This is a label',
                           font=('arial', 30, 'bold'),
                           borderwidth=1,
                           relief="solid")
        self.label.place(x=80, y=20)
        # self.label.pack()

    def receive(self):
        style = Style()
        style.theme_use('clam')

        # Add the rowheight
        # Modify the font of the body
        style.configure('Treeview', rowheight=40, font=('arial', 20))
        # Modify the font of the headings
        style.configure("Treeview.Heading", font=('Calibri', 20, 'bold'))

        # Add a Treeview widget
        tree = Treeview(self.label,
                        column=("c1", "c2", "c3"),
                        show='headings',
                        height=6)
        tree.column("# 1", anchor=CENTER, width=50)
        tree.heading("# 1", text="ID")

        tree.column("# 2", anchor=CENTER, width=150)
        tree.heading("# 2", text="FName")

        tree.column("# 3", anchor=CENTER, width=150)
        tree.heading("# 3", text="LName")

        # Insert the data in Treeview widget
        tree.insert('', 'end', values=('1', 'Joe', 'Nash'))
        tree.insert('', 'end', values=('2', 'Emily', 'Mackmohan'))
        tree.insert('', 'end', values=('3', 'Estilla', 'Roffe'))
        tree.insert('', 'end', values=('4', 'Percy', 'Andrews'))
        tree.insert('', 'end', values=('5', 'Stephan', 'Heyward'))

        tree.pack()


if __name__ == "__main__":
    app = Window()
    app.mainloop()

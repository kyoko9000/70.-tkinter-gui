# ****************tkinter GUI **********************************
from tkinter import Tk, Label, CENTER
from tkinter.ttk import Button, Style, Treeview


class Window(Tk):
    def __init__(self):
        super().__init__()
        self.tree = None
        self.e = None
        self.wm_title("form")
        self.geometry("550x420")

        style = Style()
        style.configure('2.TButton', font=('arial', 25))

        button_1 = Button(self,
                          text="show tabel",
                          style="2.TButton",
                          command=self.add_data)
        button_1.place(x=50, y=350, width=100, height=50)

        button_2 = Button(self,
                          text="edit row",
                          style="2.TButton",
                          command=self.edit)
        button_2.place(x=200, y=350, width=100, height=50)

        button_3 = Button(self,
                          text="delete row",
                          style="2.TButton",
                          command=self.delete)
        button_3.place(x=350, y=350, width=100, height=50)

        # show a label
        self.label = Label(self,
                           text='This is a label',
                           font=('arial', 30, 'bold'),
                           borderwidth=1,
                           relief="solid")
        self.label.place(x=80, y=20)
        # self.label.pack()

        # ======================treeview===========================
        style = Style()
        style.theme_use('clam')

        # Add the rowheight
        # Modify the font of the body
        style.configure('Treeview', rowheight=40, font=('arial', 20))
        # Modify the font of the headings
        style.configure("Treeview.Heading", font=('Calibri', 20, 'bold'))

        # Add a Treeview widget
        self.tree = Treeview(self.label,
                             column=("c1", "c2", "c3"),
                             show='headings',
                             height=6)
        self.tree.column("# 1", anchor=CENTER, width=50)
        self.tree.heading("# 1", text="ID")

        self.tree.column("# 2", anchor=CENTER, width=150)
        self.tree.heading("# 2", text="FName")

        self.tree.column("# 3", anchor=CENTER, width=150)
        self.tree.heading("# 3", text="LName")

    def add_data(self):
        # Insert the data in Treeview widget
        self.tree.insert('', 'end', values=('1', 'Joe', 'Nash'))
        self.tree.insert('', 'end', values=('2', 'Emily', 'Mackmohan'))
        self.tree.insert('', 'end', values=('3', 'Estilla', 'Roffe'))
        self.tree.insert('', 'end', values=('4', 'Percy', 'Andrews'))
        self.tree.insert('', 'end', values=('5', 'Stephan', 'Heyward'))

        self.tree.pack()

    def edit(self):
        # Get selected item to Edit
        selected_item = self.tree.selection()[0]
        print("row number", selected_item)
        # update 1 row in treeview
        self.tree.item(selected_item, text="blub", values=("num", "foo", "bar"))
        # update 1 cell in treeview
        # self.tree.set(selected_item, column=1, value="your value")

    def delete(self):
        # Get selected item to Delete
        selected_item = self.tree.selection()[0]
        print("row number", selected_item)
        self.tree.delete(selected_item)


if __name__ == "__main__":
    app = Window()
    app.mainloop()

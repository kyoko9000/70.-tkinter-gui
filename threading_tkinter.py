# ****************tkinter GUI **********************************
import random
import threading
import time
from tkinter import Tk, Label, CENTER
from tkinter.ttk import Button, Style, Treeview


class Window(Tk):
    def __init__(self):
        super().__init__()
        self.stop_thread = 0
        self.count = 3
        self.tree = None
        self.e = None
        self.wm_title("form")
        self.geometry("550x420")

        button_1 = Button(self, text="start thread", command=self.add_thread)
        button_1.place(x=50, y=350, width=100, height=50)

        button_2 = Button(self, text="stop thread", command=self.stop_threading)
        button_2.place(x=200, y=350, width=100, height=50)

        # show a label
        self.label = Label(self, text='This is a label')
        # self.label.place(x=80, y=20)
        self.label.pack()

        # ======================treeview===========================
        style = Style()
        style.theme_use('clam')  # 'clam', 'alt', 'default', 'classic'
        style.configure('Treeview', rowheight=40, font=('arial', 20))
        # Modify the font of the headings
        style.configure("Treeview.Heading", font=('Calibri', 20, 'bold'))
        # Add a Treeview widget
        self.tree = Treeview(self.label,
                             column=("c1", "c2", "c3"),
                             show='headings',
                             height=6)
        self.tree.column("# 1", anchor=CENTER, width=150)
        self.tree.heading("# 1", text="thread num")

        self.tree.column("# 2", anchor=CENTER, width=150)
        self.tree.heading("# 2", text="count")

        self.tree.column("# 3", anchor=CENTER, width=150)
        self.tree.heading("# 3", text="status")

        self.tree.pack()

    def add_table(self):
        item_count = self.tree.get_children()
        if len(item_count) == self.count:
            pass
        else:
            # Insert the data in Treeview widget
            self.tree.insert('', 'end', values=('', '', ''))

    def add_thread(self):
        for i in range(self.count):
            self.add_table()
            thread = threading.Thread(target=self.update_num, args=(i,))
            thread.start()

    def update_num(self, num):
        self.stop_thread = 0
        print("thread number: ", num)
        item_count = self.tree.get_children()
        # print(item_count)
        rnum = random.randint(0, 5)
        print(rnum)

        i = 0
        for i in range(rnum, 10):
            # update 1 row in treeview
            self.tree.item(item_count[num], values=(num, i, "run"))
            # # update 1 cell in treeview
            # # self.tree.set(selected_item, column=2, value="your value")
            time.sleep(1)
            if self.stop_thread == 1:
                break
        self.tree.item(item_count[num], values=(num, i, "stop"))

    def stop_threading(self):
        self.stop_thread = 1
        print(self.stop_thread)


if __name__ == "__main__":
    app = Window()
    app.mainloop()

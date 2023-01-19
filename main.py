# ****************tkinter GUI **********************************
from tkinter import Tk
from tkinter.ttk import Button, Label, Style


class Window(Tk):
    def __init__(self):
        super().__init__()
        self.wm_title("form")
        self.geometry("400x300")

        s = Style()
        s.configure('2.TButton', font=('arial', 25))
        exit_button = Button(self,
                             text="change text",
                             style="2.TButton",
                             command=self.receive)
        exit_button.place(x=50, y=200, width=230, height=50)

        # show a label
        self.label = Label(self,
                           text='This is a label',
                           font=('arial', 30, 'bold'))
        self.label.place(x=50, y=50)

    def receive(self):
        self.label.configure(text="hello")
        # self.destroy()


if __name__ == "__main__":
    app = Window()
    app.mainloop()

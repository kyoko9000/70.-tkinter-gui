from tkinter import Tk, Toplevel
from tkinter.ttk import Button, Label


class Window_1(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('300x200')
        self.title('Toplevel Window')

        self.label = Label(self, text="hi")
        self.label.pack(expand=True)

        self.button = Button(self,
                             text='Open a window',
                             command=self.main_control)
        self.button.place(x=50, y=150)

        self.button_1 = Button(self,
                               text='Open a window',
                               command=self.main_control)
        self.button_1.place(x=50, y=150)

    def main_control(self):
        self.label.config(text="lam choi")


class Window(Tk):
    def __init__(self):
        super().__init__()
        self.window_1 = None
        self.wm_title("form")
        self.geometry("320x200")

        self.label = Label(self, text="hi")
        self.label.pack(expand=True)

        # place a button on the root window
        self.button = Button(self,
                             text='Open a window',
                             command=self.open_window)
        self.button.place(x=50, y=150)

        # place a button on the root window
        button_1 = Button(self,
                          text='set text',
                          command=self.set_text)
        button_1.place(x=200, y=150)

    def set_text(self):
        self.label.config(text="main control")
        self.window_1.label.config(text="main control")

    def open_window(self):
        self.window_1 = Window_1(self)
        # self.window.grab_set()
        self.window_1.button_1.configure(command=self.hh)

    def hh(self):
        self.label.config(text="sub control")
        self.window_1.label.config(text="sub control")


if __name__ == "__main__":
    app = Window()
    app.mainloop()
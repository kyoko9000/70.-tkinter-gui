from tkinter import Tk, Toplevel
from tkinter.ttk import Label, Button


class Window(Tk):
    def __init__(self):
        super().__init__()
        self.window_1 = None
        self.wm_title("main")
        self.geometry("320x200")

        self.label = Label(self, text="hi")
        self.label.pack(expand=True)

        # place a button on the root window
        self.button = Button(self, text='Open a window', command=self.open_window)
        self.button.place(x=50, y=150)

        # place a button on the root window
        button_1 = Button(self, text='main_control', command=self.main_control)
        button_1.place(x=200, y=150)

    def open_window(self):
        self.window_1 = Window_1()
        # self.window_1.grab_set()
        self.window_1.button.configure(command=self.sub_control)

    def main_control(self):
        self.label.config(text="main control")
        self.window_1.label.config(text="main control")

    def sub_control(self):
        self.label.config(text="sub control")
        self.window_1.label.config(text="sub control")


class Window_1(Toplevel):
    def __init__(self):
        super().__init__()
        self.geometry('300x200')
        self.title('sub Window')

        self.label = Label(self, text=" phu ")
        self.label.pack(expand=True)

        self.button = Button(self, text='sub control')
        self.button.place(x=50, y=150)

        self.button_1 = Button(self, text='sub text', command=self.sub_text)
        self.button_1.place(x=150, y=150)

    def sub_text(self):
        self.label.config(text="lam choi")


if __name__ == "__main__":
    app = Window()
    app.mainloop()
from tkinter import Tk


class Window(Tk):
    def __init__(self):
        super().__init__()
        self.wm_title("form")
        self.geometry("320x200")


if __name__ == "__main__":
    app = Window()
    app.mainloop()
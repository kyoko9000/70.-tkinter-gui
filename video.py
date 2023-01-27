# ****************tkinter GUI **********************************
from tkinter import Tk, Label
from tkinter.ttk import Button, Style
from tkvideo import tkvideo


class Window(Tk):
    def __init__(self):
        super().__init__()
        self.wm_title("form")
        self.geometry("550x420")

        # style = Style()
        # style.configure('2.TButton', font=('arial', 30))
        exit_button = Button(self,
                             text="play video",
                             # style="2.TButton",
                             command=self.receive)
        exit_button.place(x=130, y=350, width=230, height=50)

        # show a label
        self.label = Label(self,
                           text='This is a label',
                           font=('arial', 30, 'bold'),
                           )
        # self.label.place(x=80, y=10)
        self.label.pack()

    def receive(self):
        player = tkvideo("video.mp4", self.label, loop=1, size=(400, 300))
        player.play()


if __name__ == "__main__":
    app = Window()
    app.mainloop()

# ****************tkinter GUI **********************************
from tkinter import Tk
from tkinter.ttk import Button, Style, Label

import numpy as np
from matplotlib.backends.backend_tkagg import \
    FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure


class Window(Tk):
    def __init__(self):
        super().__init__()
        self.wm_title("form")
        self.geometry("600x500")

        style = Style()
        style.configure('2.TButton', font=('arial', 25))
        button = Button(self,
                        text="change text",
                        style="2.TButton",
                        command=self.plot)
        button.place(x=100, y=400, width=230, height=50)

        # show a label
        self.label = Label(self,
                           text='This is a label',
                           font=('arial', 30, 'bold'))
        self.label.place(x=20, y=20, width=500, height=350)

    def plot(self):
        # the figure that will contain the plot
        fig = Figure(figsize=(5, 5), dpi=100)

        # adding the subplot
        plt = fig.add_subplot(111)

        # list of squares
        y = np.array([5, 10, 7])
        x = np.array([5, 20, 30])

        # plotting the graph
        plt.plot(x, y)

        # creating the Tkinter canvas
        # containing the Matplotlib figure
        canvas = FigureCanvasTkAgg(fig, self.label)
        canvas.draw()

        # creating the Matplotlib toolbar
        toolbar = NavigationToolbar2Tk(canvas, self.label)
        toolbar.update()

        # placing the toolbar on the Tkinter window
        canvas.get_tk_widget().pack()


if __name__ == "__main__":
    app = Window()
    app.mainloop()

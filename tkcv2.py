from tkinter import Tk
from tkinter.ttk import Label, Button
import cv2
from PIL import ImageTk, Image


class Window(Tk):
    def __init__(self):
        super().__init__()
        self.wm_title("form")
        self.geometry("550x420")

        button_1 = Button(self,
                          text="show tabel",
                          command=self.show_frames)
        button_1.place(x=50, y=350, width=100, height=50)

        # show a label
        self.label = Label(self,
                           text='This is a label',
                           font=('arial', 30, 'bold'))
        self.label.place(x=80, y=20)
        # ===================== cv2  =======================
        self.cap = cv2.VideoCapture("video.mp4")

    def show_frames(self):
        # resize image
        print('Original Dimensions : ', self.cap.read()[1].shape)
        scale_percent = 30  # percent of original size
        width = int(self.cap.read()[1].shape[1] * scale_percent / 100)
        height = int(self.cap.read()[1].shape[0] * scale_percent / 100)
        dim = (width, height)
        # resize image
        resized = cv2.resize(self.cap.read()[1], dim, interpolation=cv2.INTER_AREA)
        print('Resized Dimensions : ', resized.shape)

        # Get the latest frame and convert into Image
        cv2image = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(cv2image)

        # Convert image to PhotoImage
        imgtk = ImageTk.PhotoImage(image=img)
        self.label.imgtk = imgtk
        self.label.configure(image=imgtk)

        # Repeat after an interval to capture continiously
        self.label.after(20, self.show_frames)


if __name__ == "__main__":
    app = Window()
    app.mainloop()
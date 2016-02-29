import Controls
import Model
from Enums import CanvasEnum
from Tkinter import *
from PIL import Image, ImageTk
from tkFileDialog import askopenfilename


class CrimeSceneInvestigator:
    def __init__(self, master, data):
        self.master = master
        master.title("Crime Scene Investigator")
        self.image1 = Image.open('assets/angle_pic.jpg').resize((640, 400))
        self.image2 = Image.open('assets/top_pic.jpg').resize((640, 400))
        self.data = data
        self.initUI()

    def initUI(self):
        self.canvas1 = Canvas(root, width=640, height=400)
        self.canvas2 = Canvas(root, width=640, height=400)

        # we need to keep the reference (bug  in Tkinter: GC deletes picture)
        self.tk_img1 = ImageTk.PhotoImage(self.image1)
        self.tk_img2 = ImageTk.PhotoImage(self.image2)

        self.initCanvas(self.canvas1, self.tk_img1, 0, self.click)
        self.initCanvas(self.canvas2, self.tk_img2, 1, self.click2)

        self.reset_button = Button(root, text="Reset",
                                   command=self.reset)
        self.reset_button.grid(row=0, column=0, sticky=E)

        self.open_button1 = Button(root, text="Open first picture", width=40,
                                   command=self.open1)
        self.open_button1.grid(row=0, column=0, sticky=W)

        self.open_button2 = Button(root, text="Open second picture", width=40,
                                   command=self.open2)
        self.open_button2.grid(row=0, column=1, sticky=W)

        self.label = Label(root, text="Choose 4-4 points!")
        self.label.grid(row=0, column=1, sticky=E)

    def initCanvas(self, canvas, img, position, function):
        canvas.create_image(0, 0, anchor=NW, image=img)
        canvas.image = img  # keeping the reference preventing GC
        canvas.configure(cursor="crosshair")
        canvas.grid(row=1, column=position, sticky=E)
        canvas.bind("<Button-1>", function)

    def click(self, event):
        Controls.click(event, self.canvas1, self.canvas2, self.data)

    def click2(self, event):
        Controls.click2(event, self.canvas2, self.data)

    def reset(self, enum=CanvasEnum.All):
        self.data = Model.Data()

        if enum in (CanvasEnum.Canvas1, CanvasEnum.All):
            self.canvas1.delete(ALL)
            self.tk_img1 = ImageTk.PhotoImage(self.image1)
            self.canvas1.create_image(0, 0, anchor=NW, image=self.tk_img1)

        if enum in (CanvasEnum.Canvas2, CanvasEnum.All):
            self.canvas2.delete(ALL)
            self.tk_img2 = ImageTk.PhotoImage(self.image2)
            self.canvas2.create_image(0, 0, anchor=NW, image=self.tk_img2)

    def open1(self):
        self.image1 = Image.open(askopenfilename()).resize((640, 400))
        self.tk_img1 = ImageTk.PhotoImage(self.image1)
        self.reset(CanvasEnum.Canvas1)
        self.initCanvas(self.canvas1, self.tk_img1, 0, self.click)

    def open2(self):
        self.image2 = Image.open(askopenfilename()).resize((640, 400))
        self.tk_img2 = ImageTk.PhotoImage(self.image2)
        self.reset(CanvasEnum.Canvas2)
        self.initCanvas(self.canvas2, self.tk_img2, 1, self.click2)


if __name__ == "__main__":
    root = Tk()
    data = Model.Data()
    gui = CrimeSceneInvestigator(root, data)
    root.mainloop()

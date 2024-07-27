from tkinter import *
from tkinter.colorchooser import askcolor
import ctypes

class Paint(object):

    DEFAULT_PEN_SIZE = 5.0
    DEFAULT_COLOUR = 'red'

    def __init__(self):
        self.root = Tk()
        self.root.title("мое приложение")

        self.pen_button = Button(self.root, text='карандаш', command=self.use_pen)
        self.pen_button.grid(row=0, column=0)

        #цвет кнопки
        self.colour_button = Button(self.root, text='цвет', command=self.choose_colour)
        self.colour_button.grid(row=0, column=1)

        #кнопка стирания
        self.eraser_button = Button(self.root, text='ластик', command=self.use_eraser)
        self.eraser_button.grid(row=0, column=2)

        #шкала из 10 возможных чтобы выбрать ширину карандашной линии
        self.choose_size_button = Scale(self.root, from_=1, to=10, orient=HORIZONTAL)
        self.choose_size_button.grid(row=0, column=3)

        user32 = ctypes.windll.user32
        monitor_width = user32.GetSystemMetrics(0)
        monitor_height = user32.GetSystemMetrics(1)

        self.c = Canvas(self.root, bg='white', width=monitor_width, height=monitor_height)
        self.c.grid(row=1, columnspan=4)

        self.setup()

        self.root.mainloop()


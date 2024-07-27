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

    def setup(self):
        self.old_x = None
        self.old_y = None
        self.line_width = self.choose_size_button.get()
        self.colour = self.DEFAULT_COLOUR
        self.eraser_on = False
        self.active_button = self.pen_button
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<B3-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)

#функция использования ручки
    def use_pen(self):
        self.activateButton(self.pen_button)
#функция использования цвета
    def choose_colour(self):
        self.eraser_on = False
        self.colour = askcolor(color=self.colour)[1]
# функция использования ластика
    def use_eraser(self):
        self.activateButton(self.eraser_button, eraser_mode=True)
#При нажатии на кнопку она будет поднята
    def activateButton(self, some_button, eraser_mode=False):
        self.active_button.config(relief=RAISED)
        some_button.config(relief=SUNKEN)
        self.active_button = some_button
        self.eraser_on = eraser_mode

#!/usr/bin/python3
# 使用Python内置GUI模块tkinter
import tkinter
from tkinter import *
from tkinter.tix import Tk

from PIL import Image, ImageTk

import GO_GAME as Game


class wel:

    def __init__(self):
        self.window = Tk()  # 初始化Tk()

        # 打开指定的图片文件
        def get_image(filename, width, height):
            im = Image.open(filename).resize((width, height))
            return ImageTk.PhotoImage(im)

        self.window.title("The Game of GO     Updated by Yuhan Liu")  # 设置窗口标题
        self.window.geometry("1197x900")  # 设置窗口大小 注意：是x 不是*
        self.window.resizable(width=False, height=False)  # 设置窗口是否可以变化长/宽，False不可变，True可变，默认为True

        # 创建画布，设置要显示的图片，把画布添加至应用程序窗口
        canvas_window = tkinter.Canvas(self.window, width=1197, height=900)
        im_window = get_image('./Pictures/Background.png', 1197, 900)
        canvas_window.create_image(597.5, 450, image=im_window)
        canvas_window.pack()

        # 设置字体格式
        FONT = ("Freestyle Script", 25)
        button1 = Button(self.window, text='S T A R T', font=FONT, height=1, width=10, command=self.welstart,
                         activeforeground="black", activebackground='white', bg='black', fg='white')
        button2 = Button(self.window, text='Q U I T', font=FONT, height=1, width=10, command=self.quit,
                         activeforeground="black", activebackground='white', bg='black', fg='white')
        button1.place(x=521, y=250)
        button2.place(x=521, y=320)
        self.window.iconbitmap('./GO.ico')
        self.window.mainloop()

    def welstart(self):
        self.window.destroy()
        Game.main01()

    def quit(self):
        quit()
wel()

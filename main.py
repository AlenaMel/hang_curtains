#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, cv2
import cv2.cv as cv
import numpy as np
# from Tkinter.ttk import *
from tkinter.ttk import *
import Tkinter as tk
# import Tkinter.Widget
# from Tkinter.ttk import *
# import Tkinter.ttk as ttk
import ttk
from dialog import *
from PIL import Image, ImageTk
import Image, ImageTk
import curtain

list1 = ["10.jpg", "big", "mosaic1.jpg", "mosaic.jpg"]

x1 = 330  # 150
y1 = 6  # 150
x2 = 498  # 350
y2 = 6  # 150
x3 = 330  # 150
y3 = 238  # 280
x4 = 498  # 350
y4 = 238  # 280
temp_name = ''
current = -1


# класс главного окна
class main:
    def __init__(self, master):
        global var_trans
        self.master = master
        self.master.title('Hang curtains')
        self.master.geometry('800x600+200+150')
        # Bar
        self.fra1 = Frame(self.master, relief=RAISED, bg="Silver", bd=2)
        self.fra1.grid(row=0, column=0, columnspan=20)
        self.lab1 = Label(self.fra1, text='points').grid(row=0, column=0)  # .pack( side=LEFT )
        self.labx1 = Label(self.fra1, text='X').grid(row=1, column=2)
        self.laby1 = Label(self.fra1, text='Y').grid(row=1, column=3)
        self.labx2 = Label(self.fra1, text='X').grid(row=1, column=6)
        self.laby2 = Label(self.fra1, text='Y').grid(row=1, column=7)
        self.lab2 = Label(self.fra1, text='Top left   ').grid(row=2, column=1)
        self.var_x1 = IntVar()
        self.var_x1.set(x1)
        self.sb_x1 = Spinbox(self.fra1, from_=1, to=1000, textvariable=self.var_x1, width=10,
                             command=self.chang_rect).grid(row=2, column=2)
        self.var_y1 = IntVar()
        self.var_y1.set(y1)
        self.sb_y1 = Spinbox(self.fra1, from_=1, to=1000, textvariable=self.var_y1, width=10,
                             command=self.chang_rect).grid(row=2, column=3)
        self.lab3 = Label(self.fra1, text='Top right   ').grid(row=2, column=5)
        self.var_x2 = IntVar()
        self.var_x2.set(x2)
        self.sb_x2 = Spinbox(self.fra1, from_=1, to=1000, textvariable=self.var_x2, width=10,
                             command=self.chang_rect).grid(row=2, column=6)
        self.var_y2 = IntVar()
        self.var_y2.set(y2)
        self.sb_y2 = Spinbox(self.fra1, from_=1, to=1000, textvariable=self.var_y2, width=10,
                             command=self.chang_rect).grid(row=2, column=7)
        self.lab4 = Label(self.fra1, text='Bottom left   ').grid(row=3, column=1)
        self.var_x3 = IntVar()
        self.var_x3.set(x3)
        self.sb_x3 = Spinbox(self.fra1, from_=1, to=1000, textvariable=self.var_x3, width=10,
                             command=self.chang_rect).grid(row=3, column=2)
        self.var_y3 = IntVar()
        self.var_y3.set(y3)
        self.sb_y3 = Spinbox(self.fra1, from_=1, to=1000, textvariable=self.var_y3, width=10,
                             command=self.chang_rect).grid(row=3, column=3)
        self.lab5 = Label(self.fra1, text='Bottom right   ').grid(row=3, column=5)
        self.var_x4 = IntVar()
        self.var_x4.set(x4)
        sb_x4 = Spinbox(self.fra1, from_=1, to=1000, textvariable=self.var_x4, width=10,
                        command=self.chang_rect).grid(row=3, column=6)
        self.var_y4 = IntVar()
        self.var_y4.set(y4)
        self.sb_y4 = Spinbox(self.fra1, from_=1, to=1000, textvariable=self.var_y4, width=10,
                             command=self.chang_rect).grid(row=3, column=7)
        self.lab6 = Label(self.fra1, text='file   ').grid(row=4, column=1)
        self.ent = Entry(self.fra1, width=50, bd=3).grid(row=4, column=2, columnspan=4)
        self.combobox = Combobox(self.fra1, values=list1, height=3, width=15, state='readonly').grid(row=4, column=6)
        # self.combobox.bind('<<ComboboxSelected>>', self.get_selected)
        self.var_temp = IntVar()
        self.var_temp.set(-1)
        self.sb_temp = Spinbox(self.fra1, from_=-1, to=2, textvariable=self.var_temp, width=10,
                               command=self.get_selected).grid(row=4, column=7)
        self.lab7 = Label(self.fra1, text='Scale method').grid(row=5, column=1)
        self.var_scale = IntVar()
        self.var_scale.set(0)
        rad0 = Radiobutton(self.fra1, text="Resize", variable=self.var_scale, value=0).grid(row=5, column=2)
        rad1 = Radiobutton(self.fra1, text="Pyromids", variable=self.var_scale, value=1).grid(row=5, column=3)
        self.lab7 = Label(self.fra1, text='Opening%').grid(row=5, column=5)
        self.var_open = IntVar()
        self.var_open.set(100)
        self.sb_open = Spinbox(self.fra1, from_=1, to=100, textvariable=self.var_open, width=10).grid(row=5, column=6)
        var_trans = IntVar()
        self.check1 = Checkbutton(self.fra1, text='Transparant', variable=var_trans,  # onvalue=1,offvalue=0
                                  command=self.cbt).grid(row=5, column=7)
        # end bar
        self.master.protocol('WM_DELETE_WINDOW',
                             self.exitMethod)
        self.master.mainloop()

    def chang_rect(self):
        global x1, y1, x2, y2, x3, y3, x4, y4, xr, yr
        x1 = self.var_x1.get()
        y1 = self.var_y1.get()
        x2 = self.var_x2.get()
        y2 = self.var_y2.get()
        x3 = self.var_x3.get()
        y3 = self.var_y3.get()
        x4 = self.var_x4.get()
        y4 = self.var_y4.get()

    def get_selected(self):
        global temp_name, current
        # temp_name = self.combobox.get()
        # current = self.combobox.current()
        current = self.var_temp.get()
        if current == -1:
            temp_name = ''
        elif current == 0:
            temp_name = '10.jpg'
        elif current == 1:
            temp_name = 'big.jpg'
        elif current == 2:
            temp_name = 'mosaic.png'

    def cbt(self):
        print "variable is", var_trans.get()

    def openDialog(self):
        self.dialog = dialog(self.master)
        self.sendValue = self.text.get('0.0', END)
        self.returnValue = self.dialog.go(self.sendValue)
        if self.returnValue:
            self.text.delete('0.0', END)
            self.text.insert('0.0', self.returnValue)

    def exitMethod(self):
        self.dialog = yesno(self.master)
        self.myMssg = 'Do you want to exit?'
        self.returnValue = self.dialog.go(message=self.myMssg)
        if self.returnValue:
            self.master.destroy()


# создание окна
root = Tk()
# Set up GUI
# window = tk.Tk()  #Makes main window
# window.wm_title("Digital Microscope")
# window.config(background="#FFFFFF")

# Graphics window
imageFrame = tk.Frame(root, width=600, height=500)
imageFrame.grid(row=8, column=0, padx=10, pady=2)

# Capture frames
lmain = tk.Label(imageFrame)
lmain.grid(row=8, column=0)


def show_frame():
    global x1, y1, x2, y2, x3, y3, x4, y4, img2, current, temp_name, var_trans
    # current = 1
    frame = cv2.imread('373.jpg')
    if current == -1:
        cv2.rectangle(frame, (x1, y1), (x4, y4), (0, 255, 0), 3)
    elif current >= 0:
        imgc = curtain.Curtain(temp_name)
        rows, cols, channels = frame.shape
        roi = np.zeros((rows, cols, channels), dtype=np.uint8)
        h1, w1 = frame.shape[:2]
        if current == 0:
            roir = imgc.fillrec(((y4 - y1), (x4 - x1)))
        elif current == 1:
            roir = imgc.croprec(((y4 - y1), (x4 - x1)))
        elif current == 2:
            roir = imgc.mosaicrec(((y4 - y1), (x4 - x1)))
        cv2.imshow("test-main", roir)
        img2 = np.zeros((h1, w1, channels), np.uint8)
        img2[0:h1, 0:w1, :3] = [255, 255, 255]
        x_offset = x1  # 330
        y_offset = y1  # 5
        img2[y_offset:y_offset + roir.shape[0], x_offset:x_offset + roir.shape[1]] = roir
        if var_trans.get() == 1:
            ###############################################################
            # # version with transparency
            rows, cols, channels = img2.shape
            roi = frame[0:rows, 0:cols]
            img2gray = cv2.cvtColor(img2, cv.CV_BGR2GRAY)
            ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)
            mask_inv = cv2.bitwise_not(mask)
            img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
            img2_fg = cv2.bitwise_and(img2, img2, mask=mask)
            dst = cv2.add(img1_bg, img2_fg)
            frame[0:rows, 0:cols] = dst
            # #########################################################
        else:
            frame[y_offset:y_offset + roir.shape[0], x_offset:x_offset + roir.shape[1]] = roir
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame)


# Slider window (slider controls stage position)
sliderFrame = tk.Frame(root, width=600, height=100)
sliderFrame.grid(row=600, column=0, padx=10, pady=2)

show_frame()  # Display 2
# root.mainloop()  #Starts GUI
# cv2.imshow('res', img2)
# запуск окна
main(root)

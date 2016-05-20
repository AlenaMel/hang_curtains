#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, cv2
import numpy as np
from tkinter.ttk import *
from Tkinter import *
#from myBoolean import *
from dialog import *
from PIL import Image, ImageTk

list1 = ["10.jpg", "big", "mosaic.jpg"]


# класс главного окна
class main:
  def __init__(self, master):
    self.master = master
    self.master.title('Hang curtains')
    self.master.geometry('800x600+200+150')
    # Bar
    self.fra1 = Frame(self.master, relief = RAISED, bg="Silver", bd=2)
    self.fra1.grid(row=0,column=0,columnspan=20)
    self.lab1 = Label( self.fra1, text='points' ).grid(row=0,column=0)# .pack( side=LEFT )
    self.labx1 = Label( self.fra1, text='X' ).grid(row=1,column=2)
    self.laby1 = Label( self.fra1, text='Y' ).grid(row=1,column=3)
    self.labx2 = Label( self.fra1, text='X' ).grid(row=1,column=6)
    self.laby2 = Label( self.fra1, text='Y' ).grid(row=1,column=7)
    self.lab2 = Label( self.fra1, text='Top left   ' ).grid(row=2,column=1)
    var_x1 = StringVar(root)
    var_x1.set(150)
    sb_x1 = Spinbox(self.fra1, from_=1, to=1000, textvariable=var_x1, width=10).grid(row=2,column=2)
    var_y1 = StringVar(root)
    var_y1.set(150)
    sb_y1 = Spinbox(self.fra1, from_=1, to=1000, textvariable=var_y1, width=10).grid(row=2,column=3)
    self.lab3 = Label( self.fra1, text='Top right   ' ).grid(row=2,column=5)
    var_x2 = StringVar(root)
    var_x2.set(350)
    sb_x1 = Spinbox(self.fra1, from_=1, to=1000, textvariable=var_x2, width=10).grid(row=2,column=6)
    var_y2 = StringVar(root)
    var_y2.set(150)
    sb_y1 = Spinbox(self.fra1, from_=1, to=1000, textvariable=var_y2, width=10).grid(row=2,column=7)
    self.lab4 = Label( self.fra1, text='Bottom left   ' ).grid(row=3,column=1)
    var_x3 = StringVar(root)
    var_x3.set(150)
    sb_x1 = Spinbox(self.fra1, from_=1, to=1000, textvariable=var_x3, width=10).grid(row=3,column=2)
    var_y3 = StringVar(root)
    var_y3.set(280)
    sb_y1 = Spinbox(self.fra1, from_=1, to=1000, textvariable=var_y3, width=10).grid(row=3,column=3)
    self.lab5 = Label( self.fra1, text='Bottom right   ' ).grid(row=3,column=5)
    var_x4 = StringVar(root)
    var_x4.set(350)
    sb_x4 = Spinbox(self.fra1, from_=1, to=1000, textvariable=var_x4, width=10).grid(row=3,column=6)
    var_y4 = StringVar(root)
    var_y4.set(280)
    sb_y1 = Spinbox(self.fra1, from_=1, to=1000, textvariable=var_y4, width=10).grid(row=3,column=7)
    self.lab6 = Label( self.fra1, text='file   ' ).grid(row=4,column=1)
    self.ent = Entry( self.fra1, width=50, bd=3 ).grid(row=4,column=2,columnspan=4)
    combobox = Combobox(self.fra1, values=list1, height=3, width=15, state='readonly').grid(row=4,column=6)
    self.lab7 = Label( self.fra1, text='Scale method' ).grid(row=5,column=1)
    var=IntVar()
    var.set(1)
    rad0 = Radiobutton(self.fra1,text="Resize",variable=var,value=0).grid(row=5,column=2)
    rad1 = Radiobutton(self.fra1,text="Pyromids",variable=var,value=1).grid(row=5,column=3)
    self.lab7 = Label( self.fra1, text='Opening%' ).grid(row=5,column=5)
    var_open = StringVar(root)
    var_open.set(100)
    sb_open = Spinbox(self.fra1, from_=1, to=100, textvariable=var_open, width=10).grid(row=5,column=6)
    # end bar
    img = cv2.imread('373.jpg',0)
#   h, w = img.shape[:2]
    image = Image.open("373.jpg")
    photo = ImageTk.PhotoImage(image)
    label = Label(image=photo)
    label.image = photo # keep a reference!
    label.grid(row=8,column=1)
    #photo = PhotoImage(file = "warm_purple-logo.png" ).grid(row=4,column=1)
    #self.ent = Entry( self.fra1, width=50, bd=3 ).grid(row=4,column=2)
    # self.button = Button(self.master,
    #                      text = 'dialog',
    #                      command = self.openDialog)
    # self.button.pack(side = BOTTOM)
    self.master.protocol('WM_DELETE_WINDOW',
                         self.exitMethod)
    self.master.mainloop()

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
    self.returnValue = self.dialog.go(message = self.myMssg)
    if self.returnValue:
      self.master.destroy()


# создание окна
root = Tk()

# запуск окна
main(root)
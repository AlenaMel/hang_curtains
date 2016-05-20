#!/usr/bin/python
# -*- coding: utf-8 -*-

# импортирование модулей python
from Tkinter import *

# класс дочернего окна
class dialog:
  def __init__(self, master):
    self.top = Toplevel(master)
    self.top.title('dialog')
    self.top.geometry('200x100+300+250')
    self.frame = Frame(self.top)
    self.frame.pack(side = BOTTOM)
    self.accept_button = Button(self.frame,
                                text = 'accept',
                                command = self.accept)
    self.accept_button.pack(side = LEFT)
    self.cancel_button = Button(self.frame,
                                text = 'cancel',
                                command = self.cancel)
    self.cancel_button.pack(side = RIGHT)
    self.text = Text(self.top,
                     background = 'white')
    self.text.pack(side = TOP,
                   fill = BOTH,
                   expand = YES)
    self.top.protocol('WM_DELETE_WINDOW', self.cancel)

  def go(self, myText = '',):
    self.text.insert('0.0', myText)
    self.newValue = None
    self.top.grab_set()
    self.top.focus_set()
    self.top.wait_window()
    return self.newValue

  def accept(self):
    self.newValue = self.text.get('0.0', END)
    self.top.destroy()

  def cancel(self):
    self.top.destroy()


# класс диалогового окна выхода
class yesno:
  def __init__(self, master):
    self.slave = Toplevel(master)
    self.frame = Frame(self.slave)
    self.frame.pack(side = BOTTOM)
    self.yes_button = Button(self.frame,
                             text = 'yes',
                             command = self.yes)
    self.yes_button.pack(side = LEFT)
    self.no_button = Button(self.frame,
                            text = 'no',
                            command = self.no)
    self.no_button.pack(side = RIGHT)
    self.label = Label(self.slave)
    self.label.pack(side = TOP,
                    fill = BOTH,
                    expand = YES)
    self.slave.protocol('WM_DELETE_WINDOW', self.no)

  def go(self, title = 'question',
               message = '[question goes here]',
               geometry = '200x70+300+265'):
    self.slave.title(title)
    self.slave.geometry(geometry)
    self.label.configure(text = message)
    self.booleanValue = TRUE
    self.slave.grab_set()
    self.slave.focus_set()
    self.slave.wait_window()
    return self.booleanValue

  def yes(self):
    self.booleanValue = TRUE
    self.slave.destroy()

  def no(self):
    self.booleanValue = FALSE
    self.slave.destroy()

# тестовая команда
if __name__ == '__main__':
  root = Tk()
  root.withdraw()
  myTest = yesno(root)
  if myTest.go(message = 'Is it working?'):
    print 'Yes'
  else:
    print 'No'

# тестовая команда
if __name__ == '__main__':
  root = Tk()
  root.withdraw()
  myTest = dialog(root)
  print myTest.go('Hello World!')

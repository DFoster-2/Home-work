from tkinter import *

def Chalng_1():
  global e
  global root2
  global label3
  global number
  
  multiplayer = int (e.get())
  number = 1
  print (number)
  numberstr = "1"
  for x in range (0,multiplayer):
    number = number*2
    print (number)
    
    numberstr = numberstr + ", "+ str (number)
  label3.config(text = numberstr)

def binaryToDesimal():
  global e3 
  global root4
  global label5
  
  inputt = e3.get()
  lenthinputt = len (inputt) 
  number = 1
  listt = [1]
  for x in range (0,lenthinputt -1 ):
      number = number*2
      listt.append(number)
      print (listt)
  digit = ""
  for x in range (0,lenthinputt):
      digit = digit + inputt[x]
  digitlen = len (digit)
  list2 = []
  for x in range (0,lenthinputt):
      print (inputt[digitlen -x -1 ])
      list2.append(inputt[digitlen -x -1 ])
      print (list2)
  desimaol = 0
  for x in range (0,lenthinputt ):
    digit2 = list2[x]
    if digit2 == "1":
      digit3 = int (listt [x])
      print (type(digit3))
      desimaol =desimaol + digit3
      print (desimaol)
  print (desimaol)
  label5.config(text = str(desimaol))
  
def HowManyDigets():
  global e2
  global root2
  global label4
  
  y = e2.get()
  yint = int(y)
  digit = 1
  digit_value =1
  sum = 1
  while sum <yint:
   digit += 1
   digit_value *= 2
   sum += digit_value
  print (digit)
  label4.config(text = str(digit))
  
def passthough3():
  global root4
  root4.destroy()
  start()
  
def passthough2():
  global root3
  root3.destroy()
  start()
  
def passthough():
  global root2
  root2.destroy()
  start()
  
def binaryToDesimal_setup():
  global root
  global root4
  global e3
  global label5
  
  root.destroy()
  root4 = Tk()
  
  label = Label(root4, text = "Challenge 3",font=('Helvetica bold',20))
  label2 = Label(root4, text = "Enter a binary nummber")
  e3 = Entry(root4, width = 10, borderwidth = 3)
  
  e3.insert(0,"100010")
  
  button1 = Button (root4, text = "Submit", bg = "#D9DDDC",command = binaryToDesimal)
  button2 = Button (root4, text = "Home", bg = "#D9DDDC",command = passthough3)
  
  label.grid(row = 0, column= 0)
  e3.grid (row = 2,column=0)
  button1.grid (row = 3,column= 0)
  label2.grid(row = 1, column= 0)
  button2.grid (row = 0,column= 1)
  
  label5 = Label(root4, text ="" )
  
  label5.grid(row =4,column=0)
  
def HowManyDigets_setup():
  global root
  global root3
  global e2
  global label4
  
  root.destroy()
  root3 = Tk()
  
  label = Label(root3, text = "Challenge 2",font=('Helvetica bold',20))
  label2 = Label(root3, text = "Enter desimal nummber and see\n how many digets it is in binaty")
  e2 = Entry(root3, width = 5, borderwidth = 3)
  
  e2.insert(0,"123")
  
  button1 = Button (root3, text = "Submit", bg = "#D9DDDC",command = HowManyDigets)
  button2 = Button (root3, text = "Home", bg = "#D9DDDC",command = passthough2)
  
  label.grid(row = 0, column= 0)
  e2.grid (row = 2,column=0)
  button1.grid (row = 3,column= 0)
  label2.grid(row = 1, column= 0)
  button2.grid (row = 0,column= 1)
  
  label4 = Label(root3, text ="" )
  
  label4.grid(row =4,column=0)
  
def muterplyers_setup():
  global root
  global e
  global root2
  global label3
  
  root.destroy()
  root2 = Tk()
  
  label = Label(root2, text = "Challenge 1",font=('Helvetica bold',20))
  label2 = Label(root2, text = "How far do you want it to go up to?")
  e = Entry(root2, width = 5, borderwidth = 3)
  
  e.insert(0,"14")
  
  button1 = Button (root2, text = "Submit", bg = "#D9DDDC",command = Chalng_1)
  button2 = Button (root2, text = "Home", bg = "#D9DDDC",command = passthough)
  
  label.grid(row = 0, column= 0)
  e.grid (row = 2,column=0)
  button1.grid (row = 3,column= 0)
  label2.grid(row = 1, column= 0)
  button2.grid (row = 0,column= 1)
  
  label3 = Label(root2, text ="" )
  
  label3.grid(row =4,column=0)
  
def start ():
  global root
  
  root = Tk()
  
  label = Label(root, text = "Home work")
  label.config(font=('Helvetica bold',20))
  label.grid (row =0, column =1)
  
  spaceer = Label(root, text = "..............")
  spaceer2 = Label(root, text = "..............")
  spaceer3 = Label(root, text = "..............")
  
  spaceer.grid (row = 4, column = 0)
  spaceer2.grid (row = 4, column = 1)
  spaceer3.grid (row = 4, column = 2)
  
  Button_c1 = Button (root, text = "Challenge 1", bg = "#D9DDDC",padx = 40, pady = 10,command = muterplyers_setup)
  Button_c2 = Button (root, text = "Challenge 2", bg = "#D9DDDC",padx = 40, pady = 10, command = HowManyDigets_setup)
  Button_c3 = Button (root, text = "Challenge 3", bg = "#D9DDDC",padx = 40, pady = 10, command = binaryToDesimal_setup)
  
  Button_c1.grid(row = 1, column = 0)
  Button_c2.grid(row = 1, column = 1)
  Button_c3.grid(row = 1, column = 2)
  
start()
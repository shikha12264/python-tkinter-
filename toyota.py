from tkinter import *
root = Tk()
v = Canvas(root,bg="black")
#1st outer oval
s = v.create_oval(40,40,220,150,width = 10,outline = "gray67")
#2nd vertical oval
k = v.create_oval(110,50,150,140,width = 10,outline = "gray67")
#3rd horizontal oval
d = v.create_oval(70,40,190,85,width = 10,outline = "gray67")
txt = v.create_text(150,200,font = ("IMPACT",44),fill = "red2",text = "TOYOTA")
v.pack()

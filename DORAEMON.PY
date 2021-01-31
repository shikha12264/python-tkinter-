from tkinter import *
root = Tk()
canvas = Canvas(root,width=250,height=350, bg="black")
# Creating body of doreamon
canvas.create_rectangle(47,190,178,285,outline ="deepskyblue2", fill ="deepskyblue2")
#hands
canvas.create_polygon(178,180,178,215,228,220,178,180,fill ="deepskyblue2")
canvas.create_oval(200,200,228,230,fill ="white")
canvas.create_polygon(50,176,47,215,3,165,50,176, fill ="deepskyblue2")
canvas.create_oval(2,160,30,190,fill="white")
#legs
canvas.create_oval(35,280,101,310,fill ="white")
canvas.create_oval(120,280,190,310,fill ="white")
canvas.create_oval(100,277,120,300,fill ="black", outline = "black")
# Pocket oval
canvas.create_oval(65,200,160,273,fill ="white")
#neck belt
canvas.create_oval(45,165,180,205, outline ="black", fill ="red")
#face
canvas.create_oval(20,40,200,200,fill ="deepskyblue2")
canvas.create_oval(40,70,180,200,fill ="white")

#eye
canvas.create_oval(110,60,80,100,fill ="white")
canvas.create_oval(110,80,100,90,fill ="black")
canvas.create_oval(110,60,140,100,fill="white")
canvas.create_oval(110,80,120,90,fill ="black")
# midline
canvas.create_line(110,90,110,140,width =2)
# moustache
canvas.create_line(105,115,45,108,width =2)
canvas.create_line(105,123,55,123,width =2)
canvas.create_line(105,127,45,135,width =2)
canvas.create_line(115,115,183,108,width =2)
canvas.create_line(115,123,170,123,width =2)
canvas.create_line(115,127,183,135,width =2)
#nose
canvas.create_oval(120,90,100,110,fill ="red")

#smile
canvas.create_arc(65,100,150,170,start =180,extent =180, fill ="red")
#pocket
canvas.create_arc(77,200,145,260,start = 180,extent =180)
#bell
canvas.create_oval(100,200,125,225,fill ="darkgoldenrod1")
#create lines
canvas.create_line(102,210,125,210,width=2)
canvas.create_line(102,213,125,213,width =2)
# inner red oval
canvas.create_oval(110,213,115,223,fill ="red")
canvas.pack()
root.mainloop()
from tkinter import *
root = Tk()
canvas = Canvas(root,width=250,height=350, bg="black")
# Creating body of doreamon
canvas.create_rectangle(47,190,178,285,outline ="deepskyblue2", fill ="deepskyblue2")
#hands
canvas.create_polygon(178,180,178,215,228,220,178,180,fill ="deepskyblue2")
canvas.create_oval(200,200,228,230,fill ="white")
canvas.create_polygon(50,176,47,215,3,165,50,176, fill ="deepskyblue2")
canvas.create_oval(2,160,30,190,fill="white")
#legs
canvas.create_oval(35,280,101,310,fill ="white")
canvas.create_oval(120,280,190,310,fill ="white")
canvas.create_oval(100,277,120,300,fill ="black", outline = "black")
# Pocket oval
canvas.create_oval(65,200,160,273,fill ="white")
#neck belt
canvas.create_oval(45,165,180,205, outline ="black", fill ="red")
#face
canvas.create_oval(20,40,200,200,fill ="deepskyblue2")
canvas.create_oval(40,70,180,200,fill ="white")

#eye
canvas.create_oval(110,60,80,100,fill ="white")
canvas.create_oval(110,80,100,90,fill ="black")
canvas.create_oval(110,60,140,100,fill="white")
canvas.create_oval(110,80,120,90,fill ="black")
# midline
canvas.create_line(110,90,110,140,width =2)
# moustache
canvas.create_line(105,115,45,108,width =2)
canvas.create_line(105,123,55,123,width =2)
canvas.create_line(105,127,45,135,width =2)
canvas.create_line(115,115,183,108,width =2)
canvas.create_line(115,123,170,123,width =2)
canvas.create_line(115,127,183,135,width =2)
#nose
canvas.create_oval(120,90,100,110,fill ="red")

#smile
canvas.create_arc(65,100,150,170,start =180,extent =180, fill ="red")
#pocket
canvas.create_arc(77,200,145,260,start = 180,extent =180)
#bell
canvas.create_oval(100,200,125,225,fill ="darkgoldenrod1")
#create lines
canvas.create_line(102,210,125,210,width=2)
canvas.create_line(102,213,125,213,width =2)
# inner red oval
canvas.create_oval(110,213,115,223,fill ="red")
canvas.pack()
root.mainloop()

from tkinter import *
root = Tk()
root.title("LG logo modification")
canvas = Canvas(root,width =500, height =500,bg="black")
#modification
canvas.create_oval(10,10,100,100,fill ="#c70851")
canvas.create_oval(60,30,50,40,outline = "white",fill ="white")

canvas.create_arc(20,20,100,90,start =60,extent=245,outline="white")

canvas.pack()
root.mainloop()

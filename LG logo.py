from tkinter import *
root = Tk()
root.title("LG logo modification")
canvas = Canvas(root,width =500, height =500,bg="black")
#main circle
canvas.create_oval(100,100,300,300,fill ="#c70851")

canvas.create_line(200,260,200,130,fill="white")
#canvas.create_line(60,85,80,85,fill="white")
canvas.create_arc(120,120,280,280, start =90,extent=270,outline = "white")

#dot
canvas.create_oval(190,180,160,150,fill="white")
canvas.pack()
root.mainloop()

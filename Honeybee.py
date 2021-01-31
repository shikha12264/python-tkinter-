from tkinter import *
tk=Tk()
canvas=Canvas(tk,height="600",width="900",bg="gray")
canvas.pack(fill=BOTH,expand=1)

#1st wing
canvas.create_oval(290,270,450,0,fill="sky blue",width=5) 

#body
canvas.create_oval(200,200,700,450,fill="black") 
#face
canvas.create_oval(100,175,300,375,fill="orange",width=5)

#yellow strips
canvas.create_rectangle(325,250,450,430,fill="orange")
canvas.create_arc(326,450,573,410,start=180,extent=90,fill="orange",outline="orange")
canvas.create_rectangle(525,250,650,400,fill="orange")
canvas.create_arc(403,350,649,443,start=0,extent=-90,fill="orange",outline="orange")

#2nd wing
canvas.create_oval(315,150,660,300,fill="sky blue",width=5) 

#tip
canvas.create_polygon(690,300,690,350,730,325,fill="black")

#eyes
canvas.create_oval(125,220,155,270,fill="black")
canvas.create_oval(175,225,215,275,fill="black")
canvas.create_oval(135,225,150,240,fill="white")
canvas.create_oval(188,230,208,250,fill="white")

#mouth
canvas.create_arc(111,300,250,350,start=0,extent=-190,fill="black")
canvas.create_polygon(220,330,251,330,260,310,fill="black")
canvas.create_line(200,330,275,310,220,330,fill="black",smooth="true",width=5)

#strings
canvas.create_line(245,215,210,105,170,140,width=7,smooth="true")
canvas.create_line(155,190,120,140,105,170,width=7,smooth="true")

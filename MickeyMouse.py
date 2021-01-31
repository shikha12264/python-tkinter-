from tkinter import *
tk=Tk()
canvas=Canvas(tk,height="600",width="900",bg="gray")
canvas.pack(fill=BOTH,expand=1)

#face
canvas.create_oval(225,125,625,525,fill="black")
canvas.create_oval(210,300,300,480,fill="black")
canvas.create_oval(550,300,640,480,fill="black")

#cheeks
canvas.create_oval(205,310,400,500,fill="peach puff",outline="black",width=5)
canvas.create_oval(430,310,640,500,fill="peach puff",outline="black",width=5)

#eye region
canvas.create_oval(300,140,440,400,fill="peach puff",outline="peach puff")
canvas.create_oval(410,140,550,400,fill="peach puff",outline="peach puff")

#chin
canvas.create_oval(285,400,560,518,fill="peach puff",outline="peach puff")
canvas.create_oval(320,270,525,540,fill="peach puff",outline="peach puff")

#ears
canvas.create_oval(75,5,325,225,fill="black")
canvas.create_oval(525,5,775,225,fill="black")

#eyes
canvas.create_oval(365,200,415,340,width=5,fill="white")
canvas.create_oval(435,200,485,340,width=5,fill="white")
canvas.create_oval(385,250,415,340,fill="black")
canvas.create_oval(435,250,465,340,fill="black")

#nose
canvas.create_oval(350,310,500,350,fill="peach puff",outline="peach puff")
canvas.create_oval(365,325,485,385,fill="black")

#mouth
canvas.create_arc(350,340,498,530,start=0,extent=-180,fill="black")
canvas.create_arc(345,400,503,455,start=0,extent=-180,fill="peach puff",outline="peach puff")
canvas.create_polygon(467,515,525,420,425,490,fill="black")
canvas.create_polygon(382,515,320,420,425,485,fill="black")
canvas.create_line(328,428,300,410,275,380,width=5,smooth="true")
canvas.create_line(513,430,525,430,570,380,width=5,smooth="true")
canvas.create_line(255,410,275,376,300,370,width=5,smooth="true")
canvas.create_line(550,370,570,378,590,410,width=5,smooth="true")

#tongue
canvas.create_arc(385,475,470,530,fill="red",start=0,extent=-180)
canvas.create_oval(378,475,440,525,fill="red",outline="red")
canvas.create_oval(420,475,475,520,fill="red",outline="red")

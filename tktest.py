from tkinter import *
from time import *
root=Tk()
root.title('tk test')
c=Canvas(root, height=500, width=500)
c.pack()
ball=c.create_oval(238, 238, 262, 262, fill='blue', outline='blue')
def key(event):
    keypressed=event.keysym
    if keypressed == 's':
        root.destroy()
def move(event):
    x, y=event.x, event.y
    c.coords(ball, x-12, y-12, x+12, y+12)
root.bind('<Motion>', move)
root.bind('<Key>', key)
root.mainloop()

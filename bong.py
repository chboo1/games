from tkinter import *
from random import randint
fenetre=Tk()
fenetre.title('Bong')
c=Canvas(fenetre, width=500, height=500)
c.pack()
def motion(event):
    x, y = event.x, event.y
    firstx=x-50
    secondx=x+50
    c.coords(rect, firstx, 450, secondx, 462)
degre90=(10, 0)
degre270=(-10, 0)
degre0=(0, -10)
degre180=(0, 10)
degre45=(5, -5)
degre135=(5, 5)
degre225=(-5, 5)
degre315=(-5, -5)
mouvd= {
    'dir': randint(1, 8)
}
def bouger_balle(mouvd):
    mouv = mouvd['dir']
    try:
        if mouv == 1:
            c.move(balle, 5, -5)
        elif mouv == 2:
            c.move(balle, 5, -5)
        elif mouv == 3:
            c.move(balle, 5, 5)
        elif mouv == 4:
            c.move(balle, 5, 5)
        elif mouv == 5:
            c.move(balle, -5, 5)
        elif mouv == 6:
            c.move(balle, -5, 5)
        elif mouv == 7:
            c.move(balle, -5, -5)
        elif mouv == 8:
            c.move(balle, -5, -5)
        else:
            raise ValueError
        if c.coords(balle)[0] == 0 or c.coords(balle)[1] == 0 or c.coords(balle)[2] == 500 or c.coords(balle)[3] == 500:
            if mouv == 1 or mouv == 5:
                mouv=(mouv+3) if mouv == 1 else (mouv-3)
            elif mouv == 2:
                mouv=8
            elif mouv < 7:
                mouv=mouv-2
            elif mouv == 8 or mouv == 7:
                mouv=mouv-2
            else:
                mouv=mouv+2
            mouvd['dir'] = mouv
    except ValueError:
        print('', end='')
    fenetre.after(50, lambda: bouger_balle(mouvd))

balle=c.create_oval(200, 300, 300, 400, fill='blue', outline='blue')
rect=c.create_rectangle(200, 450, 300, 462, fill='black')
#bouger_balle(mouvd)
fenetre.after(0, lambda: bouger_balle(mouvd))
fenetre.bind('<Motion>', motion)
fenetre.mainloop()

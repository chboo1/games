from tkinter import Canvas, Tk
from random import randint
from enum import Enum
from time import time
import pathlib


class Direction(Enum):
    HAUT_DROITE = 1
    HAUT_GAUCHE = 2
    BAS_GAUCHE = 4
    BAS_DROITE = 3

    def droite(self):
        return self is Direction.HAUT_DROITE or self is Direction.BAS_DROITE

    def gauche(self):
        return self is Direction.HAUT_GAUCHE or self is Direction.BAS_GAUCHE

    def haut(self):
        return self is Direction.HAUT_DROITE or self is Direction.HAUT_GAUCHE

    def bas(self):
        return self is Direction.BAS_DROITE or self is Direction.BAS_GAUCHE


class Mur(Enum):
    DROITE = 1
    BAS = -2
    GAUCHE = -1
    HAUT = 2
    PLAT = -2


class Bong():

    def __init__(self, width, height):
        # begin
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.title('Bong')
        self.c = Canvas(self.root, width=width, height=height)
        self.balle = self.c.create_oval(200, 300, 300, 400,
                                        fill='blue', outline='blue')
        self.root.after(1000, self.pt)
        self.rect = self.c.create_rectangle(200, 450, 300, 462, fill='black')
        self.root.bind('<Motion>', self.motion)
        self.root.bind('<Return>', self.kr)
        self.dir = Direction(randint(1, 4))
        self.mouv = self.dir
        self.c.pack()
        self.start = time()
        self.coin = self.c.create_oval(10, 5, 20, 25,
                                       fill='yellow', outline='yellow')
        self.coin2 = self.c.create_oval(14, 9, 16, 21,
                                         fill='white', outline='white')
        self.coin3 = self.c.create_oval(9, 4, 21, 26)
# end

    def motion(self, event):
        # begin
        self.x, self.y = event.x, event.y
        firstx = self.x-50
        secondx = self.x+50
        self.c.coords(self.rect, firstx, 450, secondx, 462)

    def pt(self):
        print(int(time())-int(self.start))
        self.root.after(1000, self.pt)
        # end

# degre90=(10, 0)
# degre270=(-10, 0)
# degre0=(0, -10)
# degre180=(0, 10)
# degre45=(5, -5)
# degre135=(5, 5)
# degre225=(-5, 5)
# degre315=(-5, -5)
    def kr(self, event):
        # b
        self.start = time()
        self.root.destroy()
        # e

    def quel_mur(self, coords):
        # b
        self.coords = coords
        if self.coords[0] == 0.0:
            return Mur.GAUCHE
        elif self.coords[1] == 0.0:
            return Mur.HAUT
        elif self.coords[2] == self.width:
            return Mur.DROITE
        elif self.coords[3] == self.height:
            return Mur.BAS
        elif self.coords[0]+50 in [self.x-13, self.x-12, self.x-11,
                                    self.x-10, self.x-9, self.x-8, self.x-7, self.x-6, self.x-5, self.x-4, self.x-3, self.x-2, self.x-1, self.x,
                                     self.x+13] and self.coords[3] == 462:
            print('...')
            return Mur.PLAT
        # e

    def bouger_balle(self):
        # b
        print(self.x-13, self.x+13)
        mouv_x = 5 if self.mouv.droite() else -5
        mouv_y = -5 if self.mouv.haut() else 5
        self.c.move(self.balle, mouv_x, mouv_y)

        coords = self.c.coords(self.balle)
        mur = self.quel_mur(coords)
        if mur:
            self.mouv = Direction(self.mouv.value + mur.value)
        if not mur == Mur.BAS:
            self.root.after(50, self.bouger_balle)
        else:
            self.root.destroy()
            print(range(self.x-13, self.x+13))
            print(coords)
# e
    def main(self):

        # b
        self.root.after(2000, self.bouger_balle)
        self.root.mainloop()
        # e


jeu = Bong(500, 500)
jeu.main()


def checkfile(file_path):
    # b
    ret = True
    pl = pathlib.Path(file_path)
    ret = pl.exists()
    if not ret:
        return True
    # e

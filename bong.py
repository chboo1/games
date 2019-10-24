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
    BAS = 0
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
        self.platform_x = (200, 300)
        self.platform_y = (450, 462)
        self.rect = self.c.create_rectangle(self.platform_x[0],
                                            self.platform_y[0],
                                            self.platform_x[1],
                                            self.platform_y[1],
                                            fill='black')
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

    def motion(self, event):
        # begin
        self.x, self.y = event.x, event.y
        firstx = self.x-50
        secondx = self.x+50
        self.platform_x = (firstx, secondx)
        self.c.coords(self.rect,
                      firstx, self.platform_y[0],
                      secondx, self.platform_y[1])
        self.liste_bin = []
# end

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

    def touche_platforme(self, coords):
        x1, y1, x2, y2 = map(int, coords)
        if y2 < self.platform_y[0]:
            return False

        milieu = (x1 + x2) / 2
        if milieu < self.platform_x[0] or milieu > self.platform_x[1]:
            return False

        return True

    def quel_mur(self, coords):
        # b
        self.coords = coords
        if self.coords[0] <= 0.0:
            return Mur.GAUCHE
        elif self.coords[1] <= 0.0:
            return Mur.HAUT
        elif self.coords[2] >= self.width:
            return Mur.DROITE
        elif self.coords[3] >= self.height:
            return Mur.BAS
        elif self.touche_platforme(coords):
            return Mur.PLAT
        # e

    def bouger_balle(self):
        # b
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

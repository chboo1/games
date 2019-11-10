from tkinter import Canvas, Tk, Button
from random import randint
from enum import Enum
from time import time, sleep


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


def start():
    jeu.main(800, 500)


class Bong():

    def __init__(self, width, height):
        # begin
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.title('Bong')
        self.c = Canvas(self.root, width=width, height=height)
        self.root.bind('<Return>', self.kr)
        self.root.bind('<space>', self.space)
        self.dir = Direction(randint(1, 4))
        self.mouv = self.dir
        self.c.pack()
        self.start = time()
        self.freeze = None
        self.but = Button(self.root, text='PLAY', command=self.main)
        self.but.pack()
        self.but2 = None
        self.root.mainloop()
        # end

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

    def space(self, event):
        self.freeze = True
        self.root.unbind('<space>')
        sleep(0.1)
        self.root.bind('<space>', self.unspace)
        self.c.itemconfig(self.txt, text='Paused.')
        self.but2 = Button(self.root, text='Quit', command=self.kr)
        self.but2.pack()

    def unspace(self, event):
        self.freeze = False
        self.root.after(0, self.bouger_balle)
        self.root.unbind('<space>')
        sleep(0.1)
        self.root.bind('<space>', self.space)
        self.c.itemconfig(self.txt, text='Space to pause.')
        self.but2.destroy()

    def kr(self, event=None):
        # b
        self.start = time()
        self.root.destroy()
        # e

    def touche_platforme(self, coords):
        x1, y1, x2, y2 = map(int, coords)
        if y2 < self.platform_y[0] or y2 > self.platform_y[1]:
            return False

        milieu = (x1 + x2) / 2
        if milieu < self.platform_x[0] or milieu > self.platform_x[1]:
            return False

        return True

    def quel_mur(self, coords):
        # b
        self.coords = coords
        if self.coords[1] <= 0.0 and self.coords[2] >= self.width:
            return [Mur.HAUT, Mur.DROITE]
        elif self.coords[1] <= 0.0 and self.coords[0] <= 0.0:
            return [Mur.HAUT, Mur.GAUCHE]
        elif self.coords[0] <= 0.0:
            return [Mur.GAUCHE]
        elif self.coords[1] <= 0.0:
            return [Mur.HAUT]
        elif self.coords[2] >= self.width:
            return [Mur.DROITE]
        elif self.coords[3] >= self.height:
            return [Mur.BAS]
        elif self.touche_platforme(coords):
            return [Mur.PLAT]
        # e

    def bouger_balle(self):
        # b
        if not self.freeze:
            try:
                mouv_x = 5 if self.mouv.droite() else -5
                mouv_y = -5 if self.mouv.haut() else 5
                self.c.move(self.balle, mouv_x, mouv_y)
                coords = self.c.coords(self.balle)
                murs = self.quel_mur(coords)
                if murs:
                    nouv_dir = sum([mur.value for mur in murs])
                    self.mouv = Direction(self.mouv.value + nouv_dir)
                if murs == [Mur.BAS]:
                    raise ZeroDivisionError
                else:
                    self.root.after(10, self.bouger_balle)

            except ValueError:
                self.root.after(10, self.bouger_balle)
            except ZeroDivisionError:
                self.c.delete(self.balle)
                self.c.delete(self.rect)
                self.c.delete(self.txt)
                self.but = Button(self.root, text='PLAY', command=self.main)
                self.but.pack()
# e
    def main(self):

        # b
        self.root.quit()
        self.root.after(2000, self.bouger_balle)
        self.but.destroy()
        self.root.bind('<Motion>', self.motion)
        self.balle = self.c.create_oval((self.width/2)-50, 200, (self.width/2)
                                        + 50, 300,
                                        fill='blue', outline='blue')
        self.platform_x = ((self.width/2)-12, (self.width/2)+13)
        self.platform_y = (450, 462)
        self.txt = self.c.create_text(400, 10,
                        font=('Helvetica', 18), text='Space to pause.')
        self.rect = self.c.create_rectangle(self.platform_x[0],
                                            self.platform_y[0],
                                            self.platform_x[1],
                                            self.platform_y[1],
                                            fill='black')
        self.root.mainloop()
        # e


jeu = Bong(800, 500)

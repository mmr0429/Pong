import pygame
from pygame.math import Vector2
from player import *

class Line(Player):
    def __init__(self,scr,px,res_x,res_y,bnc):
        super().__init__(scr,px,res_x,res_y,bnc) #Call __init__ from Player class
        self.pos=Vector2((399),(0))

    def draw(self):

        self.box=pygame.Rect(self.pos.x, self.pos.y, 3, 600)
        pygame.draw.rect(self.display, (64, 64, 64), self.box) #draw rectangle on given screen

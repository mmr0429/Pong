import pygame
from pygame.math import Vector2
from player import *

class Playerb(Player):

    def __init__(self,scr,px,res_x,res_y,bnc):
        super().__init__(scr,px,res_x,res_y,bnc) #Call __init__ from Player class
        #Overwrite position, so they are next to each other
        self.pos=Vector2((780),(self.ry/2-20))
        self.start_x=780

    #def fix_pos(self):
    #    self.pos.x=(self.rx/8-20)
    #    self.pos=Vector2((self.rx/8-20),(self.ry/2-20))

    def tick(self): #change y position of rectangle
        #Y
        if (self.pos.y <= self.ry) and (self.pos.y >= 0):

            self.vel += (0.7*self.acc)
            self.pos += (0.7*self.vel)
            self.acc *=0
            self.keys=pygame.key.get_pressed() #Get the key pressed dict
            if (self.keys[pygame.K_UP]):
                self.acc.y -= self.mov_pix
            if (self.keys[pygame.K_DOWN]):
                self.acc.y += self.mov_pix


        elif (self.pos.y +40) >= self.ry:
            if self.bounce is 0:
                self.acc.y *=0
                self.vel.y *= 0
                self.pos.y = (self.ry - 40)
            else:

                self.pos.y = (self.ry - 40)
                self.acc.y *=(-0.5)
                self.vel.y *= (-0.5)
                self.pos.y += self.vel.y
                self.acc.y *=0

        elif self.pos.y < 0:
            if self.bounce is 0:
                self.acc.y *=0
                self.vel.y *= 0
                self.pos.y = 0
            else:
                self.pos.y = 0
                self.acc.y *=(-0.5)
                self.vel.y *= (-0.5)
                self.pos.y += self.vel.y
                self.acc.y *=0

    def draw(self):

        self.box=pygame.Rect(self.pos.x, self.pos.y, 10, 40)
        pygame.draw.rect(self.display, (128, 128, 128), self.box) #draw rectangle on given screen

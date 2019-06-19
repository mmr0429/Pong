import pygame
from pygame.math import Vector2

class Player(object):
    def __init__(self,scr,px,res_x,res_y,bnc):
        self.bounce=bnc
        self.rx=res_x
        self.ry=res_y

        self.start_x=10
        self.start_y=self.ry/2-20

        self.display=scr
        self.mov_pix=px

        self.pos=Vector2((10),(self.ry/2-20))
        self.vel=Vector2(0,0)
        self.acc=Vector2(0,0)

    def reset_loc(self):
        self.pos.x=self.start_x
        self.pos.y=self.start_y
        self.vel*=0
        self.acc*=0

    #Changes bouncing option
    def bounce_mode(self,newsetting):
        self.bounce = newsetting

    def tick(self): #change y position of rectangle

        #Y
        if (self.pos.y <= self.ry) and (self.pos.y >= 0):

            self.vel += (0.7*self.acc)
            self.pos += (0.7*self.vel)
            self.acc *=0

            self.keys=pygame.key.get_pressed() #Get the key pressed dict
            if (self.keys[pygame.K_w]):
                self.acc.y -= self.mov_pix
            if (self.keys[pygame.K_s]):
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

    def get_location(self):
        return self.pos

    def draw(self):

        self.box=pygame.Rect(self.pos.x, self.pos.y, 10, 40)
        pygame.draw.rect(self.display, (128, 128, 128), self.box) #draw rectangle on given screen

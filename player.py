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
        #self.box=pygame.Rect(10, 10, 20, 20)
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

    def tick(self): #change x and y position of rectangle
        #X
        #if ((self.pos.x+20) <= self.rx) and (self.pos.x >= 0):
        if 0:

            self.vel += self.acc
            self.pos += self.vel
            self.acc *=0




            self.keys=pygame.key.get_pressed() #Get the key pressed dict
            if (self.keys[pygame.K_d]):
                self.acc.x += self.mov_pix
            if (self.keys[pygame.K_a]):
                self.acc.x -= self.mov_pix


        elif self.pos.x >= self.rx:

            if self.bounce is 0:
                self.acc.x *=0
                self.vel.x *= 0
                self.pos.x = (self.rx - 20)
            else:

                self.pos.x = (self.rx - 20)
                self.acc.x *=(-0.5)
                self.vel.x *= (-0.5)
                self.pos.x += self.vel.x
                self.acc.x *=0



        elif self.pos.x < 0:
            if self.bounce is 0:
                self.acc.x *=0
                self.vel.x *= 0
                self.pos.x = 0
            else:
                self.pos.x = 0
                self.acc.x *=(-0.5)
                self.vel.x *= (-0.5)
                self.pos.x += self.vel.x
                self.acc.x *=0



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

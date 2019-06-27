import pygame
from pygame.math import Vector2
from pygame.math import Vector3
#from playerb import *
from player import *
import random

class Ball(Player):
    def __init__(self,scr,px,res_x,res_y,bnc,cir_x,cir_y):
        super().__init__(scr,px,res_x,res_y,bnc)

        self.ball_speed=4

        self.bounce=0
        self.bounce_fix=1

        self.start_x=cir_x
        self.start_y=cir_y

        self.cx=self.start_x
        self.cy=self.start_y

    def reset_ball(self):
        self.cx=self.start_x
        self.cy=self.start_y
        self.vel*=0
        self.acc*=0

    def tick(self):
        #X
        if ((self.cx+10) <= self.rx) and (self.cx >= 0):

            self.vel += self.acc
            self.cx += self.vel.x
            self.acc *=0

            #self.keys=pygame.key.get_pressed() #Get the key pressed dict
            #if (self.keys[pygame.K_l]):
            #    self.acc.x += self.mov_pix
            #if (self.keys[pygame.K_h]):
            #    self.acc.x -= self.mov_pix

        elif (self.cx+10) >= self.rx:

            if self.bounce is 0:
                self.acc.x *=0
                self.vel.x *= 0
                self.cx = (self.rx - 10)
            else:
                self.cx = (self.rx - 10)
                self.acc.x *=(-1)
                self.vel.x *= (-1)
                self.cx += self.vel.x
                self.acc.x *=0

        elif self.cx < 0:
            if self.bounce is 0:
                self.acc.x *=0
                self.vel.x *= 0
                self.cx = 0
            else:
                self.cx = 0
                self.acc.x *=(-1)
                self.vel.x *= (-1)
                self.cx += self.vel.x
                self.acc.x *=0

        #Y
        if (self.cy <= self.ry) and (self.cy >= 0):

            self.vel += self.acc
            self.cy += self.vel.y
            self.acc *=0

            #self.keys=pygame.key.get_pressed() #Get the key pressed dict
            #if (self.keys[pygame.K_k]):
            #    self.acc.y -= self.mov_pix
            #if (self.keys[pygame.K_j]):
            #    self.acc.y += self.mov_pix

        elif (self.cy +10) >= self.ry:
            if self.bounce_fix is 0:
                self.acc.y *=0
                self.vel.y *= 0
                self.cy = (self.ry - 10)
            else:
                self.cy = (self.ry - 10)
                self.acc.y *=(-1)
                self.vel.y *= (-1)
                self.cy += self.vel.y
                self.acc.y *=0

        elif self.cy < 0:
            if self.bounce_fix is 0:
                self.acc.y *=0
                self.vel.y *= 0
                self.cy = 0
            else:
                self.cy = 0
                self.acc.y *=(-1)
                self.vel.y *= (-1)
                self.cy += self.vel.y
                self.acc.y *=0

    def move_ball(self):
        rand_ball=random.randint(1,4)
        if rand_ball is 1:
            self.acc.x += (self.mov_pix*self.ball_speed)
            self.acc.y += (self.mov_pix*self.ball_speed)
        elif rand_ball is 2:
            self.acc.x += (self.mov_pix*(-self.ball_speed))
            self.acc.y += (self.mov_pix*(-self.ball_speed))
        elif rand_ball is 3:
            self.acc.x += (self.mov_pix*(-self.ball_speed))
            self.acc.y += (self.mov_pix*self.ball_speed)
        elif rand_ball is 4:
            self.acc.x += (self.mov_pix*self.ball_speed)
            self.acc.y += (self.mov_pix*(-self.ball_speed))

    def get_location(self):
        return Vector2(self.cx,self.cy)

    def ball_bounce(self):
        self.cx = self.get_location().x
        self.acc.x *=(-1)
        self.vel.x *= (-1)
        self.cx += self.vel.x
        self.acc.x *=0

        self.cy = self.get_location().y
        self.acc.y *=(-1)
        self.vel.y *= (1)
        self.cy += self.vel.y
        self.acc.y *=0

    def draw(self):
        pygame.draw.circle(self.display, (128, 128, 128), (int(self.cx),int(self.cy)),10)

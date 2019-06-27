import pygame
from pygame.math import Vector2
from player import *

class Playerb(Player):

    def __init__(self,scr,px,res_x,res_y,bnc):
        super().__init__(scr,px,res_x,res_y,bnc) #Call __init__ from Player class

        self.pos=Vector2((780),(self.ry/2-20))
        self.start_x=780
        self.ai=1

    def not_human(self,mode):
        self.ai=mode

    def tick(self,ball_loc): #change y position of rectangle
        ball_location=ball_loc

        if self.ai is 0:
        #Y
            if (self.pos.y <= self.ry) and (self.pos.y >= 0):

                self.vel += self.acc
                self.pos += self.vel
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
        else:
            #AI for player 2
            paddle_pos=self.get_location()

            if (self.pos.y <= self.ry) and (self.pos.y >= 0):

                self.vel += (0.1*self.acc)
                self.pos += (0.1*self.vel)
                self.acc *=0

                if (ball_location.x > 100)and(ball_location.y < paddle_pos.y):
                    self.vel.y -= self.mov_pix
                elif (ball_location.x > 100)and(ball_location.y >= paddle_pos.y):
                    self.vel.y += self.mov_pix
                else:
                    pass

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

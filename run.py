import pygame,sys
from player import *
from playerb import *
from ball import *
from line import *


class Game(object):

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Pong by m')
        self.started=0
        self.p1_score = 0
        self.p2_score = 0
        resx=800
        resy=600
        self.co_op=1

        self.screen = pygame.display.set_mode((resx,resy))
        self.clock = pygame.time.Clock()
        self.delta = 0.0
        self.max_tps = 45.0
        self.mov_pix = 1

        #player
        can_player_spring_back=0 #Bounce off the walls
        self.player=Player(self.screen,self.mov_pix,resx,resy,can_player_spring_back)
        self.player.bounce_mode(1)
        if self.co_op is 1:
            self.player2=Playerb(self.screen,self.mov_pix,resx,resy,can_player_spring_back)
            self.player2.bounce_mode(1)
        self.ball=Ball(self.screen,self.mov_pix,resx,resy,1,400,300)

        self.screen_line=Line(self.screen,self.mov_pix,resx,resy,1)

        #Points
        self.points=0

        while True:

            # event handling
            # When exit is pressed, quitw
            for event in pygame.event.get():
                # When exit is pressed, quit
                if event.type == pygame.QUIT:
                    sys.exit(0)
                # When esc is pressed
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)
#ONLY FOR DEBUGGING---------------------------------------------------------
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    self.player.reset_loc()
                    self.player2.reset_loc()
                    self.ball.reset_ball()

                elif event.type == pygame.KEYDOWN and event.key == pygame.K_b:
                    self.ball.ball_bounce()

                elif event.type == pygame.KEYDOWN and event.key == pygame.K_m:
                    self.ball.move_ball()

            #Ticking
            self.delta += (self.clock.tick() / 1000.0)
            if self.delta > 1 / self.max_tps:
                self.tick()
                self.delta -= 1 / self.max_tps

            #Drawing
            self.screen.fill((0, 0, 0))  # Clears the screen
            self.draw()
            pygame.display.flip()

    def tick(self):

        if self.started is 0:
            self.ball.move_ball()
            self.started=1

        if self.p1_score is 4:
            print("PLAYER 1 WINS !!!!")
            self.p1_score *= 0
            self.p2_score *= 0
            self.player.reset_loc()
            self.player2.reset_loc()
            self.ball.reset_ball()
            self.started=0

        if self.p2_score is 4:
            print("PLAYER 2 WINS !!!!")
            self.p1_score *= 0
            self.p2_score *= 0
            self.player.reset_loc()
            self.player2.reset_loc()
            self.ball.reset_ball()
            self.started=0

        #print(self.ball.get_location().x)
        if (self.ball.get_location().x < 10):
            print("\n\n\n\n\nPLAYER 2 SCORES")
            self.p2_score += 1
            self.player.reset_loc()
            self.player2.reset_loc()
            self.ball.reset_ball()
            self.started=0

        if (self.ball.get_location().x > 791):
            print("\n\n\n\n\nPLAYER 1 SCORES")
            self.p1_score += 1
            self.player.reset_loc()
            self.player2.reset_loc()
            self.ball.reset_ball()
            self.started=0

        if (self.ball.get_location().x is 800):
            self.player.reset_loc()
            self.player2.reset_loc()
            self.ball.reset_ball()

        if ((self.player2.get_location().y <= self.ball.get_location().y)and((self.player2.get_location().y+40) > self.ball.get_location().y))and((self.player2.get_location().x <= self.ball.get_location().x)and((self.player2.get_location().x+10) > self.ball.get_location().x)):
            self.ball.ball_bounce()
        if ((self.player.get_location().y <= self.ball.get_location().y)and((self.player.get_location().y+40) > self.ball.get_location().y))and((self.player.get_location().x <= self.ball.get_location().x)and((self.player.get_location().x+10) > self.ball.get_location().x)):
            self.ball.ball_bounce()

        self.player.tick()
        if self.co_op is 1:
            self.player2.tick()

        self.ball.tick()

    def draw(self):

        self.screen_line.draw()
        self.player.draw()
        if self.co_op is 1:
            self.player2.draw()
        self.ball.draw()

if __name__=="__main__":
    Game()

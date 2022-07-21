import random

class InvalidMove(Exception):pass

class Game:
    def __init__(self): 
        self.colors=('r','g','b','y')
        self.to_guess=[random.choice(self.colors) for i in range(4)] 

    def match_guess(self,guess):
        if len(guess)!=len(self.to_guess) or [g for g in guess if g not in self.colors]:
            raise InvalidMove()
        ret=[0,0] 
        usedindexes=[] 
        for i,g in enumerate(guess):
            if g==self.to_guess[i]:
                ret[0]+=1
                usedindexes.append(i)
        for i,g in enumerate(guess):
            if i in usedindexes: continue
            for j,c in enumerate(self.to_guess):
                if c==g and j not in usedindexes:
                    ret[1]+=1
                    usedindexes.append(j)
        return ret            

class UI:
    def make_move(self): 
    guess=raw_input("Guess: ")
    return guess.split()

def main(self):
    print("The game begins...")
    print("Possible colors (enter first letter): [r]ed [g]reen [b]lue [y]ellow")
    print("Enter your guess like: r g b y")
    g=Game()
    while True:
        guess=self.make_move()
        try:
            bp,wp=g.match_guess(guess)
        except InvalidMove:
            print("Invalid guess, try again")
            continue
        print("Black pegs %s"%bp)
        print("White pegs %s"%wp)
        if bp==4:
            print("You won!")

if __name__=="__main__":
    u=UI()
    u.main()
import pygame
from pygame.locals import *


def draw_current(men, turn, spacing, corner):
    current = len(men) - 1
    pos = corner[0] + current * spacing[0], turn * spacing[1] + corner[1]
    screen.blit(images[men[-1]], pos)

images = { K_r: pygame.image.load('red.png'), K_g: pygame.image.load('green.png'),
           K_b: pygame.image.load('blue.png'), K_y: pygame.image.load('yellow.png'),
           K_SPACE: pygame.image.load('empty.png') }

pygame.init()

SCREEN_SIZE = (640, 480)
background_image_filename = 'mastermind_board.jpg'
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
background = pygame.image.load(background_image_filename).convert()
screen.blit(background, (0, 0))
pygame.display.update()

men = []

margin = 5, 3
spacing = [x + m for m, x in zip(margin, images[K_r].get_size())]
corner = 74, 74
turn = 0
quit = False

while not quit:
    for event in pygame.event.get():
        if event.type == QUIT:
            quit = True
            break
        if event.type == KEYUP:
            if event.key in images:
            #print event.key
                men.append(event.key)
            # update
                draw_current(men,turn, spacing, corner)
                if len(men) == 4:
                    turn += 1
                    men = []
                pygame.display.update()
            elif event.key in (K_q, K_ESCAPE):
                 quit = True
                 break

pygame.quit()
# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
#-------------------------------
#this allows use of modules
from constants import *
from player import Player
#--------------------------------
def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    aclock = pygame.time.Clock()
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    dt = 0

    #start of game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        #limit framerate to 60 FPS
        dt = aclock.tick(60) / 1000


#need to find out what this does in docs
if __name__ == "__main__":
    main()
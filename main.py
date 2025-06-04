# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
#-------------------------------
#this allows use of modules
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
#--------------------------------
def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    aclock = pygame.time.Clock()
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    field = AsteroidField()
    dt = 0

    #start of game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updateable.update(dt)
        for rock in asteroids:
            if rock.collision(player) == True:
                print("Game Over!")
                sys.exit()
        screen.fill("black")
        for drawing in drawable:
            drawing.draw(screen)
        pygame.display.flip()
        #limit framerate to 60 FPS
        dt = aclock.tick(60) / 1000


#need to find out what this does in docs
if __name__ == "__main__":
    main()
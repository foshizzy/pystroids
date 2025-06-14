import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            roid1_v = self.velocity.rotate(random_angle)
            roid2_v = self.velocity.rotate(-random_angle)
            new_rad = self.radius - ASTEROID_MIN_RADIUS
            roid1 = Asteroid(self.position.x, self.position.y, new_rad)
            roid1.velocity = roid1_v * 1.2
            roid2 = Asteroid(self.position.x, self.position.y, new_rad)
            roid2.velocity = roid2_v * 1.2
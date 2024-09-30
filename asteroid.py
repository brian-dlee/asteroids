import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, 2)

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return []

        child_radius = self.radius - ASTEROID_MIN_RADIUS
        random_angle = random.uniform(20, 50)        
        
        a1 = Asteroid(self.position.x, self.position.y, child_radius)
        a1.velocity = self.velocity.rotate(random_angle) * 1.2

        a2 = Asteroid(self.position.x, self.position.y, child_radius)
        a2.velocity = self.velocity.rotate(random_angle * -1) * 1.2

        return [a1, a2]

    def update(self, dt):
        self.position += self.velocity * dt


import abc

import pygame


class CircleShape(abc.ABC, pygame.sprite.Sprite):
    position: pygame.Vector2
    velocity: pygame.Vector2
    radius: float

    def __init__(self, x: float, y: float, radius: float):
        super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    @abc.abstractmethod
    def draw(self, screen: pygame.Surface):
        # sub-classes must override
        pass

    @abc.abstractmethod
    def update(self, dt: float):
        # sub-classes must override
        pass

    def is_colliding(self, other: "CircleShape"):
        distance = self.position.distance_to(other.position)
        combined_radius = other.radius + self.radius
        return distance - combined_radius <= 0

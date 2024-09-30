import pygame

class CircleShape(pygame.sprite.Sprite):
    position: pygame.Vector2
    velocity: pygame.Vector2
    radius: float 

    def __init__(self, x, y, radius):
        super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def is_colliding(self, other: "CircleShape"):
        distance = self.position.distance_to(other.position)
        combined_radius = other.radius + self.radius
        return distance - combined_radius <= 0


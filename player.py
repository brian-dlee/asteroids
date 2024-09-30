import pygame

from circleshape import CircleShape
from constants import (
    PLAYER_RADIUS,
    PLAYER_SHOOT_SPEED,
    PLAYER_SHOT_COOLDOWN,
    PLAYER_SPEED,
    PLAYER_TURN_SPEED,
)
from shot import Shot


class Player(CircleShape):
    default_shot_groups: list[pygame.sprite.Group] = []

    def __init__(self, x: float, y: float):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown = 0

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def move(self, dt: float) -> None:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def rotate(self, dt: float) -> None:
        self.rotation += PLAYER_TURN_SPEED * dt

    def shoot(self) -> None:
        if self.shot_cooldown > 0:
            return

        shot_velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

        shot = Shot(self.position.x, self.position.y)
        shot.velocity = shot_velocity

        for group in self.default_shot_groups:
            group.add(shot)

        self.shot_cooldown = PLAYER_SHOT_COOLDOWN

    def triangle(self) -> tuple[pygame.Vector2, pygame.Vector2, pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5

        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right

        return (a, b, c)

    def update(self, dt: float) -> None:
        self.shot_cooldown -= dt

        keys = pygame.key.get_pressed()

        # left
        if keys[pygame.K_a]:
            self.rotate(dt * -1)

        # up
        if keys[pygame.K_w]:
            self.move(dt)

        # right
        if keys[pygame.K_d]:
            self.rotate(dt)

        # down
        if keys[pygame.K_s]:
            self.move(dt * -1)

        # shoot
        if keys[pygame.K_SPACE]:
            self.shoot()

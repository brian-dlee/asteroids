import pygame
from asteroidfield import AsteroidField
from constants import *
from player import Player

def with_groups(o, *groups):
    for group in groups:
        group.add(o)

    return o


def main():
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    pygame.init()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player = with_groups(Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2), updatable, drawable)
    player.default_shot_groups = [shots, updatable, drawable]

    asteroid_field = with_groups(AsteroidField(), updatable)
    asteroid_field.default_asteroid_groups = [asteroids, updatable, drawable]

    dt = 0
    game_clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill('black')

        for o in updatable:
            o.update(dt)

        for o in asteroids:
            if o.is_colliding(player):
                exit("Game over!")

        for o in drawable:
            o.draw(screen)

        pygame.display.flip()

        dt = game_clock.tick(60) / 1000.0


if __name__ == "__main__":
    main()


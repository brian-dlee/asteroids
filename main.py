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

        for obj in updatable:
            obj.update(dt)

        asteroids_shot = set()
        shots_hit = set()

        for asteroid in asteroids:
            if asteroid.is_colliding(player):
                exit("Game over!")

            for bullet in shots:
                if asteroid.is_colliding(bullet):
                    asteroids_shot.add(asteroid)
                    shots_hit.add(bullet)
                    break

        for asteroid in asteroids_shot:
            asteroid.kill()

        for bullet in shots_hit:
            bullet.kill()

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        dt = game_clock.tick(60) / 1000.0


if __name__ == "__main__":
    main()


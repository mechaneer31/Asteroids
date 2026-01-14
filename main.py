from asteroid import *
from asteroidfield import *
from circleshape import *
from constants import *
from logger import log_event
from logger import log_state
from player import *
import pygame
from shot import *
import sys


def main():
    print("Starting Asteroids with pygame version: " + pygame.version.ver)
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player_x = SCREEN_WIDTH / 2
    player_y = SCREEN_HEIGHT / 2
    player = Player(player_x, player_y)

    asteroid_field = AsteroidField()
    
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for asteroid in asteroids:
            if CircleShape.collides_with(player, asteroid) == True:
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for each_asteroid in asteroids:
            for each_shot in shots:
                if CircleShape.collides_with(each_shot, each_asteroid)  == True:
                    log_event("asteroid_shot")
                    each_asteroid.split()
                    each_shot.kill()

        screen.fill("black")
        for sprite in drawable:        
            sprite.draw(screen)
        pygame.display.flip()
        clock.tick(60)
        dt = clock.get_time() / 1000
        
        


if __name__ == "__main__":
    main()


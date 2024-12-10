# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():
    pygame.init
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    Player.containers = (updateable, drawable)

    player = Player(x, y)
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill((0,0,0))
        
        for object in updateable:
            object.update(dt)

        for object in drawable:
            object.draw(screen)

        pygame.display.flip()

        #framerate = 60
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()
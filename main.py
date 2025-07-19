import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *



def main():
    #Grouping
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable

    #Initialize pygame and window
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
    asteroidObj = AsteroidField()

    #FPS Management
    clock = pygame.time.Clock()
    dt = 0


    #Launch message
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
            
        screen.fill((0, 0, 0))
        for object in drawable:
            object.draw(screen)

        updatable.update(dt)
        pygame.display.flip()
        

        dt = clock.tick(60) / 1000 #Convert ms to seconds
    
    


if __name__ == "__main__":
    main()

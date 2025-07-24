import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS, PLAYER_SHOOT_SPEED

class Shot(CircleShape):
    def __init__(self, position, heading):
        super().__init__(position.x, position.y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 1).rotate(heading) * PLAYER_SHOOT_SPEED

    def draw(self, screen):
        direction = self.velocity.normalize() * 10
        start_pos = self.position
        end_pos = self.position + direction
        pygame.draw.aaline(screen,
                         (255, 255, 255),
                         start_pos,
                         end_pos)
        


    def update(self, dt):
        self.position += self.velocity * dt
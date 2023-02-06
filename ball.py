import pygame


class Ball(pygame.sprite.Sprite):
        """ A moving ball that can change position based on where it's hit by the paddles """
        def __init__(self, x: int, y: int, radius: int):
                """
                x: x position on screen
                y: y position on screen
                radius: radius of circle
                """
                super().__init__()
                self.image = pygame.Surface([50, 50])
                self.rect = self.image.get_rect()
                
                self.color = (255, 0, 0)
                pygame.draw.circle(self.image, self.color, (x, y), radius)
                
                """
                direction
                ---------
                if x and y are both positive: moving towards bottom right
                x is positive but y is negative: moving towards top right
                x is negative and y is negative: moving top left
                x is negative and y is positive: moving bottom left
                """
                self.direction = pygame.math.Vector2(1, 1)
        
        def draw(self, surface: pygame.surface.Surface):
                """ Draws self.image to the surface parameter """
                surface.blit(self.image, (self.rect.x, self.rect.y))
                
        def update(self):
                """ Moves the ball according to self.direction """
                self.rect.x = self.rect.x + self.direction.x
                self.rect.y = self.rect.y + self.direction.y

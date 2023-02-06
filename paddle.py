import pygame


class Paddle(pygame.sprite.Sprite):
        def __init__(self, x: int, y: int):
                """
                x: x position on screen
                y: y position on screen
                """

                super().__init__()
                width = 15
                self.direction = 1
                height = 70
                self.image = pygame.Surface((width, height))
                self.rect = self.image.get_rect()
                
                self.color = (255, 255, 255)
                pygame.draw.rect(self.image, self.color, pygame.Rect(0, 0, width, height), 0, 10)
                
                """
                direction
                ---------
                if x and y are both positive: moving towards bottom right
                x is positive but y is negative: moving towards top right
                x is negative and y is negative: moving top left
                x is negative and y is positive: moving bottom left
                """

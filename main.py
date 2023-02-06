
import sys
import pygame

from paddle import Paddle
from ball import Ball

# Initialize pygame
pygame.init()

font = pygame.font.SysFont(pygame.font.get_default_font(), 50)

# Window dimensions
width = 700
height = 400

# Background color
background_color = (0, 0, 0)

#Creating a display
screen = pygame.display.set_mode((width, height), 0, 32)

# Exit flag for game-loop
running = True

paddle_a = Paddle(0, 0)
paddle_b = Paddle(width - 15, 0)

last_pressed = paddle_a

clock = pygame.time.Clock()
fps = 60
ball = Ball(width // 2, height // 2, 15)


# Start game-loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                paddle_a.direction = -1

            elif event.key == pygame.K_s:
                paddle_a.direction = 1

            if event.key == pygame.K_UP:
                paddle_b.direction = -1

            elif event.key == pygame.K_DOWN:
                paddle_b.direction = 1


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                paddle_a.direction = 0

            elif event.key == pygame.K_s:
                paddle_a.direction = 0

            if event.key == pygame.K_UP:
                paddle_b.direction = 0

            elif event.key == pygame.K_DOWN:
                paddle_b.direction = 0

    # fill the screen
    screen.fill(background_color)

    screen.blit(paddle_a.image, paddle_a.rect)
    screen.blit(paddle_b.image, paddle_b.rect)

    ball.draw(screen)
    ball.update()

    if ball.rect.y +50 > height:
        ball.direction.y = -1
    elif ball.rect.y  <= 0:
        ball.direction.y = 1
    if ball.rect.x + 50 > width:
        paddle_a.score += 1
    elif ball.rect.x <= 0:
        paddle_b.score += 1

    if pygame.Rect.colliderect(ball.rect, paddle_a.rect):
        ball.direction.x = 1
        last_pressed = paddle_a
    elif pygame.Rect.colliderect(ball.rect, paddle_b.rect):
        ball.direction.x = -1
        last_pressed = paddle_b

    paddle_a.update()
    paddle_b.update()

    # Update the display
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
sys.exit()

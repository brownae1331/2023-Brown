import pygame
from pygame.constants import K_LEFT

pygame.init()

clock = pygame.time.Clock()

# set screen size
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")

# Define color
Green = (34, 139, 34)
Red = (255, 0, 0)
Cyan = (0, 255, 255)


def Game():
    # Set Variables
    playerX, playerY = 20, 380
    playerSpeedX = 0
    playerSpeedY = 0

    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            # When key is pressed down
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    playerSpeedX = 5
                elif event.key == pygame.K_LEFT:
                    playerSpeedX = -5
                if event.key == pygame.K_SPACE:
                    playerSpeedY = 3

            # When key is let up
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    playerSpeedX = 0
                if event.key == pygame.KEYUP:
                    playerSpeedY = 0

        playerX += playerSpeedX

        # Backgrpund color
        screen.fill(Cyan)

        # Drawing code
        pygame.draw.rect(screen, Green, [0, 430, 700, 70])
        pygame.draw.rect(screen, Red, [playerX, playerY, 25, 50])
        pygame.display.flip()

        clock.tick(60)


Game()

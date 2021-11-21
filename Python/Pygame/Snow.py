import pygame
import random

# Define some colors
BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
RED = (255,   0,   0)
BLUE = (0, 0, 255)


class Block(pygame.sprite.Sprite):
    """
    This class represents the ball.
    It derives from the "Sprite" class in Pygame.
    """

    def __init__(self, color, width, height):
        """ Constructor. Pass in the color of the block,
        and its size. """

        # Call the parent class (Sprite) constructor
        super().__init__()

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()


class Ball(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()


    # Initialize Pygame
pygame.init()

# Set the height and width of the screen
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])

# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
block_list = pygame.sprite.Group()

# This is a list of every sprite.
# All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()


for i in range(50):
    index = 0
    block = Block(BLACK, 20, 15)

    block.rect.x = (i * 22)
    block.rect.y = 0

    block_list.add(block)
    all_sprites_list.add(block)

for i in range(50):
    index = 0
    block = Block(RED, 20, 15)

    block.rect.x = (i * 22)
    block.rect.y = 20

    block_list.add(block)
    all_sprites_list.add(block)

for i in range(50):
    index = 0
    block = Block(BLUE, 20, 15)

    block.rect.x = (i * 22)
    block.rect.y = 40

    block_list.add(block)
    all_sprites_list.add(block)


padel = Block(BLACK, 50, 15)
all_sprites_list.add(padel)

ball = Ball(RED, 10, 10)
all_sprites_list.add(ball)
ball.rect.x = 200
ball.rect.y = 200

# Create a RED player block

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

score = 0

padelX = 350
padelY = 300
padelSpeed = 0
xBall, yBall = 350, 250
ballSpeed = 1
yoffset, xoffset = 3, 3

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                padelSpeed = 3
            elif event.key == pygame.K_LEFT:
                padelSpeed = -3

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                padelSpeed = 0

    # Clear the screen
    screen.fill(WHITE)

    if padel.rect.x >= 650:
        padelX -= 3
    if padel.rect.x <= 0:
        padelX += 3
    padelX += padelSpeed
    padel.rect.x = padelX
    padel.rect.y = padelY

    yBall -= yoffset * ballSpeed
    xBall -= xoffset * ballSpeed

    if((yBall > playery + 200 or yBall < playery - 10) and xBall < 10):
        xBall, yBall = 350, 250
        player1y, player2y = 175, 175
        ballSpeed = 1

    elif ((yBall > player2y + 200 or yBall < player2y - 10) and xBall > 665):
        xBall, yBall = 350, 250
        player1y, player2y = 175, 175
        ballSpeed = 1

    if xBall <= 10 and xBall > 5 or xBall >= 665 and xBall < 695:
        xoffset = xoffset * -1

    if yBall <= 0 or yBall >= 485:
        yoffset = yoffset * -1

    ball.rect.x = xBall
    ball.rect.y = yBall

    # Draw all the spites
    all_sprites_list.draw(screen)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 60 frames per second
    clock.tick(60)

pygame.quit()

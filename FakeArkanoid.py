
import pygame
import random

# deport indian

# Define some colors
BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
RED = (255,   0,   0)
BLUE = (0, 0, 255)
FUNNY = (69, 42, 69)
CHIMBUS = (80, 0, 80)
PLIMBEY = (145, 141, 12)
BACKGROUND = (23, 255, 247)
PINKY = (230, 41, 173)
# define some variables
x_speed = 0
playerx = 250
xball = 200
yball = 350
colour = RED
answer = ""
speedtimer = 0
xoffset, yoffset = 3, 3
nonraxoffset, nonrayoffset = 3, 3


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
        self.color = color
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()


class Ball(pygame.sprite.Sprite):
    ball_hit_list = []

    def __init__(self, color, width, height, speed):
        super().__init__()
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.speed = speed

        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()

    def powerup(self):
        if self.powerup > 0:
            self.powerup -= 1


class player(pygame.sprite.Sprite):

    def __init__(self, color, width, height,):
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

    def abilities(self, speed):
        self.speed = speed

    def powerup(self, num):
        if num > 0:
            num -= 1
            return 2
        else:
            return 1


#  Initialize Pygame

pygame.init()
# Set the height and width of the screen
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Project Plimble")
pygame.mixer.init()

# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
block_list = pygame.sprite.Group()

# This is a list of every sprite.
# All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()
for i in range(1, 7):
    powerupcolour = random.randint(1, 15)
    if i == 1:
        colour = RED
    elif i == 2:
        colour = BLUE
    elif i == 3:
        colour = BLACK
    elif i == 4:
        colour = FUNNY
    elif i == 5:
        colour = CHIMBUS
    elif i == 6:
        colour = PINKY
    for j in range(15):
        colourblock = colour
        if j == powerupcolour:
            colourblock = PLIMBEY
        # This represents a block
        block = Block(colourblock, 45, 15)

        # Set a random location for the block
        block.rect.x = (j * 47)
        block.rect.y = (i * 20)

        # Add the block to the list of objects

        block_list.add(block)
        all_sprites_list.add(block)
# Create a RED player block
player = player(RED, 50, 15)
player.speed = 1
all_sprites_list.add(player)
# create a ball
ball = Ball(RED, 10, 10, 1)
all_sprites_list.add(ball)
# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

score = 0

# -------- Main Program Loop -----------
while not done:
    if len(block_list) == 0:
        done = True
        answer = "congratulation"
    elif yball == 450:
        done = True
        answer = "you are awful"
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed
            if event.key == pygame.K_LEFT:
                x_speed = -5
            elif event.key == pygame.K_RIGHT:
                x_speed = 5
    # User let up on a key
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                x_speed = 0
        if event.type == pygame.QUIT:
            done = True
    # stop the paddles going off the screen
    if player.rect.x <= 0:
        playerx += 5
    elif player.rect.x >= 670:
        playerx -= 5
    # Clear the screen
    screen.fill(BACKGROUND)

    playerx += (x_speed * player.speed)
    player.rect.x = playerx
    player.rect.y = 300
    xball -= xoffset
    yball -= yoffset
    if xball < 0 or xball >= 685:
        xoffset = xoffset * -1
    if yball < 0 or yball >= 400:
        yoffset = yoffset * -1
    ball.rect.x = xball
    ball.rect.y = yball
    # See if the player block has collided with anything.
    blocks_hit_list = pygame.sprite.spritecollide(ball, block_list, True)
    if ((ball.rect.y > (player.rect.y - 15)) and (ball.rect.y < (player.rect.y + 50))) and ((ball.rect.x > player.rect.x - 15) and (ball.rect.x < player.rect.x + 50)):
        if x_speed == -5:
            xoffset = xoffset * -1
        yoffset = yoffset * -1
        yball -= yoffset + random.randint(1, 3)
    # Check the list of collisions.
    if len(blocks_hit_list) > 0:
        yoffset = yoffset * -1
        if blocks_hit_list[0].color == PLIMBEY:
            player.abilities(player.powerup(200))
            speedtimer = 200
    else:
        speedtimer -= 1
    if speedtimer == 0:
        player.abilities(1)
    for block in blocks_hit_list:
        score += 1
        print(score)

    # Draw all the spites

    all_sprites_list.draw(screen)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 60 frames per second
    clock.tick(60)
print(answer, "没有共产党就没有新中国 没有共产党就没有新中国 共产党辛劳为民族 共产党他一心救中国他指给了人民解放的道路 他领导中国走向光明 他坚持了抗战八年多 他改善了人民生活 他建设了敌后根据地 他实行了民主好处多 没有共产党就没有新中国 没有共产党就没有新中国")
pygame.quit()

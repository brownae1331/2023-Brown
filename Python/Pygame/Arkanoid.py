import pygame
import random

# Define some colors
BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
RED = (255,   0,   0)
BLUE = (0, 0, 255)
GREY = (211, 211, 211)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)


class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()


class PowerUp(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x, y):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def powerUpGravity(self):
        self.rect.x += 1
        self.rect.y += 1


pygame.init()

screenWidth = 700
screenHeight = 400
screen = pygame.display.set_mode([screenWidth, screenHeight])

blockList = pygame.sprite.Group()
allSpritesList = pygame.sprite.Group()

for i in range(6):
    if i == 0:
        color = GREY
    elif i == 1:
        color = RED
    elif i == 2:
        color = YELLOW
    elif i == 3:
        color = CYAN
    elif i == 4:
        color = MAGENTA
    elif i == 5:
        color = GREEN
    y = 17 * i
    for ii in range(15):
        block = Block(color, 45, 15)
        block.rect.x = (ii * 47)
        block.rect.y = y
        blockList.add(block)
        allSpritesList.add(block)

paddle = Block(BLACK, 50, 15)
allSpritesList.add(paddle)

ball = Block(RED, 10, 10)
allSpritesList.add(ball)
ball.rect.x = 200
ball.rect.y = 200

done = False

clock = pygame.time.Clock()

padelX = 350
padelY = 300
padelSpeed = 0
xBall, yBall = 350, 250
ballSpeed = 1
yoffset, xoffset = 3, 3

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                padelSpeed = 5
            elif event.key == pygame.K_LEFT:
                padelSpeed = -5

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                padelSpeed = 0

    screen.fill(BLUE)

    if paddle.rect.x >= 650:
        padelX -= 3
    if paddle.rect.x <= 0:
        padelX += 3
    padelX += padelSpeed
    paddle.rect.x = padelX
    paddle.rect.y = padelY

    yBall -= yoffset * ballSpeed
    xBall -= xoffset * ballSpeed

    # When ball hits walls
    if xBall <= 10 and xBall > 5 or xBall >= 690 and xBall < 695:
        xoffset = xoffset * -1

    if yBall <= 0 or yBall >= 390:
        yoffset *= -1

    ball.rect.x = xBall
    ball.rect.y = yBall

    # When ball hits paddle
    if pygame.sprite.collide_rect(ball, paddle) == True:
        yoffset *= -1

    # When ball hits block
    blockHitList = pygame.sprite.spritecollide(ball, blockList, True)

    powerUpX = ball.rect.x
    powerUpY = ball.rect.y

    for block in blockHitList:
        yoffset *= -1
        rnd = random.randint(1, 10)
        if rnd == 10:
            powerUp = PowerUp(YELLOW, 10, 10, ball.rect.x, ball.rect.y)
            PowerUp.powerUpGravity(powerUp)
            allSpritesList.add(powerUp)

    allSpritesList.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()

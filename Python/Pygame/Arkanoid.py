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


class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def movement(self, powerUp):
        if powerUp == True:
            speed = 7
        else:
            speed = 5
        return speed

    def changeColor(self, color):
        self.image.fill(color)


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

paddle = Paddle(BLACK, 50, 15)
allSpritesList.add(paddle)

ball = Block(RED, 10, 10)
allSpritesList.add(ball)
ball.rect.x = 200
ball.rect.y = 200

done = False

clock = pygame.time.Clock()

paddleSpeed = 0
paddleX, paddleY = 350, 300
xBall, yBall = 350, 250
ballSpeed = 1
yoffset, xoffset = 3, 3
powerUp = False

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                paddleSpeed = Paddle.movement(paddle, powerUp)
            elif event.key == pygame.K_LEFT:
                paddleSpeed = -Paddle.movement(paddle, powerUp)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                paddleSpeed = 0

    if paddle.rect.x >= 650:
        paddleX -= 3
    if paddle.rect.x <= 0:
        paddleX += 3
    paddleX += paddleSpeed

    paddle.rect.x = paddleX
    paddle.rect.y = paddleY

    screen.fill(BLUE)

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
            powerUp = True

    if powerUp == True:
        Paddle.changeColor(paddle, YELLOW)

    allSpritesList.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()

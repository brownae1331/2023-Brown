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


class Player(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def moveLeft(self, powerUp):
        if self.rect.x < 0:
            self.rect.x = 0

        if powerUp == True:
            self.rect.x -= 30
        else:
            self.rect.x -= 5

    def moveRight(self, powerUp):
        if self.rect.x > 430:
            self.rect.x = 430

        if powerUp == True:
            self.rect.x += 30
        else:
            self.rect.x += 5


class Ball(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

        self.velocity = [5, -5]

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]


class PowerUp(pygame.sprite.Sprite):
    def __init__(self, color, width, height, ability):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.ability = ability
        self.count = 0
        self.speedUp = False

    def update(self):
        self.rect.y += 2.5
        if pygame.sprite.collide_rect(self, player) == True or self.rect.y < 0:
            self.kill()


pygame.init()

# Size of screen
screenWidth = 500
screenHeight = 650
screen = pygame.display.set_mode([screenWidth, screenHeight])


# Adding the blocks
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
    for ii in range(10):
        block = Block(color, 48, 15)
        block.rect.x = (ii * 50)
        block.rect.y = y
        blockList.add(block)
        allSpritesList.add(block)

# Add the player
player = Player(BLACK, 70, 8)
allSpritesList.add(player)
player.rect.x = 215
player.rect.y = 550

# Add the ball
ball = Ball(RED, 10, 10)
allSpritesList.add(ball)
ball.rect.x = 200
ball.rect.y = 200

done = False
clock = pygame.time.Clock()

speedUp = False
count = 0

# Main game loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # The player movement
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        player.moveLeft(speedUp)
    if key[pygame.K_RIGHT]:
        player.moveRight(speedUp)

    allSpritesList.update()

    # Let the ball bouce off the walls
    if ball.rect.x >= 490 or ball.rect.x <= 0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y > 640 or ball.rect.y < 0:
        ball.velocity[1] = -ball.velocity[1]

    # Let the ball bouce off the player
    if pygame.sprite.collide_rect(ball, player) == True:
        ball.velocity[1] = -ball.velocity[1]

    # Let the ball break the block
    blockHitList = pygame.sprite.spritecollide(ball, blockList, True)

    # Let the ball bounce off the block
    for i in blockHitList:
        ball.velocity[1] = -ball.velocity[1]
        # 1 - 10 chance of getting a power up when block is hit
        if random.randint(1, 2) == 2:
            rnd = random.randint(1, 3)
            if rnd == 1:
                powerUp = PowerUp(YELLOW, 15, 7, "speed")
                powerUp.rect.x = ball.rect.x
                powerUp.rect.y = ball.rect.y
                allSpritesList.add(powerUp)

            elif rnd == 2:
                powerUp = PowerUp(RED, 15, 7, "yo")
                powerUp.rect.x = ball.rect.x
                powerUp.rect.y = ball.rect.y
                allSpritesList.add(powerUp)

            elif rnd == 3:
                powerUp = PowerUp(GREEN, 15, 7, "hi")
                powerUp.rect.x = ball.rect.x
                powerUp.rect.y = ball.rect.y
                allSpritesList.add(powerUp)

    try:
        powerUp
    except NameError:
        pass
    else:
        if pygame.sprite.collide_rect(powerUp, player) == True:
            print("yo")
            if powerUp.ability == "speed":
                speedUp = True

    # Set how long the speed power up will last
    if speedUp == True:
        if count > 30:
            speedUp = False
            count = 0
        else:
            count += 1

    # Draw the sprite on the screen
    allSpritesList.draw(screen)
    pygame.display.flip()
    clock.tick(60)
    screen.fill(BLUE)


pygame.quit()

import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
player1y = 175
player2y = 175
p1Speed = 0
p2Speed = 0
xBall = 300
yBall = 400
ballSpeed = 1
yoffset = 3
xoffset = 3
pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop

    # --- Game logic should go here

    if ((yBall > player1y + 200 or yBall < player1y - 10) and xBall < 10) or ((yBall > player2y + 200 or yBall < player2y - 10) and xBall > 690):
        xBall = 350
        yBall = 250
        ballSpeed = 1
    elif xBall <= 10 and xBall > 5 or xBall >= 665 and xBall < 700:
        xoffset = xoffset * -1
    if yBall <= 0 or yBall >= 485:
        yoffset = yoffset * -1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # User pressed down on a key
        elif event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
            if event.key == pygame.K_UP:
                p1Speed = -3
            elif event.key == pygame.K_DOWN:
                p1Speed = 3
            # Player2 controls
            if event.key == pygame.K_w:
                p2Speed = -3
            elif event.key == pygame.K_s:
                p2Speed = 3

    # User let up on a key
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                p1Speed = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                p2Speed = 0

    # --- Screen-clearing code goes here
    # Move the object according to the speed vector.
    # Player 1
    if player1y <= 300 and player1y >= 0:
        player1y += p1Speed
    elif player1y < 0:
        player1y += 1
    elif player1y > 300:
        player1y -= 1

    # Player2
    if player2y <= 300 and player2y >= 0:
        player2y += p2Speed
    elif player2y < 0:
        player2y += 1
    elif player2y > 300:
        player2y -= 1

    # Ball
    yBall -= yoffset * ballSpeed
    xBall -= xoffset * ballSpeed

    # Speed up game
    ballSpeed += 0.001

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)

    # --- Drawing code should go here
    pygame.draw.rect(screen, WHITE, [0, player1y, 10, 200])
    pygame.draw.rect(screen, WHITE, [690, player2y, 10, 200])
    pygame.draw.line(screen, WHITE, [350, 0], [350, 500], 6)
    pygame.draw.ellipse(screen, RED, [xBall, yBall, 25, 25], 0)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()

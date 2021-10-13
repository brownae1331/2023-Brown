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
y = 175
secy = 200
yoffset = 0
y_speed = 0
x = 0
x_speed = 0
pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop

    # --- Game logic should go here

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # User pressed down on a key
        elif event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
            if event.key == pygame.K_LEFT:
                x_speed = -3
            elif event.key == pygame.K_RIGHT:
                x_speed = 3
            elif event.key == pygame.K_UP:
                y_speed = -3
            elif event.key == pygame.K_DOWN:
                y_speed = 3

    # User let up on a key
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0
    # --- Screen-clearing code goes here
    # Move the object according to the speed vector.
    y += y_speed
    x += x_speed
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    #andrew is dumb
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)

    # --- Drawing code should go here
    pygame.draw.rect(screen, WHITE, [x, y, 10, 200])
    pygame.draw.rect(screen, WHITE, [690, 175, 700, 200])
    pygame.draw.line(screen, WHITE, [350, 0], [350, 500], 6)
    pygame.draw.ellipse(screen, RED, [20, 20, 25, 25], 0)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()

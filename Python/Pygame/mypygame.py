import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (47, 154, 222)
BROWN = (165,42,42)
YELLOW = (255,255,0)
x = 0
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLUE)

    x = x + 1
    # --- Drawing code should go here
    pygame.draw.rect(screen, GREEN, [000, 400, 700, 150], 0)
    pygame.draw.rect(screen, BROWN, [200, 300, 400, 450], 0)
    pygame.draw.rect(screen, WHITE, [100, 100, 100, 100], 0)
    pygame.draw.rect(screen, WHITE, [150, 100, 200, 200], 0)
    pygame.draw.rect(screen, YELLOW, [450, 500, 200, 200], 0)
    pygame.draw.ellipse(screen, YELLOW, [x, 100, 200, 200], 0)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
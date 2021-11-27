import pygame
from pygame.constants import K_ESCAPE, KEYDOWN, MOUSEBUTTONDOWN

pygame.init()

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Set screen size
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")

# Define fonts
largefont = pygame.font.SysFont("comicsansms", 50)
smallfont = pygame.font.SysFont("comicsansms", 30)

# Define colors
Black = (0, 0, 0)
White = (255, 255, 255)
Red = (255, 0, 0)


def DrawText(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def MainMenu():
    done = False

    # -------- Game Loop -----------
    while not done:
        screen.fill(Black)
        DrawText('Main Menu', largefont, White, screen, 350, 0)

        mx, my = pygame.mouse.get_pos()

        button1 = pygame.Rect(50, 100, 200, 50)
        button2 = pygame.Rect(50, 200, 200, 50)
        if button1.collidepoint((mx, my)):
            if click:
                PlayerGame()
        if button2.collidepoint((mx, my)):
            if click:
                Computer()

        pygame.draw.rect(screen, Red, button1)
        DrawText('2 Player', smallfont, White, screen, 50, 100)
        pygame.draw.rect(screen, Red, button2)
        DrawText('Computer', smallfont, White, screen, 50, 200)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    done = True
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(60)


def PlayerGame():
    # Set Variable
    player1y, player2y = 175, 175
    p1Speed, p2Speed = 0, 0
    p1score, p2score = 0, 0
    xBall, yBall = 350, 250
    ballSpeed = 1
    yoffset, xoffset = 3, 3

    # Loop until user clicks the close button
    done = False

    # -------- Game Loop -----------
    while not done:
        # When pygame.event is used
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            # When key is pressed down
            elif event.type == pygame.KEYDOWN:
                # When escape is pressed go to Main Menu
                if event.type == K_ESCAPE:
                    done = True
                # Ajust speed when key is pressed down
                # Player 1
                if event.key == pygame.K_w:
                    p1Speed = -3
                elif event.key == pygame.K_s:
                    p1Speed = 3

                # Player 2
                if event.key == pygame.K_UP:
                    p2Speed = -3
                elif event.key == pygame.K_DOWN:
                    p2Speed = 3

            # When key is let up
            elif event.type == pygame.KEYUP:
                # Ajust speed to zero when key is let up
                # Player 1
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    p1Speed = 0

                # Player 2
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    p2Speed = 0

        # Move the object according to the speed vector.
        # --- Player 1
        if player1y <= 300 and player1y >= 0:
            player1y += p1Speed
        elif player1y < 0:
            player1y += 1
        elif player1y > 300:
            player1y -= 1

        # --- Player 2
        if player2y <= 300 and player2y >= 0:
            player2y += p2Speed
        elif player2y < 0:
            player2y += 1
        elif player2y > 300:
            player2y -= 1

        # --- Ball
        yBall -= yoffset * ballSpeed
        xBall -= xoffset * ballSpeed

        # Lets the ball bounce off objects
        if((yBall > player1y + 200 or yBall < player1y - 10) and xBall < 10):
            xBall, yBall = 350, 250
            player1y, player2y = 175, 175
            ballSpeed = 1
            p2score += 1
        elif ((yBall > player2y + 200 or yBall < player2y - 10) and xBall > 665):
            xBall, yBall = 350, 250
            player1y, player2y = 175, 175
            ballSpeed = 1
            p1score += 1
        elif xBall <= 10 and xBall > 5 or xBall >= 665 and xBall < 695:
            xoffset = xoffset * -1
        if yBall <= 0 or yBall >= 485:
            yoffset = yoffset * -1

        # Speed up the game over time
        ballSpeed += 0.001

        # Background color
        screen.fill(Black)

        # Keeps the score of the players
        DrawText(str(p1score), smallfont, White, screen, 310, 0)
        DrawText(str(p2score), smallfont, White, screen, 370, 0)

        # Drawing code
        pygame.draw.rect(screen, White, [0, player1y, 10, 200])
        pygame.draw.rect(screen, White, [690, player2y, 10, 200])
        pygame.draw.line(screen, White, [350, 0], [350, 500], 6)
        pygame.draw.ellipse(screen, Red, [xBall, yBall, 25, 25], 0)
        pygame.display.flip()

        # limit to 60 frames per second
        clock.tick(60)


def Computer():
    # Set Variable
    player1y, player2y = 175, 175
    p1Speed, p2Speed = 0, 0
    p1score, p2score = 0, 0
    xBall, yBall = 350, 250
    ballSpeed = 1
    yoffset, xoffset = 3, 3

    # Loop until user clicks the close button
    done = False

    # -------- Game Loop -----------
    while not done:
        # When pygame.event is used
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            # When key is pressed down
            elif event.type == pygame.KEYDOWN:
                # When escape is pressed go to Main Menu
                if event.type == K_ESCAPE:
                    done = True
                # Ajust speed when key is pressed down
                # Player 1
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    p1Speed = -3
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    p1Speed = 3

            # When key is let up
            elif event.type == pygame.KEYUP:
                # Ajust speed to zero when key is let up
                # Player 1
                if event.key == pygame.K_w or event.key == pygame.K_s or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    p1Speed = 0

        # Computer movement
        if yBall < player2y + 100 and xBall > 350:
            p2Speed = -3
        elif yBall > player2y - 20 and xBall > 350:
            p2Speed = 3
        else:
            p2Speed = 0

        # Move the object according to the speed vector.
        # --- Player 1
        if player1y <= 300 and player1y >= 0:
            player1y += p1Speed
        elif player1y < 0:
            player1y += 1
        elif player1y > 300:
            player1y -= 1

        # --- Player 2
        if player2y <= 300 and player2y >= 0:
            player2y += p2Speed
        elif player2y < 0:
            player2y += 1
        elif player2y > 300:
            player2y -= 1

        # --- Ball
        yBall -= yoffset * ballSpeed
        xBall -= xoffset * ballSpeed

        # Lets the ball bounce off objects
        if((yBall > player1y + 200 or yBall < player1y - 10) and xBall < 10):
            xBall, yBall = 350, 250
            player1y, player2y = 175, 175
            ballSpeed = 1
            p2score += 1
        elif ((yBall > player2y + 200 or yBall < player2y - 10) and xBall > 665):
            xBall, yBall = 350, 250
            player1y, player2y = 175, 175
            ballSpeed = 1
            p1score += 1
        elif xBall <= 10 and xBall > 5 or xBall >= 665 and xBall < 695:
            xoffset = xoffset * -1
        if yBall <= 0 or yBall >= 485:
            yoffset = yoffset * -1

        # Speed up the game over time
        ballSpeed += 0.001

        # Background color
        screen.fill(Black)

        # Keeps the score of the players
        DrawText(str(p1score), smallfont, White, screen, 310, 0)
        DrawText(str(p2score), smallfont, White, screen, 370, 0)

        # Drawing code
        pygame.draw.rect(screen, White, [0, player1y, 10, 200])
        pygame.draw.rect(screen, White, [690, player2y, 10, 200])
        pygame.draw.line(screen, White, [350, 0], [350, 500], 6)
        pygame.draw.ellipse(screen, Red, [xBall, yBall, 25, 25], 0)
        pygame.display.flip()

        # limit to 60 frames per second
        clock.tick(60)


MainMenu()

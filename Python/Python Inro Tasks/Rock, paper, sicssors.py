import random
print("Enter 'R' for rock, 'P' for paper, 'S' for sicssors")
player = input()
rnd = random.randrange(1, 4)
if rnd == 1:
    print("The computer chose rock")
    if player == 'R':
        print("It's a draw")
    elif player == 'P':
        print("You won")
    elif player == 'S':
        print("You lost")
elif rnd == 2:
    print("The computer chose paper")
    if player == 'R':
        print("You lost")
    elif player == 'P':
        print("It's a draw")
    elif player == 'S':
        print("You won")
elif rnd == 3:
    print("The computer chose sissors")
    if player == 'R':
        print("You won")
    elif player == 'P':
        print("You lost")
    elif player == 'S':
        print("It's a draw")

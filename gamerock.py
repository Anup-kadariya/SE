import random

class RockPaperScissor:
    options = ['rock', 'paper', 'scissor']
# first to get 5 points wins the game
    turns = 5
    necessary_wins = turns

# both have 0 points at the start
    player_wins = 0
    computer_wins = 0

    while True:
        # player will be asked to enter their choice
        while True:
            player = input("Please enter either rock, paper or scissor: ")
            if player in options:
                break

        # computer will get random choice from import random
        computer = random.choice(options)

        if player == computer:
            print("DRAW")
        elif player == 'rock' and computer == 'paper':
            print("COMPUTER WON, paper covers rock")
            computer_wins += 1
        elif player == 'rock' and computer == 'scissor':
            print("You win, rock smashes scissor")
            player_wins += 1
        elif player == 'paper' and computer == 'rock':
            print("You win, paper covers rock")
            player_wins += 1
        elif player == 'paper' and computer == 'scissor':
            print("COMPUTER WON, scissor cut paper")
            computer_wins += 1
        elif player == 'scissor' and computer == 'rock':
            print("COMPUTER WON, rock smashes scissor")
            computer_wins += 1
        elif player == 'scissor' and computer == 'paper':
            print("You win, scissor cut paper")
            player_wins += 1

        if player_wins == necessary_wins or computer_wins == necessary_wins:
            break

# print final result
    if player_wins > computer_wins:
        print(">Congratulations, You win! <")
    else:
        print(">Sorry, You lose, COMPUTER WON! <")

    print("> You scored:", player_wins, "point(s) <")
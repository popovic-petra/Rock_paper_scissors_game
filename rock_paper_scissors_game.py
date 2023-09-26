import random
import time

game = ["rock", "paper", "scissors"]
players = {}

print("Hello! Welcome to the rock, paper, scissors game!")
time.sleep(1)

while True:
    flag = int(input(f"Pick an option: \n 1. start game \n 2. show highscores \n 3. exit game \n Enter your choice: "))
    if flag == 1:
        player_name = input("Please enter your username: ")
        player_name = player_name.strip()

        if player_name not in players:
            players[player_name] = 0

        games = 0
        wins = 0
        losses = 0

        while True:
            player = input("Please, write your choice (rock, paper, scissors): ")
            player_lower = player.lower()
            computer = random.choice(game)

            if player_lower in game:
                print("Computer chose " + computer + ".")
                if player_lower == computer:
                    print("It's a tie!")
                elif player_lower == "rock":
                    if computer == "paper":
                        print("You lost!")
                        losses += 1
                    else:
                        print("You won!")
                        wins += 1
                elif player_lower == "paper":
                    if computer == "rock":
                        print("You won!")
                        wins += 1
                    else:
                        print("You lost!")
                        losses += 1
                elif player_lower == "scissors":
                    if computer == "rock":
                        print("You lost!")
                        losses += 1
                    else:
                        print("You won!")
                        wins += 1
                print()
            else:
                print("You did not enter a valid option. Try again.")
                continue

            play_again = input("Do you want to play again? (yes/no): ")
            games += 1
            if play_again.lower() != "yes":
                break

        players[player_name] += wins
        print()
        print(f"{player_name}, you played {games} game(s) today!")
        print(f"You won {wins} game(s) and lost {losses} game(s).")

        play_again = input("Do you want to play with another username? (yes/no): ")
        if play_again.lower() == "yes":
            continue
        print()

    elif flag == 2:
        sorted_players = dict(sorted(players.items(), key=lambda x: x[1], reverse=True))
        print("Highscores:")
        for player, score in sorted_players.items():
            print(f"{player}: {score} wins")

    elif flag == 3:
        print()
        print("Thank you for playing! Have a nice day.")
        break
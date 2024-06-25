# PIG Dice Game

import random

def roll():
    return random.randint(1, 6)

while True:
    players = input("Enter a number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid input, please try again.")

max_score = 50
player_scores = [0] * players

while True:
    game_over = False
    for player_idx in range(players):
        print("\nPlayer", player_idx + 1, "turn has just started!")
        print("Your total score is:", player_scores[player_idx])

        current_score = 0
        while True:
            should_roll = input("Would you like to roll (y/n)? ").lower()
            if should_roll == "n":
                break
            elif should_roll != "y":
                print("Invalid input. Please enter 'y' or 'n'.")
                continue

            value = roll()
            print("You rolled a:", value)
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("Your score is:", current_score)

        player_scores[player_idx] += current_score
        print("Your total score is:", player_scores[player_idx])

        if player_scores[player_idx] >= max_score:
            game_over = True
            break
    
    if game_over:
        break

max_score = max(player_scores)
winning_players = [i + 1 for i, score in enumerate(player_scores) if score == max_score]

if len(winning_players) == 1:
    print(f"Player {winning_players[0]} is the winner with a score of {max_score}!")
else:
    print(f"We have a tie! Players {', '.join(map(str, winning_players))} tied with a score of {max_score}!")

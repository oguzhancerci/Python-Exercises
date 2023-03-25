import random

def play_game():
    
    rock, paper, scissors = 'rock', 'paper', 'scissors'
    beats = {rock: scissors, paper: rock, scissors: paper}
    loses_to = {rock: paper, paper: scissors, scissors: rock}
 
    score = {"wins": 0, "losses": 0, "ties": 0}

    while True:
        
        player_choice = input("Choose rock, paper, or scissors: ").lower()

        if player_choice not in (rock, paper, scissors):
            print("Invalid choice. Try again.")
            continue
 
        computer_choice = random.choice([rock, paper, scissors])

        # Determine the winner
        if computer_choice == loses_to[player_choice]:
            print(f"You chose {player_choice} and the computer chose {computer_choice}. You lost!")
            score["losses"] += 1
        elif computer_choice == beats[player_choice]:
            print(f"You chose {player_choice} and the computer chose {computer_choice}. You won!")
            score["wins"] += 1
        else:
            print(f"Both players chose {player_choice}. It's a tie!")
            score["ties"] += 1
              
        print(f"Score: {score['wins']} wins, {score['losses']} losses, {score['ties']} ties")
        
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != "y":
            break

play_game()

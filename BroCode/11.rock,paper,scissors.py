import random

options = ('rock', 'paper', 'scissors')
is_running = True

while is_running:
    player = None
    computer = random.choice(options)
    
    while player not in options:
        player = input("> Enter a choice: ").lower()

    print(f"Player : {player}")
    print(f"Computer : {computer}")

    if player == computer:
        print(">--->>   Tie Yo!   <<--<")
    elif player == "rock" and computer == "scissors":
        print(">--->>   You win!  <<--<")
    elif player == "paper" and computer == "rock":
        print(">--->>   You win!  <<--<")
    elif player == "scissors" and computer == "paper":
        print(">--->>   You win!  <<--<")
    else:
        print("<---<<   You lose!  >>--->")

    if not input("Play again? (y/n): ").lower() == "y":
        is_running = False  

print("Thanks for playing")
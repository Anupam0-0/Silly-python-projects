import random

lowest_num = 1
highest_num = 100

answer = random.randint(lowest_num, highest_num)

guesses = 0

is_running = True

print()
print("Python No. Guessing Game")
print(f"Select a number betwwen {lowest_num} and {highest_num}")

while is_running:
    guess = input(" >> Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if (guess < lowest_num) or (guess > highest_num):
            print("Out of range")
            print(f"Select a number betwwen {lowest_num} and {highest_num}")
        elif guess < answer:
            print("Too low! Try again!")
        elif guess > answer:
            print("Too High!")
        else:
            print(f"CORECT! The answer is {answer}")
            print(f"No. of guesses: {guesses}")
            is_running = False

    else:
        print("Invalid guess")
        print(f"Select a number between {lowest_num} and {highest_num}")


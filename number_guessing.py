import random

guess_count = 0
number = random.randint(0,100)
won_game = False

print("You have 7 tries to guess the random number")

while guess_count < 7:

    user_guess = int(input("What's your guess? "))
    tries_left = f"You have {6 - guess_count} more tries"

    if user_guess == number:
        print(f"You guessed it in {guess_count + 1} tries! It's {number}")
        won_game = True
        break
    elif user_guess > number:
        guess_count += 1
        print(f"Lower! {tries_left}")
    elif user_guess < number:
        print(f"Higher! {tries_left}")
        guess_count += 1

if won_game != True:
    print(f"Better luck next time.. The number was {number}")
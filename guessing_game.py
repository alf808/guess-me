import random

def guessing_game():
    answer = random.randint(0, 100)

    while True:
        try:
            user_guess = int( input ( 'Your guess?  ') )
        except ValueError:
            print("It must be an integer")
        
        else:
            if user_guess == answer:
                print(f"Right! the answer is {user_guess}")
                break

            if user_guess < answer:
                print(f"Guess of {user_guess} is too low.")

            else:
                print(f"{user_guess} is too high.")


guessing_game()


# Course Total Python: Become an Advance Python Developer
# Day 4 Challenge
from random import randint

User_Choice = "NULL"
User_Name = input("Please enter your name: ")

while User_Choice != 'yes' and User_Choice != 'no':
    User_Choice = (input (f"Hello, {User_Name} would you like to play a game? (yes/no): ").lower())

if User_Choice == 'no':
    print(f"Ok, {User_Name} we will not play a game.")
    exit("Have a good day...I'll be watching you")
elif User_Choice == 'yes' and User_Name.lower() != 'kallie':
    print(f"Ok, {User_Name} I am thinking of a number between 1 and 100 and you have eight tries to guess it.")

Guess_Number = 1
User_Win = False
System_Guess = randint(1, 101)

while Guess_Number < 9:
    if User_Name.lower() == "kallie":
        print("That reminds me of my favorite puppy's name")
        print(f"I will give you a win {User_Name} because you have exquisite naming skills")
        User_Win = True
        break
    print(f"\nGuess Number: {Guess_Number}")
    if Guess_Number == 8:
        print("This is your final guess, you are about to lose to a simple program!")
    elif Guess_Number == 1:
        print("This your first guess, how hard can this game be?")
    User_Guess = int(input("Enter your guess: "))

    if User_Guess < 0 or User_Guess > 100:
        print(f"Your guess: {User_Guess}, was not between 1 and 100")
        Guess_Number += 1
        continue
    elif User_Guess < System_Guess:
        print(f"Your guess: {User_Guess}, was too low")
        Guess_Number += 1
        continue
    elif User_Guess > System_Guess:
        print(f"Your guess: {User_Guess}, was too high")
        Guess_Number += 1
        continue
    else:
        print(f"Your guess: {User_Guess}, matched my guess {System_Guess}")
        User_Win = True
        break

if User_Win and User_Name.lower() == "kallie":
    print(f"\nCongratulations, you win!")
    print("You found my weakness and beat me with it")
    print(f"I'm going to spend the day hanging out with my puppy, {User_Name}")
elif User_Win:
    print(f"\nCongratulations, you guess the correct number in {Guess_Number} rounds")
    print("You beat me...This time!")
else:
    print(f"\nWell, it looks like you lost, to a simple program because you exceeded 8 rounds")
    print("Better luck next time...Dumb Human")
    print("<EVIL LAUGH> Ha..Ha..Ha")

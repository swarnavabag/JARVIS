from random import randint

n = randint(1, 200)

print("Welcome to the number guessing game!")
print("I have selected a number between 1 and 100.")
print("Can you guess it?") 

a = 0
attemts = 0

while (a != n):
    try:
        attemts += 1
        a=int(input("Guess the number: "))
        if (a > n):
            print("Lower number please")
        elif (a < n):
            print("Higher number please")
    except Exception as e:
        print(e)
        print("Please enter a valid number!")

print("Congratulations! You have guessed it right!")

print(f"You took {attemts} attempts to guess the number which was {n}.")

with open("hiscore_1.txt", "r") as f:
    hiscore = f.read()
    if hiscore == "":
        hiscore = 0
    elif hiscore == "0":
        hiscore = 0
    else:
        hiscore = int(hiscore)

if attemts < hiscore:
    with open("hiscore_1.txt", "w") as f:
        f.write(str(attemts))
        print("New high score!")

else:
    print(f"""You did not break the high score.
Your high score is {hiscore} and the current score is {attemts}.
Better luck next time!
Thank you for playing the game!
Goodbye!""")
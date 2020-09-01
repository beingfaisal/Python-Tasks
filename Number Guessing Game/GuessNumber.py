import random


def primeChecker(num):
    isPrime = True
    checker = num - 1
    if num <= 1:
        isPrime = False
    else:
        while isPrime and (checker > 1):
            if num % checker == 0:
                isPrime = False
            else:
                checker -= 1
    return isPrime


number = random.randint(15, 100)
hint1 = hint2 = hint3 = hint4 = hint5 = ""

# Setting the Hints here
hint1 = f"The Number is between {number - random.randint(4, 9)} -- {number + random.randint(1, 9)}"

if number % 2 == 0:
    hint2 = "The number is even"
else:
    hint2 = "The number is odd"

if number % 3:
    hint3 = "The number is not divisible by 3"
else:
    hint3 = "The number is divisible by 3"

if number % 5:
    hint4 = "The number is not  a multiple of 5"
else:
    hint4 = "The number is a Multiple of 5"

if primeChecker(number):
    hint5 = "THe number is a prime Number"
else:
    hint5 = "The number is not a prime number"

# Initializing required variable
hintList = [hint1, hint2, hint3, hint4, hint5]
x = 0
hasGuessed = False

while (x < len(hintList)) and not hasGuessed:
    if x == 0:
        print("Lets start the game here is your first hint\n")
        guessNum = int(input(f"{hintList[x]} \n"))
    else:
        guessNum = int(input(f"{hintList[x]} \n"))
    x += 1
    if guessNum == number:
        hasGuessed = True
    else:
        print("Wrong Guess Try Again")

if hasGuessed:
    print("Congratulation You have beaten the game")
else:
    print("You Lost\n", "The number was ", number)

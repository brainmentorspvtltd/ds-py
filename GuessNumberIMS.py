import random

cpu = random.randint(1,100)
count = 5
while True:
    user = int(input("Guess the number.."))
    if user == cpu:
        print("Congrats you win..")
        break
    elif user > cpu:
        print("You have guessed the larger number..")
    elif user < cpu:
        print("You have guessed the smaller number..")
    else:
        print("Invalid input..")
    count -= 1
    print("chances left:",count)

    if count == 0:
        print("you have lost the game..")
        print("The correct number is :",cpu)
        break

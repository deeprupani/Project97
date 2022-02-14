import random

randomNo=random.randint(1,9)
chance=0

while chance < 5:
    guess=input("Enter Your Guess ")
    guess=int(guess)

    chance=chance+1
    print("Chances: ",chance)

    if (guess > randomNo):
        print("A little bit lower")
    elif guess < randomNo :
        print("A little bit higher")    
    elif guess == randomNo :
        print("Congrats!You won")
        break    

if not chance < 5:
    print("You Lose!The correct no was ",randomNo)
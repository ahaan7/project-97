import random 
print ("number guessing game")
number = random.randint(1,9)
chances=0
print ("guess a number between 1 and 9")
while chances <5:
    guess=int(input("Enter your guess:"))
    if guess==number :
        print("congratas you won")
        break
    elif guess<number:
        print("your guess was too low")
    else:
        print("Your guess was too high")
    chances+=1

if not chances<5:
    print("you lose! the number is ",number)
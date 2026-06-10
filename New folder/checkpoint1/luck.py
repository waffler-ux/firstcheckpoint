import random
ran= random.randint(1,100)
y= int(input("i am thinking of a random number between 1 and 100 try to guess it : "))
while y != ran :
    if y > ran:
        print("too high")
    elif y < ran:
        print("too low")
    y=int(input("try again : "))
print("correct")
import random
import time
ran= random.randint(1,100)
y= int(input("\033[34m"+"i am thinking of a random number between 1 and 100 try to guess it : "))
while y != ran :
    if y > ran:
        time.sleep(1.5)
        print("\033[31m"+"too high")
    elif y < ran:
        time.sleep(1.5)
        print("\033[33m"+"too low")
    time.sleep(2)
    y=int(input("\033[34m"+"try again : "))
print("\033[32m"+"correct")
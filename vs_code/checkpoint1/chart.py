x=input("is it raining ? : ")
import time
t = "yes"
n = "no"
try : 
    if x == t:
        x1=input("do you have an umbrella ? :")
        if x1 == n:
            while x1 == n:
                time.sleep(5)
                x2=input("still raining ?")
                if x2==n:
                    print("go outside.")
                    break
        elif x1 == t:
            print("go outside.")
    elif x == n:
        print("go outside.")
except:
    print("no")
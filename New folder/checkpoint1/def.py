i= int
z= int
import time
import math
f=True
v=False
b = "yes"
n = "no"
def calc(i,z):
    while f:
        try:
            calc=input("would you like to do a normal calculation or the square root of a number : ")
            if calc =="square root":
                sqr=int(input("enter yout number : "))
                sor=math.sqrt(sqr)
                print(sor)
            elif calc == "normal":
                z=int(input("\033[32m"+"enter a number :"))
                time.sleep(1)
                i=int(input("\033[32m"+"enter another number : "))
                time.sleep(1)
                print("\033[34m"+"choose one of the follwing operations + ,- ,* ,/,**,//,%")
                c = "+"
                e = "-"
                q = "/"
                w = "*"
                power = "**"
                div = "//"
                div_rest="%"
                p=input( "the operation is : ")
                if p == c:
                    print(z+i)
                elif p == e:
                    print(z-i)
                elif p == q:
                    print(z/i)
                elif p == w:
                    print(z*i)
                elif p == power:
                    print(z**i)
                elif p == div:
                    print(z//i)
                elif p == div_rest:
                    print("the rest of the division is : ",(z%i))
        except:
            print("\033[97m","please enter a number")
        print("\033[34m"+"again? yes or no")
        time.sleep(1)
        j = input("")
        if j == b:
            print("\033[33m"+"ok")
            time.sleep(1)
        elif j == n:
            print("\033[33m""see you next time.")
            break
print(calc(i,z))
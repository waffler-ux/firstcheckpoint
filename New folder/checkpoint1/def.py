i= int
z= int
import time
f=True
v=False
b = "yes"
n = "no"
def calc(i,z):
    while f :
        i=int(input("\033[32m"+"enter a number :"))
        time.sleep(1)
        z=int(input("\033[32m"+"enter another number : "))
        time.sleep(1)
        print("\033[34m"+"choose one of the follwing operations + ,- ,* ,/")
        c = "+"
        e = "-"
        q = "/"
        w = "*"
        p=input( "the operation is : ")
        if p == c:
            print(z+i)
        elif p == e:
            print(z-i)
        elif p == q:
            print(z/i)
        elif p == w:
            print(z*i)
        print("\033[34m"+"again? yes or no")
        time.sleep(1)
        j = input("")
        if j == b:
            print("\033[34m"+"ok")
            time.sleep(1)
        elif j == n:
            print("")
            break
print(calc(i,z))
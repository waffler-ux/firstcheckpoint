def wow(t):
    low=0
    up=0
    for i in t:
        if i.isupper():
            up+=1
        elif i.islower():
            low+=1
    print(f"the number of loweercases is : ",low)
    print(f"the number of uppercases is : ",up)
s=input("enter a sentence : ")
wow(s)
n=int(input("Enter your choice:")) #Let n be the choice i.e. a,b,c,d
i=0
while n>i:
    if n==0:
        i=0
        print("+0")
    elif n==1:
        i=i+1
        print("+1")
    elif n==2:
        i=i+2
        print("+2")
    elif n==3:
        i=i+3
        print("+3")
    elif n==4:
        i=i+4
        print("+4")
    elif n==5:
        i=i+5
        print("+5")
    else:
        print("Inapprpriate option")
print("You gained",i,"points")
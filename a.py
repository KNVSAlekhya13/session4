
print("you will have 10 chances to check your luck")
for i in range (1,11):
    n=int(input("enter a number"))
    if(i>=10):
        print("your limit is over")
    elif(n==36):
        print("won")
        break
    else:
        print("better luck next time")
    

    
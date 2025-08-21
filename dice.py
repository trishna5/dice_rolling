import random 
low=1
high=6
dice1=random.randint(low,high)
dice2=random.randint(low,high)
while(1):
    ch=input("Roll the dice(y/n):")
    if(ch=="y" or ch=="Y"):
        print(f"({dice1},{dice2})")
    elif(ch=="n" or ch=="N"):
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice")
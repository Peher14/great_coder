print("Welcome to pizza delivery!")
size=input("Enter s,m,l for small medium and large pizza respectively.")
pep=input("Do you want pepper y or n")
cheese=input("Do you want extra cheese y or n")
bill=0
if(pep=="y"):
    if(size=="s"):
        bill=17
    elif(size=="m"):
        bill=23
    elif(size=="l"):
        bill=28
    else:
    print("You entered wrong input for size")
elif(pep=="n")
    if(size=="s"):
        bill=15
    elif(size=="m"):
        bill=20
    elif(size=="l"):
        bill=25
    else:
    print("You entered wrong input for size")   
else:
print("you entered wrong input for pepper")
if(cheese=="y"):
    bill=bill+1
    print("Bill=",bill )        
elif(cheese=="n"):
     print("Bill=",bill )
else:
print("you entered wrong input for cheese")

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
    else:
        bill=28
else:
    if(size=="s"):
        bill=15
    elif(size=="m"):
        bill=20
    else:
        bill=25
if(cheese=="y"):
    bill=bill+1
    print("Bill=",bill )        
else:
     print("Bill=",bill )   

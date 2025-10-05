import random
rock=''',--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
'''
paper='''  ___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----'   '''
scissors='''      
    _       ,/'
   (_).  ,/'
   __  ::
  (__)'  `\.
            `\.
'''
print("LET US PLAY ROCK PAPER AND SCISSORS")
print("CHOOSE 0 FOR ROCK, 1 FOR PAPER AND 2 FOR SCISSORS")
choice=int(input("ENTER YOUR CHOICE\n"))
print("YOUR CHOICE IS")
if(choice==0):
    print(rock)
elif(choice==1):
    print(paper)
elif(choice==2):
    print(scissors)   
else:
    print("INVALID CHOICE")

cc=random.randint(0,2)
print("CCOMPUTER'S CHOICE:\n\n")
if(cc==0):
    print(rock)
elif(cc==1):
    print(paper)
elif(cc==2):
    print(scissors)
if(choice==0):
    if(cc==0):
        print("DRAW")
    elif(cc==1):
        print("YOU LOST")
    else:
        print("YOU WIN")
elif(choice==1):
    if(cc==0):
        print("YOU WIN")
    elif(cc==1):
        print("DRAW")
    else:
        print("YOU LOST")
elif(choice==2):
    if(cc==0):
        print("YOU LOST")
    elif(cc==1):
        print("YOU WIN")
    else:
        print("DRAW")


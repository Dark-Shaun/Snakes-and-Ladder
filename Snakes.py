from random import randint
from Snakes_1 import pname

name_1,name_2=pname()
sum1=0
sum2=0
n=0
n1=0
n2=0

while n!=100:
    i=int(input ("i:"))
    print("Player Name:D_Rolled:Position")
    if i==1:
        sum1=n1
        num1=randint(1,6)#the random function will act like a dice
        sum1=sum1+num1
        n=sum1
        if n in [57,63,4,8,20,71,85,89,44,35]:#These are the Ladder position that means when the token reaches that particular position then it will be climb the ladder if present to higher number.
            if n==57:
                n=84
            elif n==63 :
                n=74
            elif n==4:
                n=94
            elif n==8:
                n=87
            elif n==20:
                n=61
            elif n==71:
                n=81
            elif n==85:
                n=99
            elif n==89:
                n=95
            elif n==44:
                n=88
            else:
                n==4
        if n in [56,60,11,17,68,80,90,77,36]:#These are the Snake positon just like the Ladder position if we reach the Snake position(number) our position will be reduced to lower position
            if n==56:
                n=46
            elif n==60:
                n=50
            elif n==11:
                n=1
            elif n==17:
                n=7
            elif n==68:
                n=48
            elif n==80:
                n=51
            elif n==90:
                n=1
            elif n==77:
                n=2
            else:
                n=3
        n1=n
        if n>100:#The use of 'if' statment is mainly when number rolled out will take the sum i.e value of 'n' beyond 100.
            sum1=sum1-num1
            n=sum1
            n1=n
            print("{}:{}:{}".format(name_1,num1,n))
        elif n==100:
            print("{}:{}:{}".format(name_1,num1,n))
            print("{} has WON!!!!! ".format(name_1))
        else:
             print("{}:{}:{}".format(name_1,num1,n))
    elif i==2:
        sum2=n2
        num2=randint(1,6)#the random function will act like a dice
        sum2=sum2+num2
        n=sum2
        if n in [57,63,4,8,20,71,85,89,44,35]:#These are the Ladder position that means when the token reaches that particular position then it will be climb the ladder if present to higher number.
            if n==57:
                n=84
            elif n==63 :
                n=74
            elif n==4:
                n=94
            elif n==8:
                n=87
            elif n==20:
                n=61
            elif n==71:
                n=81
            elif n==85:
                n=99
            elif n==89:
                n=95
            elif n==44:
                n=88
            else:
                n==45
        if n in [56,60,11,17,68,80,90,77,36]:#These are the Snake positon just like the Ladder position if we reach the Snake position(number) our position will be reduced to lower position
            if n==56:
                n=46
            elif n==60:
                n=50
            elif n==11:
                n=1
            elif n==17:
                n=7
            elif n==68:
                n=48
            elif n==80:
                n=51
            elif n==90:
                n=1
            elif n==77:
                n=2
            else:
                n=3
        n2=n
        if n>100:#The use of 'if' statment is mainly when number rolled out will take the sum i.e value of 'n' beyond 100.
            sum2=sum2-num2
            n=sum2 
            n2=n
            print("{}:{}:{}".format(name_2,num2,n))
        elif n==100:
            print("{}:{}:{}".format(name_2,num2,n))
            print("{} has WON!!!!! ".format(name_2))
        else:
            print("{}:{}:{}".format(name_2,num2,n))
else:
    print("GAME OVER")
    



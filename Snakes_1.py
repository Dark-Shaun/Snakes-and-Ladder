def pname():
    global name_1,name_2
    name_1=input("Enter the name of the player 1:")
    name_2=input("Enter the name of the player 2:")
    print("Number 1 : {}".format(name_1))
    print("Number 2 :{}".format(name_2))
    print("First turn will belong to {}".format(name_1))
    print("Enter i=1 if {}".format(name_1))
    print("Enter i=2 if {}".format(name_2))
    return name_1,name_2
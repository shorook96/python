import random


def guess():
    mylist = ["apple", "banana", "cherry"]
    random.shuffle(mylist)
    choice = mylist[0]
    guessd = []
    l = 0
    countt = 0
    while (l < len(choice)):
        guessd.append(" _ ")
        l = l + 1

    print(guessd)
    count = 0
    mystring = ""
    while (count < 7 and countt < len(choice)):

        lst = []
        c = 0
        inp = input("type a letter \n")
        boolean = inp in choice
        if boolean == True:
            for i in choice:
                if i == inp:
                    lst.append(c)
                    countt = countt + 1
                c = c + 1

            for j in lst:
                guessd[j] = inp
                # else:
                #     print("  _  ",end="")

        count = count + 1

        print(guessd)
    if countt==len(choice):
        print(f"you guessed the word {choice} correctly!")
    else:
        print(f"you failed to guess the word {choice}")


guess()

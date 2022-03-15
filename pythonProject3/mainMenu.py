import datetime


def validatename(varname):
    atrr = input(f"please enter your {varname} make sure it is alphabetic \n")
    if atrr.isalpha():
        return atrr

    return validatename(varname)


def validatephone(varname):

    f=open("users.txt")
    while True:
        phonefound = False
        atrr = input(f"please enter your {varname}:  +20")
        if atrr.isdigit() and len(atrr) == 10:
            for x in f :
                lst=x.split(",")
                if lst[2] == atrr:
                    phonefound=True

            if phonefound == True:
                print("this phone already exist")
            else:
                return atrr
        else:
            print("you haven't entered 10 digits or you haven't entered numeric value  ")


        return validatephone(varname)


def validateemail(varname):

    f=open("users.txt")
    while True:
        emailfound = False
        atrr = input(f"please enter your {varname} make sure it contains @ and . \n")
        if "@" in atrr and "." in atrr and atrr[0]!="@" and atrr[0]!="." :
            for x in f:
                lst=x.split(",")
                if lst[3]==atrr:
                    emailfound=True
            if emailfound==True:
                print("this email already exist")
            else:
                return atrr
        else:
            return validateemail(varname)


def enterpassword(varname):
    atrr = input(f"please enter your {varname} \n ")
    return atrr


def reenterpassword(varname, password):
    passwordmatch = False
    while passwordmatch == False:
        atrr = input(f"please re-enter your {varname} , make sure it matches the pre-entered password \n")
        if atrr == password:
            return atrr


def create():
    phone = input("enter your phone \n")
    f = open("projects.txt", "r")
    for x in f:
        lst = x.split(",")
        if lst[0] == phone:
            print("this phone is already taken")
            return create()
    f.seek(0)
    titleexist = True
    while titleexist == True:
        title = input("enter your project title,it has to be unique ")

        for y in f:

            lstt = y.split(",")

            if lstt[1] != title:
                titleexist = False
            else:
                titleexist = True

    f.close()
    # title=input("type your project title")
    details = input("type details of the project \n")
    target = int(input("type your target \n"))
    while target > 25000:
        target = int(input("please type a number less than 25000 \n"))
    print("kindly provide the start date")
    startdateyear = int(input("type the year  "))
    startdatemonth = int(input("type the month  "))
    while startdatemonth < 1 or startdatemonth > 12:
        startdatemonth = int(input("type a valid month  "))
    startdateday = int(input("type the day  "))
    while startdateday < 1 or startdateday > 31:
        startdateday = int(input("type a valid day  "))
    startdate = datetime.datetime(startdateyear, startdatemonth, startdateday)
    print("kindly provide the end date")
    enddateyear = int(input("type the year  "))
    enddatemonth = int(input("type the month  "))
    while enddatemonth < 1 or enddatemonth > 12:
        enddatemonth = int(input("type a valid month  "))
    enddateday = int(input("type the day  "))
    while enddateday < 1 or enddateday > 31:
        enddateday = int(input("type a valid day  "))

    enddate = datetime.datetime(enddateyear, enddatemonth, enddateday)
    while enddate < startdate:
        print("kindly provide the end date , make sure it greater than the start date")
        enddateyear = int(input("type the year  "))
        enddatemonth = int(input("type the month  "))
        while enddatemonth < 1 or enddatemonth > 12:
            enddatemonth = int(input("type a valid month  "))

        enddateday = int(input("type the day  "))
        while enddateday < 1 or enddateday > 31:
            enddateday = int(input("type a valid day  "))

        enddate = datetime.datetime(enddateyear, enddatemonth, enddateday)
    f = open("projects.txt", "a")
    f.write(
        f"\n{phone},{title},{details},{target},{startdateyear}-{startdatemonth}-{startdateday},{enddateyear}-{enddatemonth}-{enddateday}")
    f.close()


def view():
    f = open("projects.txt")
    count=0
    for x in f:
        lst = x.split(",")
        if count != 0:
            print(f" title: {lst[1]}\n the details: {lst[2]} \n target: {lst[3]} \n startDate: {lst[4]}\n endDate:{lst[5]} \n \n \n ")
        count+=1
    f.close()



def edit():
    flagphone = False
    f = open("projects.txt", "r+")
    phone = ""
    while flagphone == False:

        phone = input("enter your phone,make sure that you have already created a project by this phone \n")

        for x in f:
            lst = x.split(",")
            if lst[0] == phone:
                flagphone = True

    validreply = False
    while validreply == False:
        inp = input(
            "type \n t for changing the title of your project \n d for changing details of your project\n g for "
            "changing your project target \n")

        if inp == 't' or inp == "d" or inp == "g":
            validreply = True
            change = input("type your new value \n")
            with open("projects.txt", "r") as f:
                lines = f.readlines()
            with open("projects.txt", "w") as f:
                for line in lines:

                    if line.split(",")[0] != phone:
                        f.write(line)
                    else:
                        if inp == "t":
                            l = line.replace(line.split(",")[1], change)

                        elif inp == "d":
                            l = line.replace(line.split(",")[2], change)
                        else:
                            l = line.replace(line.split(",")[3], change)

                        f.write(l)


def delete():
    f = open("projects.txt", "r")
    flag = False
    phone = ""
    while (flag == False):
        phone = input("enter your phone \n")

        for x in f:
            lst = x.split(",")
            if lst[0] == phone:
                flag = True
                break
                # f.close()
        print("hi")
    ###############
    print(phone)
    with open("projects.txt", "r") as f:
        lines = f.readlines()
    with open("projects.txt", "w") as f:
        for line in lines:

            if line.split(",")[0] != phone:
                f.write(line)

                #######################



def search():
    yearfound=False
    while yearfound == False:
        year=input("kindly provide the year to show all projects started at this year \n")
        f= open("projects.txt")
        for x in f:
            lst=x.split(",")
            if year in lst[4]:
                yearfound=True
                print(f" title: {lst[1]}\n the details: {lst[2]} \n target: {lst[3]} \n startDate: {lst[4]}\n endDate:{lst[5]} \n \n \n ")
        if yearfound== False:
            print("no projects started at that year \n")


def project():
    inp = input("type \n c for creating a project \n v for viewing projects\n e for editing your project \n d for "
                "deleting "
                "your project \n s for searching a specific project by name \n")
    if inp == 'c':
        return create()
    if inp == "v":
        return view()
    if inp == "e":
        return edit()
    if inp == "d":
        return delete()
    if inp == "s":
        return search()


def login():
    f = open("users.txt", "r")
    emailfound = False
    while emailfound == False:
        email = input("enter your email,make sure you have registered by this email \n")
        password = input("enter your password , make sure it is the one you registered by\n")
        for x in f:
            lst = x.split(",")

            # print(lst)

            if lst[3] != email and lst[4] != password:
                pass
            else:
                f.close()
                return project()


def register():
    fname = validatename("first name")
    lname = validatename("last name")
    phone = validatephone("phone number")
    email = validateemail("email")
    password = enterpassword("password")
    confirmedpass = reenterpassword("password", password)
    f = open("users.txt", "a")
    f.write(f"{fname},{lname},{phone},{email},{confirmedpass}\n")
    f.close()
    # print(fname)
    # print(lname)
    # print(phone)
    # print(email)
    # print(confirmedpass)


def mainMenu():
    x = input("please enter l for login and r for register \n")
    if x == 'r':
        return register()

    elif x == 'l':
        return login()
    else:
        return mainMenu()


mainMenu()

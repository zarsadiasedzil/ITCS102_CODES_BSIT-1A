import getpass
login = False
while login == False:
    unsername = input("Username: ")
    password = getpass.getpass("Password: ")
    if unsername == "Zion" and password == "Mamamo":
        print ("Login success")
    else:
        print("Who are you?")
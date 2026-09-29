#codechallenge4
#Getpass
import getpass
username = input("Please enter username to log in: ")
password = getpass.getpass(input("Please enter password to log in: "))

if username == "Morte" or password == "2021" :
    print()
    print("\t---------------------- [W E L C O M E] -----------------------")
    print("\t------------ Welcome user please fill each blank ------------")
    print()
    
    age = int(input("\tEnter Age : "))
    isEmployed = bool(input("\tAre you currently employed : ")) == "true"
    credits = eval(input("\tCredit Score History : "))
    annual = eval(input("\tHow much is your annual income : "))
    collateral = bool(input("\tDo you have any collateral : ")) == "true"

#Baserate
    base_rate = 0.0

    if age >= 21 and isEmployed == True:
        print()
        print("\t----------------------- COMPUTATION -----------------------")
        print("\n")
        print("\tPassed for baseline eligibility")
        if credits >= 750 :
            print("\tYour credit score is above 750")
            if annual >= 100000:
                print("\tYou have a High Annual Income")
                base_rate = 4.5
                print("\tHi Morte, Your interest rate is ", base_rate)
            else :
                base_rate = 5.0
                print("\tHi Morte, Your interest rate is ", base_rate)
    elif credits >= 600 and credits < 750:
        print("Reach the Credit Score requirements")
        if collateral == True:
            base_rate = 7.0
            print("\tHi Morte, Your interest rate is ", base_rate)
        elif annual < 40000:
            base_rate = 9.5
            print("\tHi Morte, Your interest rate is ", base_rate)
        else:
            base_rate = 8.0
            print("\tHi, Your interest rate is ", base_rate)
    else:
        print("\tReject, Failed baseline eligibility")
            
else:
    print("\tLogin failed. Program stopped.")

print("\t------------------- COMPUTATION COMPLETED -------------------")
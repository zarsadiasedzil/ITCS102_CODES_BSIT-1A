# age (integer)
# is_employed (boolean)
# credit_score (integer)
# annoul_income (float)
# has_collateral (boolean)

age = int(input("Your age: "))
is_employed = bool(input("Are you employed?(Yes or No): ")) == "yes"
credit_score = float(input("What's your credit score: "))
annoul_income = float(input("What's your annoul income: "))
has_collateral = bool(input("Do you have collateral?(True or False): ")) == "true"

# Baseline eligibility
baseline = 0

# Financial Evaluation
if age >= 21 and is_employed == "True":
    print ("Accept")
    if credit_score >= 750:
        print ("Base rate: 5%" )
        if annoul_income >= 100000:
            print ("Final rate: 4.5%")
    elif credit_score >= 600 < 750:
        print ("8.0%")
        if has_collateral == "True":
            print ("Base rate: 7%")
        elif annoul_income < 40000:
            print ("Final rate: 9.5%")
        else:
            print ("Final rate: 8%")
    else credit_score < 600:
        print ()
else:
    print ("Denied")
# age (integer)
# is_employed (boolean)
# credit_score (integer)
# annual_income (float)
# has_collateral (boolean)

age = int(input("Your age: "))
is_employed = bool(input("Are you employed?(True or False): ")) == "true"
credit_score = float(input("What's your credit score: "))
annoul_income = float(input("What's your annoul income: "))
has_collateral = bool(input("Do you have collateral?(True or False): ")) == "true"

# Baseline eligibility
baseline = 0

# Financial Evaluation
if age >= 21 and is_employed == True
    print("Accepted: You're able to loan.")
    if credit_score >= 750:
        if annual_income >= 100000:
            interest_rate = 4.5
        else:
            interest_rate = 5.0
        print("Approvedand has ", interest_rate, "% interest rate")
    elif credit_score >= 600:
        if has_collateral:
            interest_rate = 7.0
        elif annual_income <= 40000:
            interest_rate = 9.5
        else:
            interest_rate = 8.0
        print("Approved and has ", interest_rate, "% interest rate")
    else:
        print("Rejected: Low credit score for loaning.")
else:
    print("Rejected: Requirements not meet.")

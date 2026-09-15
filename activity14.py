# age (integer)
# is_employed (boolean)
# credit_score (integer)
# annual_income (float)
# has_collateral (boolean)

age = int(input("Enter your age: "))
is_employed = bool(input("Are you employed? (True or False): "))
credit_score = float(input("What's your credit score: "))
annual_income = float(input("What's your annual income: "))
has_collateral = bool(input("Have collateral? (True or False): "))

# base interest
interest_rate = 0.0

# calculations
if age >= 21 and is_employed == True :
  if age >= 21 and is_employed:
    print("Accepted: You're able to loan.")
    if credit_score >= 750:
        if annual_income >= 100000:
            interest_rate = 4.5
        else:
            interest_rate = 5.0
        print("Approved and has:", interest_rate, "% interest rate")
    elif credit_score >= 600:
        if has_collateral:
            interest_rate = 7.0
        elif annual_income <= 40000:
            interest_rate = 9.5
        else:
            interest_rate = 8.0
        print("Approved and has:", interest_rate, "% interest rate")
    else:
        print("Rejected: Does not meet the required annoul income")
else:
    print("Rejected: Requirements not meet to loan.")

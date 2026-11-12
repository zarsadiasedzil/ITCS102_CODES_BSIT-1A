# Trial and Error Hands On Quiz
# Break a leg to all of us


# Task 2
# Small Version
print("\nSmall Version")
for x in range(7):
    for y in range(13): 
        if x == 6 or y-x == 6 or x - y == 6 or x + y == 6 or x + y == 18:
            print("*", end="")
        else:
            print(" ", end="")
    print("")

# Bigger Version

print("\n\nBigger Version")
for x in range(7):
    for y in range(13): 
        if x == 6 or y-x == 6 or x - y == 6 or x + y == 6 or x + y == 18:
            print("* ", end=" ")
        else:
            print("  ", end=" ")
    print(" ")


#Task 1 experiment
loan_amount = float(input("Enter Loan Amount: "))
years = int(input("Enter Years: "))
month = years * 12
principal = loan_amount/month
remaining_balance = 0
loan_interest = 0
monthly_pay = 0

for x in range(1, month+1):
    remaining_balance -= principal
    loan_interest = remaining_balance* 0.00256
    monthly_pay = loan_interest + principal
    print(x, monthly_pay,(", "), loan_interest,(", "), round(principal,2),(", "), round(remaining_balance))

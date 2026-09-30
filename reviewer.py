age = int(input("Please enter your age: "))
revenue = float(input("Please enter your revenue: "))
cc = int(input("Please enter credit score: "))
yrs = float(input("Please enter the number of years of your business: "))
has_defaults = bool(input("Do you have any defaults? (True/False): "))
collateral = input("Collateral name: ")
c_value = float(input("Collateral value: "))

max_loan = 0
base_fee = 0

if age >= 21 and yrs >= 2.0 and has_defaults == False:
    print("ACCEPTED: BASELINE REQUIREMENTS MET")
    if cc >= 720: #TIER 1
        print("CREDIT SCORE TOO HIGH")
        max_loan = revenue * 3
        if revenue >= 50000:
            print("REVENUE ABOVE 50k")
            base_fee = max_loan  * 0.015 #1.5%
            print("BASE FEE: ", base_fee)
        else: 
            print("REVENUE BELOW 50k")
            base_fee = max_loan * 0.025 #2.5%
            print("BASE FEE: ", base_fee)

    #COLLATERAL
        if c_value >= max_loan:
            print("COLLATERAL ",collateral," with a value of ",c_value, " is ACCEPTED")
        else:
            print("REJECTED: Insufficient collateral value for ",collateral)

    #SURCHARGE
        if c_value % 5000 != 0:
            base_fee += 250
            print("ADDITIONAL CHARGE ADDED TO BASE FEE. TOTAL BASE FEE IS ", base_fee)
        else:
            print("COLLATERAL VALUE DIVISIBLE BY 5000")

    elif cc >= 620 and cc < 720: #TIER 2
        print("CREDIT SCORE WITHIN 620 - 720")
        max_loan = revenue * 1.5
        if yrs >= 5.0:
            base_fee = max_loan * 0.02
            print("MORE THAN 5 YEARS IN BUSINESS")
        else:
            base_fee = max_loan * 0.035
            print("BUSINESS LESS THAN 5 YEARS. BASE FEE: ", base_fee)
    elif cc < 620:
        print("CREDIT SCORE TOO LOW")
    else:
       print("INVALID: DOES NOT MEET THE REQUIREMENTS.")

#COLLATERAL
        if c_value >= max_loan:
            print("COLLATERAL ",collateral," with a value of ",c_value, " is ACCEPTED")
        else:
            print("REJECTED: Insufficient collateral value for ",collateral)

    #SURCHARGE
        if c_value % 5000 != 0:
            base_fee += 250
            print("ADDITIONAL CHARGE ADDED TO BASE FEE. TOTAL BASE FEE IS ", base_fee)
        else:
            print("COLLATERAL VALUE DIVISIBLE BY 5000")

else:
    print("REJECTED: BASELINE DOES NOT MEET")
      

#code challenge 2
# money = 4567
# 1000, 500, 200, 100, 50, 20, 10, 5, 1
# What operator/ symbol did you use to solve the problem?
# floor division, % modulus

money = 4567

#computation here
thousand = money // 1000
five_hund = (money % 1000) // 500
two_hund = (money % 1000 % 500) // 200
one_hund = (money % 1000 % 500 % 200) // 100
fifty = (money % 1000 % 500 % 200 % 100) // 50
twenty = (money % 1000 % 500 % 200 % 100 % 50) // 20
ten = (money % 1000 % 500 % 200 % 100 % 50 % 20) // 10
five = (money % 1000 % 500 % 200 % 100 % 50 % 20 % 10) // 5
one = (money % 1000 % 500 % 200 % 100 % 50 % 20 % 10 % 5) // 1

#prints here
print("1000 = ",thousand)
print(" 500 = ",five_hund)
print(" 200 = ",two_hund)
print(" 100 = ",one_hund)
print("  50 = ",fifty)
print("  20 = ",twenty)
print("  10 = ",ten)
print("   5 = ",five)
print("   1 = ",one)
print("The total money deposited are",money)

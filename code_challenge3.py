# Global Freight Calculator
# Code Challenge 3

name = input("Input Name: ")
item = input("Type of Item: ")
is_fragile = input("It is Fragile?(Yes/No): ").strip().lower() == "yes"
weight = float(input("Item weight in KG: "))
distance = float(input("Distance in KM: "))
is_express = input("Item express(True/False): ").strip().lower() == "true"
is_international = input("International(True/False): ").strip().lower() == "true"

# Calculation of Base Cost
base_cost = (weight * 2.50) + (distance * 0.15)

# Evaluate Pricing Tiers
# Apply the first matching condition only
if weight <= 2.0 and distance <= 100 and not is_express and not is_international:
	total = 0

elif is_international and is_express:
	total = (base_cost * 1.40) + 50

elif is_express or (is_international and weight > 20):
	total = (base_cost * 1.20) + 25

elif weight > 30 or distance > 1000:
	total = base_cost + 30

else:
	total = base_cost

# Expected Output or Outcome when Printed
print("\n---Resibo---")
print("Tumanggap:", name)
print("Pangalan ng produkto",item)
print("Fragile?:", is_fragile)
print("Timbang:",weight,"KG" )
print("Distansya o Ambulansya?:",distance,"KM")
print("Express:", is_express)
print("International:", is_international)
print("Kabuuang Halaga:", total)
print("\n\nO")
print("\n\nThe order has been dilevered and received by Mr/Mrs.", name, ", product name", item,", weight of product", weight,",and the total cost is", total)

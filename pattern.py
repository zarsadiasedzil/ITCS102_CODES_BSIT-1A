# Trial and Error Hands On Quiz
# Break a leg to all of us


# Task 2
for x in range(7):
    for y in range(13): 
        if x == 6 or y-x == 6 or x - y == 6 or x + y == 6 or x + y == 18:
            print("*", end="")
        else:
            print(" ", end="")
    print("")
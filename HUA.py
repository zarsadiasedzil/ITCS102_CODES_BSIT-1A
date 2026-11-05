for x in range(s):
    for y in range(5):
        if x + y == 5 or y == x:
            print ("*", end = " ")
        else:
            print(" ", end = " ")
        print (" ", end = " ")
    print (" ")
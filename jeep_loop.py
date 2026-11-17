# Jeepney Simulator 
route = ["Terminal", "Perez Park", "Pacific Park", "Manila", "Caloocan", "Mindanao"]
passenger = []
seats = 6
minimum_fare = 13
total = 0

while True:
    print()
    print("Sakay:", passenger)
    print(len(passenger), "of", seats, "seats")
    print("\n1 Sakay\n 2 Priority\n 3 Para po!\n 4 Baba sa pinto\n 5 Baba sa harap\n 6 Seat check\n 7 Balikan\n 8 Exit\n\n")
    choice = input("Choice seat?:")

    if choice == "1":
        if len(passenger) == seats:
            print("Puno na!")
        else:
            name = input("Name?: ")
            passenger.append(name)
            total = total + minimum_fare
            print(name, "boarded at the back")
    elif choice == "2":
        if len(passenger) == seats:
            print("Puno na!")
        else:
            name = input("Name?: ")
            passenger.insert(0, name)
            total = total + minimum_fare
            print(name, "tool the priority seat.")

    elif choice == "3":
        name = input("Who's getting off?")
        if name in passenger:
            passenger.remove(name)
            print(name, "got off. Thank you")
        else:
            print(name, "is not on this jeep")

    elif choice == "4":
        if len(passenger) == 0:
            print("The keep is empty")
        else:
            left = passenger.po()
            print(left, "got off at the door.")

    elif choice == "5":
        if len(passenger) == 0:
            print("The jeep is empty.")
        else:
            front = passenger.pop()
            print(front, "got off at the front")

    elif choice == "6":
        for i in range(len(passenger)):
            print("Seat", i + 1, passenger(i))

    elif choice == "7":
        route.reverse()
        print("Route", route)

    elif choice == "8":
        print("Total fare today: ", minimum_fare)
    
    else:
        print("Invalid choice")
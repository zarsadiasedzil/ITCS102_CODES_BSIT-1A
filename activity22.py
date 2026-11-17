animal_type = ["Monkey", "Bee", "Zebra", "Lion"]
anime_danger_level = []

while True:
    ans = input("Do you know any animal(Yes/No): ")
    
    if ans.lower() == "yes":
        print("What the name of the animal?(select from the list): ")
        for x in animal_type:
            print(x)
        a_type = input("Type: ")

        adl = input("What is the danger level of the animal?(/10): ")
        anime_danger_level.append(adl)
        continue
    else:
        print("Thank you for answering")
        break
#fruits and fruits_shorten

fruits = ["Atis", "Bayabas", "Calamansi", "Dalandan", "Guava", "Lemon", "Dalanghita"]

# dictionary
# key.value

fruits_shortcut = { "Box": "Atis", "Triangle": "Bayabas", "Pentagon": "Calamansi", "Hexagon": "Dalandan", "Nonogon": "Guava", "Rectangle": "Lemon", "Circle": "Dalanghita" }

print (fruits[2])

print (fruits_shortcut["Circle"])

# Traversing and Dictionary
for e, d in fruits_shortcut.items:
    print ("Key word: ", e, " = ", d)
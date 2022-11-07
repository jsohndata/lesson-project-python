# Sequnce = list (like an array), Tuple
#   List: 
#       • Specific Order
#       • Values are mutable (item assigment)
#       • comma seperated


listA = [2,3,5,7,11]
print(listA)

print(f"type => {type(listA)}")

# print 5
print(listA[2])

# Change 2nd inex
listA[2] = 13
print(listA)

listB = [True, "Star", 50, 111.11]
print(listB)

#   Tuple: 
#       • Specific Order
#       • Values are NOT mutable (item assigment)
#       • comma seperated


personA = ("Marucs Aurelius","121 - 180 AD", "Rome")
personB = ("Galus Julius Caesar","49 - 44BC", "Suburra")

print(f"{type (personA)}")
print(f"{type (personB)}")

print(personA[0])
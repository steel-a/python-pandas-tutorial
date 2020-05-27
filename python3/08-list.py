from random import choice

n1 = "Maria"
n2 = "John"
n3 = "Paul"
n4 = "Luke"

# Create a list
listnames = list() # or
listnames = [] # or
listNames = [n1, n2, n3, n4]
print(listNames, 'Last element:', listNames[-1])

# Sort
listNames.sort()
print(listNames)

# Sort reverse
listNames.sort(reverse=True)
print(listNames)

# Append element at end
listNames.append('Sophia')
print(listNames)

# Insert element at specific pos
listNames.insert(0,'Ana')
print(listNames)

# Remove last element
listNames.pop()
print(listNames)

# Remove element from specific pos
listNames.pop(2) # or del listNames[2]
print(listNames)

# Remove first ocurrence of an element if in list
if 'Paul' in listNames:
    listNames.remove('Paul')
print(listNames)

# Choice an element from list
print(choice(listNames))

# Link a list
listNamesLink = listNames

# Copy a list
listNamesCopy = listNames[:]

# Clear a list
listNames.clear()

print(listNames, listNamesLink, listNamesCopy)

# List can be int or any type
listNumbers = list(range(1,4)) # equals to = [1, 2, 3]

# Lists can mix different types, even another list
mixedList = list()
mixedList.append("John")
mixedList.append(25)
mixedList.append(listNumbers) # Link of a list
mixedList.append(listNumbers[:]) # Copy of a list
listNumbers.pop() # Affect just linked list
listNumbers = list(range(1,7)) # This create a new list in same var, does not affect previous list
print(mixedList)

# Access like a matrix
listPData = [['Ana',17],['John',25],['Paul',32]]
print(listPData[0][1],listPData[1][0])
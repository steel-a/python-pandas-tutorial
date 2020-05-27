
names = ('Ariel', 'Maria', 'John', 'Paul')
print(names)
print(sorted(names))
print(len(names))
print(names[-1])
# This is not possible in tuples >> names[2] = 'Try'

# Union
names2 = ('Ana','Linda')
names3 = names + names2
del(names)
del(names2)
print(names3)
print(names3.count('Ana'))
print(names3.index('Ana'))


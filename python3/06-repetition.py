# For in range
for i in range(1,10):
    print(i,end=', ') # 1, 2, 3, 4, 5, 6, 7, 8, 9, 
print('\n')


# For in range, step specification
for i in range(1,10,2):
    print(i,end=', ') # 1, 3, 5, 7, 9,
print('\n')


# For in range, step specification
for i in range(10,1,-1):
    print(i,end=', ') # 10, 9, 8, 7, 6, 5, 4, 3, 2,
print('\n')

# For to interate tuples, lists and dictionaries
word = "Test"
for char in word:
    print(char,end=', ') # T, e, s, t,
print('\n')

# For to interate tuples, lists and dictionaries, with position
word = "Test"
for p, char in enumerate(word):
    print(p,char,end=', ') # 0 T, 1 e, 2 s, 3 t,
print('\n')

# While
i = 0
exit = False
while not exit:
    print(i,end=', ') # 1, 2, 3, 4, 5, 6, 7, 8, 9,
    i += 1
    if i>=10:
        exit = True
print('\n')

# Break
i = 0
while True:
    print(i,end=', ') # 1, 2, 3, 4, 5, 6, 7, 8, 9,
    i += 1
    if i>=10:
        break
print('\n')
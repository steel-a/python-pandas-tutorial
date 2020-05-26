# Numbers: Precedence ()     **      * / // %       + -
n1 = 9
n2 = 4
print('Sum: {}'.format(n1+n2))
print('Minus: {}'.format(n1-n2))
print('Mult: {}'.format(n1*n2))
print('Div: {}'.format(n1/n2))
print('Div: {:.1f}'.format(n1/n2))
print('Pow: {} or {}'.format(n1**n2, pow(n1,n2)))
print('Int Div: {}'.format(n1//n2)) # 2
print('Rest: {}'.format(n1%n2)) # 1

import math
print("Factorial: ",math.factorial(n2)) # 24
print("Square Root: ",math.sqrt(n1)) # 3.0

div = 4/3
print("Number: ",div) # 1.3333333333333333
print("Ceil: ",math.ceil(div)) # 2
print("Floor: ",math.floor(div)) # 1
print("Trunc: ",math.trunc(div)) # 1
print("Trunc: ",int(div)) # 1

import random
print(random.random()) # 0.7501567533620719
print(random.randint(1,10)) # 3

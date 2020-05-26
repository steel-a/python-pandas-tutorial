
# Prints
print('Hello World!')
print(7+4) # 11
print('7'+'4') # 74
print('7','4') # 7 4

# Console data input and prints
name = 'Maria' #input('Whats your name? ')
age = 23
weight = 62.5
print(name,'is',age,'years old and weighs',weight,'kilos')
print('{} is {} years old and weighs {} kilos'.format(name, age, weight))


num1 = '3' #input('Whats the first number? ')
num2 = '10' #input('Whats the second number? ')
num3 = '0'
num4 = ''
print(type(num1), float(num1), bool(num1), bool(num3), bool(num4), bool(7), bool(0))
# <class 'str'>       3.0         True        True        False     True      False
print('Sum:',num1+num2) # Sum: 310
print('Sum:',int(num1)+int(num2)) # Sum: 13
print(num1.isnumeric()) # True

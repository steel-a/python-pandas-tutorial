# Function without parameter
def showLine():
    """
    -> Show a line with size 40
    """
    print('-' * 40)


# Function with parameter
def showTitle(title):
    """
    -> Show a title in center between lines with size 40
    :param title: Title to show
    """
    showLine()
    print(f'{title:^40}')
    showLine()


showTitle("Test")


# Function with variable number of parameters and return
def sum(* num): # inside this function, num is a tuple
    """
    -> Sum numbers
    :param num: tuple with numbers to sum
    :return: sum of values
    """
    s = 0
    for n in num:
        s+=n
    return s


print('Sum:', sum(1,2,3,4))


# NOTE: Lists and Dictionaries as function parameters are passed by reference
def double(lNum):
    for i in range(0,len(lNum)):
        lNum[i] = lNum[i]*2


listNum = list(range(1,10))
print('List single:', listNum)
double(listNum)
print('List double:', listNum)


# Optional parameter
def calcArea(base, height=3):
    return base*height

# Typed parameters
def calcArea2(base: float, height: float=3) -> float:
    return base*height

print('CalcArea:',calcArea(2,2.5), calcArea(2))
print('CalcArea2:',calcArea2(2,2.5), calcArea2(2))

# Pass specific parameter
print('Specific param:',calcArea(base=3))


# Scope of variables
def scope(b):
    b+=1 # new assigment of b does not change a value
    print(a, b) # a can be printed inside a function becaus it's global


def scope2(b):
    a = 4 # this is a new 'a' variable, not the global variable
    b+=1 # new assigment of b does not change a value
    print(a, b) # a can be printed inside a function becaus it's global


def scope3(b):
    global a
    a = 4 # this is the global variable 'a'
    b+=1 # new assigment of b does not change a value
    print(a, b) # a can be printed inside a function becaus it's global


a = 2
scope(a)
scope2(a)
scope3(a)
print(a)

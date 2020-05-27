class MyClass:
    number = 0

    def __init__(self, number=0):
        self.number = number

    def triple(self):
        return self.number*3

    def __del__(self): 
        print('my_package -> my_class -> MyClass destructor called.', self.number) 

class MyClass:
    number = 0

    def __init__(self, number=0):
        self.number = number
        
    def double(self):
        return self.number*2

    def __del__(self):
        print('_my_class -> MyClass destructor called.', self.number) 


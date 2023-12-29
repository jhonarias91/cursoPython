class A():
    def __init__(self):
        #With __ or _ make the attr private(encapsulation)
        self.__counter = 0
    
    def increase(self):
        self.__counter += 1

    def getCounter(self):
        return self.__counter
    
a = A()
print (a.getCounter())        
a.increase()
print (a.getCounter())

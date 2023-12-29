class A():
    def __init__(self):
        self._account = 0

    #@property make the method looks like a attr
    @property
    def account(self):
        return self._account    
    
a = A()
print (a.account)    



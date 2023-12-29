class A():
    def __init__(self):
        self._account = 0
        self._counter = 0

    @property
    def counter (self):
        return self._counter

    @property
    def account(self):
        return self._account    

    @counter.setter
    def counter(self, counter):
        self._counter = counter

    @account.setter
    def account(self, account):
        self._account = account

a = A()
a.account = 50
print(a.account)
a.counter = 28
print (a.counter)



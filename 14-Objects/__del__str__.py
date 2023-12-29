class Phone():
    def __init__(self, branch, color):
        self.branch = branch
        self.color = color
        print("Objeto {} creado".format(self.branch))

    def __del__ (self):
        print("Objeto {} eliminado".format(self.branch))

    def __str__(self):
        return "branch: {} - color: {}".format(self.branch, self.color)
    
phone = Phone("Samsung", "Gray")    
print(phone.__str__())
print(phone)
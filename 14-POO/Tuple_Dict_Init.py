class Phone():
    def __init__(this, branch, *colors, **models):
        this.branch = branch
        this.colors = colors
        this.models = models

    def __str__(self):
        return "Branch: {} - Colors: {} - Models: {}".format(self.branch, self.colors, self.models)

phone = Phone("Samsung", "Blue", "Black", "Red", m1="S23", m2 = "S22", m3="S21")
print (phone)
#* is used to declare that multiples params can be received
def multiplesParam(*params):
    print (type(params))
    for i in params:
        print (i)

a = (5, 6, 7)
multiplesParam(a, 8, 9)        
while True:
    try:
        print(int(input("Input  a number:")))
        break
    except:
        print("Invalid value")
    finally:        
        print("Always executed")

try:
    print(int(input("Value error, type a number:")))
except ValueError:
    print("Invalid value")
    
try:
    b = int(input("ZeroDivisionError, type a number:"))
    a = 80/b
except ZeroDivisionError:
    print("No divide by 0")

try:
    b = int(input("KeyboardInterrupt, type a number:"))
    a = 80/b
    #When press ctrl + C
except KeyboardInterrupt:
    print("Canceled by user")

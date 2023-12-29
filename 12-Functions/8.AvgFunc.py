def avg (*numbers):
    avg = 0
    total = len(numbers)
    for i in numbers:
        avg=avg+i
    return avg/total

print(avg(5,6,7))

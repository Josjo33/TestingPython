import math

def isPrime2(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for check in range(3, int(math.sqrt(number)) + 1, 2):
        if number % check == 0:
            return False
    return True

def check(n):
    print("isPrime2(" + str(n) + ") = " + str(isPrime2(n)))

check(1)
check(3)
check(2)
check(4)    
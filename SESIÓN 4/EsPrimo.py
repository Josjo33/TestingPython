import math


def EsPrimo (number):
    if number <= 1 or (number%2) == 0 :
        return False
    for check in range(3, int (math.sqrt(number))):
        if number % check == 0:
            return False
    return True

def check(n):
    print("EsPrimo(" + str(n) + ") = " + str(EsPrimo(n)))

check(1)
check(2)
check(3)
def esPrimo(num: int) -> bool:

    if num <= 1:
        return False
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    
    return True


# numero = int(input("Introduce un número: "))
# if esPrimo(numero):
#     print(f"El número {numero} es primo.")
# else:
#     print(f"El número {numero} no es primo.")


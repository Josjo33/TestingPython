def son_anagramas(palabra1, palabra2):
    # Convertimos ambas palabras a minúsculas y eliminamos espacios
    palabra1 = palabra1.replace(" ", "").lower()
    palabra2 = palabra2.replace(" ", "").lower()
    
    # Si las longitudes son diferentes, no pueden ser anagramas
    if len(palabra1) != len(palabra2):
        return False
    
    # Ordenamos ambas palabras y comparamos si son iguales
    return sorted(palabra1) == sorted(palabra2)

# Ejemplo de uso
palabra1 = "iman"
palabra2 = "mani"

if son_anagramas(palabra1, palabra2):
    print(f"{palabra1} y {palabra2} son anagramas.")
else:
    print(f"{palabra1} y {palabra2} no son anagramas.")

# Otro ejemplo
palabra1 = "anitalavalatina"
palabra2 = "anitalavalatani"

if son_anagramas(palabra1, palabra2):
    print(f"{palabra1} y {palabra2} son anagramas.")
else:
    print(f"{palabra1} y {palabra2} no son anagramas.")

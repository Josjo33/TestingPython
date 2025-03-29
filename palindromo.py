def es_palindromo(texto):
    texto = str(texto).replace(" ", "").lower()
    return texto == texto[::-1]

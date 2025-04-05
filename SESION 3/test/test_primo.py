from primo import esPrimo

def test_es_primo():
    resultado = esPrimo(3)
    assert resultado == True



def test_noes_primo():
    resultado = esPrimo(10)
    assert resultado == False

from palindromo import es_palindromo

def test_es_palindromo_o_capicuo():
    resultado = es_palindromo("anita lava la tina")
    assert resultado == True
    
    resultado = es_palindromo(12321)
    assert resultado == True

    resultado = es_palindromo("madam")
    assert resultado == True


    
def test_no_es_palindromo_o_capicuo():
    resultado = es_palindromo("hello")
    assert resultado == False
    
    resultado = es_palindromo(12345)
    assert resultado == False

    resultado = es_palindromo("python")
    assert resultado == False

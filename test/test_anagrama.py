from anagrama import son_anagramas 

def test_anagramas_positivos():
    assert son_anagramas("iman", "mani") == True
    assert son_anagramas("analucia", "alucinaa") == True

def test_anagramas_negativos():
    assert son_anagramas("python", "java") == False
    assert son_anagramas("hello", "world") == False

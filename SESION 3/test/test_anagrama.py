from anagrama import son_anagramas 

def test_anagramas_positivos():
    assert son_anagramas("iman", "mani") == True
    assert son_anagramas("analucia", "alucinaa") == True

def test_anagramas_negativos():
    assert son_anagramas("python", "java") == False
    assert son_anagramas("hello", "world") == False





# Caso de prueba con mayúsculas y minúsculas
def test_anagramas_mayusculas_minusculas():
    assert son_anagramas("Amor", "Roma") == True
    assert son_anagramas("Ojo", "JoO") == True

# Caso de prueba con espacios
def test_anagramas_con_espacios():
    assert son_anagramas("un gran hombre", "un hombre gran") == True
    assert son_anagramas("salón de clases", "las clases de salón") == False

# Caso de prueba con palabras de diferentes longitudes
def test_anagramas_longitudes_diferentes():
    assert son_anagramas("python", "pythons") == False
    assert son_anagramas("gato", "gatos") == False

# Caso de prueba con caracteres repetidos
def test_anagramas_con_caracteres_repetidos():
    assert son_anagramas("banana", "anaban") == True
    assert son_anagramas("carrera", "racecar") == False

# Caso de prueba con cadenas vacías
def test_anagramas_cadenas_vacias():
    assert son_anagramas("", "") == True

# Caso de prueba con una palabra vacía y una no vacía
def test_anagramas_palabra_vacia():
    assert son_anagramas("", "hola") == False

# Caso de prueba con caracteres especiales
def test_anagramas_con_caracteres_especiales():
    assert son_anagramas("a@b#c", "c#b@a") == True
    assert son_anagramas("¡hola!", "¡ola h!") == True

# Caso de prueba con números
def test_anagramas_con_numeros():
    assert son_anagramas("12345", "54321") == True
    assert son_anagramas("abc123", "321cba") == True

# Caso de prueba con caracteres no alfabéticos y letras
def test_anagramas_con_caracteres_no_alfabeticos():
    assert son_anagramas("A-B-C", "C-B-A") == True
    assert son_anagramas("test 123", "123 test") == True

# Caso de prueba con palabras muy largas
def test_anagramas_palabras_largas():
    assert son_anagramas("anticonstitucionalmente", "constitucionalmenteanti") == True

# Caso de prueba con palabras similares pero no anagramas
def test_anagramas_no_validos():
    assert son_anagramas("hola", "holaa") == False
    assert son_anagramas("gato", "gata") == False
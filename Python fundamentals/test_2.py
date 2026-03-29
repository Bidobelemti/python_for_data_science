# =========================
# 🟡 TEST NIVEL 2
# =========================

# 1. Contar vocales en una palabra
def contar_vocales(texto):
    vocales = ['a', 'e', 'i', 'o', 'u']
    suma = 0
    for char in texto:
        if char in vocales:
            suma = suma + 1
    return suma


# 2. Retornar el número mayor de una lista (sin usar max)
def maximo(lista):
    return sorted(lista)[-1]


# 3. Verificar si todos los números son positivos
def todos_positivos(lista):
    return False if min(lista) < 0 else True


# 4. Retornar factorial de un número usando bucle
def factorial(n):
    fact = 1
    if n == 1 or n == 0:
        return 1
    for i in range(1, n+1):
        fact = i * fact
    return fact



# 5. Filtrar palabras mayores a 4 letras
def palabras_largas(lista):
    
    return [word for word in lista if len(word) > 4]

# =========================
# TESTS
# =========================
def evaluar():
    print("🟡 Test intermedio\n")

    try:
        assert contar_vocales("hola") == 2
        print("✅ 1 correcto")
    except:
        print("❌ 1 incorrecto")

    try:
        assert maximo([1,5,2,9,3]) == 9
        print("✅ 2 correcto")
    except:
        print("❌ 2 incorrecto")

    try:
        assert todos_positivos([1,2,3]) == True
        assert todos_positivos([1,-1,3]) == False
        print("✅ 3 correcto")
    except:
        print("❌ 3 incorrecto")

    try:
        assert factorial(5) == 120
        print("✅ 4 correcto")
    except:
        print("❌ 4 incorrecto")

    try:
        assert palabras_largas(["hola","python","sol"]) == ["python"]
        print("✅ 5 correcto")
    except:
        print("❌ 5 incorrecto")


if __name__ == "__main__":
    evaluar()
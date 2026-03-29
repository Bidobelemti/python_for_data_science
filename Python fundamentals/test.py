# =========================
# 🟢 TEST BÁSICO
# =========================

# 1. Función que cuenta cuántos números son mayores a 10
def contar_mayores(lista):
    return sum(lista.count(x) for x in lista if x >10)


# 2. Función que devuelve solo números impares
def obtener_impares(lista):
    return [x for x in lista if x % 2 !=0]


# 3. Función que suma números hasta encontrar un 0 (incluido no cuenta)
def suma_hasta_cero(lista):
    suma = 0
    for val in lista:
        if val == 0:
            break
        suma = val + suma
    return suma


# 4. Función que imprime "Aprobado" si nota >= 7, caso contrario "Reprobado"
def estado_nota(nota):
    return 'Aprobado' if nota >= 7 else 'Reprobado'


# =========================
# TESTS
# =========================
def evaluar():
    print("🟢 Test básico\n")

    try:
        assert contar_mayores([5, 12, 20, 3]) == 2
        print("✅ 1 correcto")
    except:
        print("❌ 1 incorrecto")

    try:
        assert obtener_impares([1,2,3,4]) == [1,3]
        print("✅ 2 correcto")
    except:
        print("❌ 2 incorrecto")

    try:
        assert suma_hasta_cero([1,2,3,0,5]) == 6
        print("✅ 3 correcto")
    except:
        print("❌ 3 incorrecto")

    try:
        assert estado_nota(8) == "Aprobado"
        assert estado_nota(5) == "Reprobado"
        print("✅ 4 correcto")
    except:
        print("❌ 4 incorrecto")


if __name__ == "__main__":
    evaluar()
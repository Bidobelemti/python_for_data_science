# =========================================
# 🧪 AUTOGRADER - ESTRUCTURAS DE DATOS
# =========================================

# =========================
# 🔹 EJERCICIO 1 (LISTAS)
# =========================
def obtener_pares(lista):
    """
    Retorna una lista con los números pares
    """
    return lista[1::2] 


# =========================
# 🔹 EJERCICIO 2 (SETS)
# =========================
def interseccion(a, b):
    """
    Retorna la intersección entre dos listas
    """
    return set(a) & set(b) # & es el operador de intersección para sets


# =========================
# 🔹 EJERCICIO 3 (DICCIONARIO)
# =========================
def contar_palabras(texto):
    """
    Retorna un diccionario con la frecuencia de cada palabra
    """
    return {palabra : texto.split().count(palabra) for palabra in set(texto.split())} # split() divide el texto en palabras y count() cuenta la frecuencia de cada palabra


# =========================
# 🔹 EJERCICIO 4 (LISTA SIN DUPLICADOS)
# =========================
def eliminar_duplicados(lista):
    """
    Elimina duplicados manteniendo el orden
    """
    return list(set(lista))


# =========================
# 🔹 EJERCICIO 5 (TUPLAS)
# =========================
def desempaquetar(persona):
    """
    Recibe una tupla (nombre, edad, pais)
    Retorna un string: "Nombre: X, Edad: Y, País: Z"
    """
    return f'Nombre: {persona[0]}, Edad: {persona[1]}, País: {persona[2]}'


# =========================================
# 🧪 TESTS (NO MODIFICAR)
# =========================================

def evaluar():
    print("🔍 Ejecutando pruebas...\n")

    # Test 1
    try:
        assert obtener_pares([1,2,3,4,5,6]) == [2,4,6]
        print("✅ Ejercicio 1 correcto")
    except:
        print("❌ Ejercicio 1 incorrecto")

    # Test 2
    try:
        assert set(interseccion([1,2,3], [2,3,4])) == {2,3}
        print("✅ Ejercicio 2 correcto")
    except:
        print("❌ Ejercicio 2 incorrecto")

    # Test 3
    try:
        resultado = contar_palabras("hola hola mundo")
        assert resultado == {"hola": 2, "mundo": 1}
        print("✅ Ejercicio 3 correcto")
    except:
        print("❌ Ejercicio 3 incorrecto")

    # Test 4
    try:
        assert eliminar_duplicados([1,2,2,3,1]) == [1,2,3]
        print("✅ Ejercicio 4 correcto")
    except:
        print("❌ Ejercicio 4 incorrecto")

    # Test 5
    try:
        assert desempaquetar(("Juan", 25, "Ecuador")) == "Nombre: Juan, Edad: 25, País: Ecuador"
        print("✅ Ejercicio 5 correcto")
    except:
        print("❌ Ejercicio 5 incorrecto")


# Ejecutar evaluación
if __name__ == "__main__":
    evaluar()
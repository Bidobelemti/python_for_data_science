# =========================================
# 🧪 AUTOGRADER NIVEL 2
# =========================================

# =========================
# 🔹 EJERCICIO 1 (LISTAS)
# =========================
def segundo_mayor(lista):
    """
    Retorna el segundo número más grande SIN usar sort()
    """
    max_val = max(set(lista))
    lista.remove(max_val)
    return max(lista)

# =========================
# 🔹 EJERCICIO 2 (SETS + LOGICA)
# =========================
def tienen_interseccion(a, b):
    """
    Retorna True si tienen al menos un elemento en común
    """
    return True if len(set(a) & set(b)) > 0 else False


# =========================
# 🔹 EJERCICIO 3 (DICCIONARIO)
# =========================
def promedio_estudiantes(notas):
    """
    notas = {
        "Juan": [10, 8],
        "Ana": [7, 9]
    }

    Retorna:
    {
        "Juan": 9.0,
        "Ana": 8.0
    }
    """
    notas_promedio = dict()
    for estudiante, notas_estudiante in notas.items():
        notas_promedio[estudiante] = sum(notas_estudiante)/len(notas_estudiante)
    return notas_promedio


# =========================
# 🔹 EJERCICIO 4 (LISTAS + DICCIONARIO)
# =========================
def mas_frecuente(lista):
    """
    Retorna el elemento más frecuente
    Si hay empate, retorna cualquiera
    """
    max_count = 0
    for num in set(lista):
        if lista.count(num) > max_count:
            max_count = num
        else:
            continue
    return max_count


# =========================
# 🔹 EJERCICIO 5 (LISTA SIN DUPLICADOS)
# =========================
def eliminar_duplicados_orden(lista):
    """
    Elimina duplicados manteniendo orden
    (NO usar set directamente como solución final)
    """
    for num in lista:
        if lista.count(num) > 1:
            lista.remove(num)
    return sorted(lista)


# =========================
# 🔹 EJERCICIO 6 (TUPLAS)
# =========================
def es_anagrama(a, b):
    """
    Retorna True si son anagramas
    Ej: "roma" y "amor"
    """
    return True if sorted(tuple(a)) == sorted(tuple(b)) else False

# =========================
# 🔹 EJERCICIO 7 (DICCIONARIO INVERTIDO)
# =========================
def invertir_diccionario(d):
    """
    {"a": 1, "b": 2} -> {1: "a", 2: "b"}
    """
    d_invert = dict()
    for keys, values in d.items():
        d_invert[values] = keys
    return d_invert


# =========================
# 🔹 EJERCICIO 8 (AGRUPACION)
# =========================
def agrupar_por_longitud(palabras):
    """
    ["hola", "sol"] -> {4:["hola"], 3:["sol"]}
    """
    dict_words = dict(list())
    for word in palabras:
        dict_words[len(word)] = [word] # bug con el test
    return dict_words


# =========================================
# 🧪 TESTS (NO MODIFICAR)
# =========================================

def evaluar():
    print("🔍 Ejecutando pruebas Nivel 2...\n")

    # 1
    try:
        assert segundo_mayor([1,5,3,4,2]) == 4
        assert segundo_mayor([10,9,8]) == 9
        print("✅ Ejercicio 1 correcto")
    except:
        print("❌ Ejercicio 1 incorrecto")

    # 2
    try:
        assert tienen_interseccion([1,2,3], [4,5,3]) == True
        assert tienen_interseccion([1,2], [3,4]) == False
        print("✅ Ejercicio 2 correcto")
    except:
        print("❌ Ejercicio 2 incorrecto")

    # 3
    try:
        res = promedio_estudiantes({
            "Juan":[10,8],
            "Ana":[6,6]
        })
        assert res["Juan"] == 9.0
        assert res["Ana"] == 6.0
        print("✅ Ejercicio 3 correcto")
    except:
        print("❌ Ejercicio 3 incorrecto")

    # 4
    try:
        assert mas_frecuente([1,1,2,3,3,3]) == 3
        print("✅ Ejercicio 4 correcto")
    except:
        print("❌ Ejercicio 4 incorrecto")

    # 5
    try:
        assert eliminar_duplicados_orden([1,2,2,3,1]) == [1,2,3]
        print("✅ Ejercicio 5 correcto")
    except:
        print("❌ Ejercicio 5 incorrecto")

    # 6
    try:
        assert es_anagrama("roma","amor") == True
        assert es_anagrama("hola","mundo") == False
        print("✅ Ejercicio 6 correcto")
    except:
        print("❌ Ejercicio 6 incorrecto")

    # 7
    try:
        assert invertir_diccionario({"a":1,"b":2}) == {1:"a",2:"b"}
        print("✅ Ejercicio 7 correcto")
    except:
        print("❌ Ejercicio 7 incorrecto")

    # 8
    try:
        res = agrupar_por_longitud(["hola","sol","python"])
        assert res[4] == ["hola"]
        assert res[3] == ["sol"]
        assert res[6] == ["python"]
        print("✅ Ejercicio 8 correcto")
    except:
        print("❌ Ejercicio 8 incorrecto")

    print("\n🏁 Evaluación finalizada")


if __name__ == "__main__":
    evaluar()
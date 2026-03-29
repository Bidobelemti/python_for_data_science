'''

Sistema de Biblioteca

Diseña un programa usando Programación Orientada a Objetos (POO) que simule una biblioteca.

🔹 Requisitos
1. Clase Libro

Atributos:

título
autor
disponible (True/False)

Métodos:

prestar() → cambia disponible a False
devolver() → cambia disponible a True
2. Clase Usuario

Atributos:

nombre
lista de libros prestados

Métodos:

pedir_libro(libro)
devolver_libro(libro)
3. Clase Biblioteca

Atributos:

lista de libros

Métodos:

agregar_libro(libro)
mostrar_libros()
buscar_libro(titulo)
🔹 Reglas del sistema
No se puede prestar un libro no disponible
Un usuario puede tener varios libros
Mostrar mensajes claros en cada acción

'''

# A book class

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def prestar(self):
        self.disponible = False
        print(self.disponible)

    def devolver(self):
        self.disponible = True
        print(self.disponible)

    def get_titulo(self):
        return self.titulo
    def get_diisponible(self):
        return self.disponible

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = list()
    def pedir_libro (self, libro : Libro):
        if libro.get_diisponible():
            self.libros.append(libro)
            libro.prestar()
            print(f'Libro {libro.get_titulo()} prestado correctamente')
        else:
            print('Libro ocupado')
    def devolver_libro(self, libro : Libro):
        self.libros.remove(libro)
        libro.devolver()
class Biblioteca:
    def __init__(self):
        self.libros = list()
    
    def agregar_libro(self, libro):
        self.libros.append(libro)
        print('Libro agregado correctamente')
    
    def mostrar_libros (self):
        print( f'libros: {[libro.get_titulo() for libro in self.libros]}')

    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.get_titulo() == titulo:
                return libro
        print('No se ha encontrado el libro')
        return None

biblio = Biblioteca()

libro1 = Libro('second ward', 'any_author')
biblio.agregar_libro(libro1)

juan = Usuario('Juan')
juan.pedir_libro(libro1)
juan.devolver_libro(libro1)
sebas = Usuario('Sebas')
sebas.pedir_libro(libro1)

biblio.mostrar_libros()


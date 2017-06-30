# Programa que muestra el uso de las listas en python

print("Uso de listas:")
# Lista vacia
mi_lista = []

# Lista de enteros
mi_lista = [1, 2, 3]
print(mi_lista)

# Lista de tipos de datos mezclados
mi_lista = [1, "Hola", 3.1, 2+5j]
print(mi_lista)

# Lista anidada
mi_lista = [mi_lista, "dato", 5.3, 2, ["lista 2", 3, ["lista 3", 4.0]]]
print(mi_lista)

mi_lista = ['p','r','o','b','e']
# Salida: p
print(mi_lista[0])

# Salida: o
print(mi_lista[2])

# Salida: e
print(mi_lista[4])

# Salida: b
print(mi_lista[-2])

# Error! Only integer can be used for indexing
# my_list[4.0]

# Lista anidada
n_list = ["Happy", [2,0,1,5]]

# Nested indexing

# Salida: a
print(n_list[0][1])    

# Salida: 5
print(n_list[1][3])

my_list = ['p','r','o','g','r','a','m','i','z']
# Elementos 3ro al 5to
print(my_list[2:5])

# Elementos comienzo al 4to
print(my_list[:-5])

# Elementos 5 al final
print(my_list[5:])

# Elementos comienzo al final
print(my_list[:])

# Reasignación
my_list[2] = 0
my_list[5] = 2
my_list[7] = 1
my_list[0:2] = ["la", "la"]
print(my_list)

# Agregar uno o varios elementos, esto es diferente a anidar listas
my_list.append("ni")
my_list.extend(["Esto", "es", "una", "prueba"])
print(my_list)

# Operaciones con listas, también crea una lista con el resultado
print(mi_lista + ["otra", "lista"])
print([1, 2] * 3)

# Inserción dentro de un espacio de la lista
mi_lista = ['a', "be", 1, 2.0]
mi_lista.insert(1, 'c')
mi_lista[3:3] = [4, 5, 6]
print(mi_lista)

# Borrar elementos de una lista o la lista misma
# Salida: Elimina el ultimo elemento y los 3 primeros
del mi_lista[-1]
del mi_lista[1:3]
print(mi_lista)
# Elimina la lista
del mi_lista

# Eliminar el elemento deseado en una lista
mi_lista = ['a', 1, 'b', 2, 'c', 3, 'd', 4, 'e', 5, 'f', 6]
# Salida: elimina el valor "5" de la lista
mi_lista.remove('b')
mi_lista.remove(2)

# Salida: elimina el ultimo elemento su funcionamiento es similar
# al pop en una pila (filo: primero en entrar, ultimo en salir)
mi_lista.pop()
# si se le pasa un parámetro, elimina el valor en la posición equivalente
mi_lista.pop(0)
print(mi_lista)

# Limpiar una lista:
#my_list.clear()
print("Contenido final de la lista: ")
#print(mi_lista.clear())

# Asignación de una lista vacia para eliminar otra lista
mi_lista[2:4] = []
# Salida: elimina los elementos 2 y 3
print(mi_lista)
# Salida: elimina todos los elementos menos el primero y ultimo
mi_lista[1:5] = []
print(mi_lista)

# Lista de métodos:
# append() - Add an element to the end of the list
# extend() - Add all elements of a list to the another list
# insert() - Insert an item at the defined index
# remove() - Removes an item from the list
# pop() - Removes and returns an element at the given index
# clear() - Removes all items from the list
# index() - Returns the index of the first matched item
# count() - Returns the count of number of items passed as an argument
# sort() - Sort items in a list in ascending order
# reverse() - Reverse the order of items in the list
# copy() - Returns a shallow copy of the list

# Probando algunos métodos
print("Prueba de otros métodos: ")
mi_lista = [1, 2, 5, 10, -2, 0, -4]
# Devuelve la posición de los valores pasados por parámetro
print(mi_lista.index(5), mi_lista.index(-2))

# Devuelve el número de apariciones del parámetro
print(mi_lista.count('a'))

print(mi_lista.sort())

print(mi_lista.reverse())

lista2 = [mi_lista.copy()*2]
print(lista2)
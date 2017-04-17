#https://www.programiz.com/python-programming
#Conjunto de programas hechos para retomar el lenguaje 
#de programación interpretado python
'''Recuerda que no es necesaria la compilación y para
ejecutarlo se escribe en consola:
python nombre_del_programa.py
En caso de necesitar la compilación se puede hacer:
python -m py_compile nombre_del_programa.py'''
"""Recuerda también que las identaciones son usadas para
dividir los módulos del código, se recomiendan 4 
espacios en blanco"""
#Programa básico
print("Programa principal")
num1 = 3
num2 = 5
sum = num1+num2
print(sum)
print("hola")

#Uso de for y función range
print("Uso de for")
for i in range(1, 11):
	print(i)
	if i == 5:
		break

#Uso de def, función double y el docstring, en este caso
#es posible exportar los comentario con el uso de
#print(nombre_de_la_funcion.__doc__)
def double(num):
	"""Función que devuelve el doble de un número"""
	return 2*num
print(double.__doc__)

#Prueba de los tipos de datos
print("Prueba de tipos de datos: ")
a = 5
print(a, "es del tipo", type(a))
a = 2.3
print(a, "es del tipo", type(a))
a = 1+2j
print(a, "es un complejo?", isinstance(a,complex))

#Prueba de números hex, oct, bin
print("Prueba de conversion 1: ")
# Salida: 107
print(0b1101011)
# Salida: 253 (251 + 2)
print(0xFB + 0b10)
# Salida: 13
print(0o15)
#Conversión de datos
sum = 2 + 3.1

#Funciones de conversion
print("Prueba de conversión 2: ")
print(int(2.3))
print(int(-5.7))
print(float(12))
print(complex('3+5j'))


#Programa para pruebas con fracciones
import fractions

print("Uso de fracciones: ")
#Salida: 3/2
print(fractions.Fraction(1.5))

#Usando la siguiente linea se facilita un poco el uso de
#la funcion Fractions perteneciente al modulo fractions
from fractions import Fraction as F
#Salida: 5
print(F(5))
#Salida: 1/3
print(F(1,3))
#Salida: 2476979795053773/2251799813685248
print(F(1.1))
#Salida: 11/10
print(F('1.1'))
#Salida: 2/3
print(F(1,3) + F(1,3))
#Salida: 6/5
print(1 / F(5,6))
#Salida: False
print(F(-3,10) > 0)
#Salida: True
print(F(-3,10) < 0)

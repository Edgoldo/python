#Programa que trata el error de precisión en 
#la aproximación de los valores usados para
#operar en los programas
import decimal

print("Error de precisión")
print(0.1)
print(decimal.Decimal(0.1))

#Operaciones tomando en cuenta la precisión
print("Operaciones de precisión")
from decimal import Decimal as D
print(D('1.1')+decimal.Decimal('2.2'))
print(D('1.2')*D('2.5'))

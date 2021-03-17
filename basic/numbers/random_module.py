# Programa con uso del modulo random
import random

print("Modulo random y uso de algunas funciones")
# Salida: 16
print(random.randrange(10,20))

x = ['a', 'b', 'c', 'd', 'e']

# Elección aleatoria
print(random.choice(x))

# Ordenamiento aleatorio
random.shuffle(x)

# Impresión luego del ordenamiento aleatorio
print(x)

# Imprime un elemento aleatorio
print(random.random())

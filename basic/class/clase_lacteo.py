"""
Course received at the free software academy (ASL) of FUNDACITE Mérida.

Class, methods, decorators, inheritance
"""
class Lacteo:
  
  def __init__(self, tipo, cantidad):
    self.__tipo = None
    self.__cantidad = None
    
    self.tipo = tipo
    self.cantidad = cantidad
    
  @staticmethod
  def lacteo_valido(tipo):
    if (not isinstance(tipo, str)):
      return False
    return (tipo.upper() == "QUESO" or tipo.upper() == "CREMA")
    
  @staticmethod
  def peso_lacteo_valido(tipo, cantidad): 
    if (isinstance(cantidad, (int, float))):
      if (tipo == "QUESO" and (cantidad == 1 or cantidad == 2)):
        return True
      if (tipo == "CREMA" and (cantidad == 0.5 or cantidad == 1)):
        return True
    return False
      
  @property
  def tipo (self):
    if (self.lacteo_valido(self.__tipo)):
      return self.__tipo
    return "Tipo lacteo no asignado"
  
  @tipo.setter
  def tipo (self, tipo):
    if (self.lacteo_valido(tipo)):
      self.__tipo = tipo.upper()
      return
    print ("Tipo de lacteo no valido")

  @property
  def cantidad(self):
    if (self.__cantidad != None):
      return self.__cantidad
    print ("Cantidad de lacteo no valida")
  
  @cantidad.setter
  def cantidad(self, cantidad):
    if (self.peso_lacteo_valido(self.__tipo, cantidad)):
      self.__cantidad = cantidad
      return 
    print ("Cantidad de lacteo no valido")
      
  @classmethod
  def cantidad_leche(cls, tipo, litros):
    if (Lacteo.lacteo_valido(tipo)):
      if (tipo.upper() == "QUESO" and (litros == 20 or litros == 40)):
        return cls(tipo, litros/20)
      if (tipo.upper() == "CREMA" and (litros == 50 or litros == 100)):
        return cls(tipo, litros/100)
    return cls(tipo, litros)
    
  def __str__(self):
    if (self.__tipo != None and self.__cantidad != None):
      return self.__tipo + " de " + str(self.__cantidad) + " Kgs"
    
    return "Lacteo con datos invalidos"
    
class Cesta(list):
  
  def __init__(self, tipo):
    self.__tipo = None
    if (Lacteo.lacteo_valido(tipo)):
      self.__tipo = tipo.upper()
      
  @staticmethod
  def peso_cesta_valido(tipo, peso):
    if (not Lacteo.lacteo_valido(tipo) or not isinstance(peso, (int, float))):
      print ("tipo o peso no valido")
      return 
    return ((tipo == "QUESO" and (0 <= peso <= 10)) or 
           (tipo == "CREMA" and (0 <= peso <= 20)))
      
  def agregar_productos(self, cantidad, peso):
    if (not Lacteo.peso_lacteo_valido(self.__tipo, peso)):
      print ("Peso de lacteo no valido")
      return 
     
    if (not self.peso_cesta_valido(self.__tipo, self.peso() + cantidad*peso)):
          print ("Peso de cesta excedido")
          return
        
    self += [Lacteo(self.__tipo, peso) for i in range(cantidad)]
      
  def peso(self):
    from functools import reduce
    if (len(self) >= 2):
      return reduce(lambda x,y : x+y, [lacteo.cantidad for lacteo in self])
    elif (len(self) == 1):
      return self[0].cantidad
    else:
      return 0
      
  def __add__(self, cesta2):
    newCesta = Cesta(self.__tipo)
    if (self.__tipo == cesta2.__tipo and 
        self.peso_cesta_valido(self.__tipo, self.peso() + cesta2.peso())):

      newCesta.extend(self)
      newCesta.extend(cesta2)
    else:      
      print ("cestas distinto tipo o peso excedido")
    
    return newCesta
    
  def verCesta(self):
    for lacteo in self:
      print (lacteo)
      
  def __setitem__(self, indice, lacteo):
    if (not(isinstance(lacteo,Lacteo)) or lacteo.tipo != self.__tipo):
      print ("dato de lacteo no valido")
      return
    
    if (indice < len(self)):
      if (self.peso_cesta_valido(self.__tipo, self.peso() - self[indice].cantidad + lacteo.cantidad)):
        self[indice].cantidad = lacteo.cantidad
      else:
        print ("Asignacion excede peso")
    else:
      print ("Indice no valido")
    
def pos_lacteos_peso(cesta, peso):
  i = 0
  for lacteo in cesta:
    if lacteo.cantidad == peso:
      yield i
    i += 1
    
c = Cesta("Crema")

c.agregar_productos(2,0.5)
c.agregar_productos(3,1)
c.agregar_productos(1,0.5)
  
q = Lacteo("crema",0.5)  
c[3] = q

for pos in pos_lacteos_peso(c,2):
  print (pos)
      
c.verCesta()
"""
Course received at the free software academy (ASL) of FUNDACITE Mérida.

Other example of class, methods, decorators, getters and setters
"""
class Lapicero:
  nro_lapicero = 0
  colores = ["negro","azul","rojo"]
  
  def __init__(self, color):
    if (Lapicero.colorvalido(color)):
        self.color = color
    else:
        self.color = None
        print ("Error en color")
    self.__cantidad = 10 # 100%
    Lapicero.nro_lapicero += 1
  
  @staticmethod  
  def colorvalido(ncolor):
    if (ncolor.lower() in Lapicero.colores):
      return True
    return False
 
  @classmethod  
  def colorHx(cls, colorHx):
    if (colorHx == 0xFFFFFF):
      return cls("negro")
    elif (colorHx == 0xFF0000):
      return cls("rojo")
    elif (colorHx == 0x0000FF):
      return cls("azul")
    else:
      print ("Color invalido")
      return None
    

  def escribir(self,palabra):
    if (self.__cantidad >= len(palabra)):
      self.__cantidad = self.__cantidad - len(palabra)
    else:
      print ("No tengo tinta")
  
  @property
  def cantidad(self):
    if (self.__cantidad == 10):
      return "full"
    elif (self.__cantidad == 0):
      return "vacio"
    return self.__cantidad

  @cantidad.setter
  def cantidad(self,n):
    if (self.__cantidad + n <= 10):
      self.__cantidad += n
    else:
      print ("Sobrecarga")
      
class Cartuchera:
  def __init__(self,n):
    self.__num = 0
    self.num = n
    self.__lapiceros = []
    
  @property
  def num(self):
    return self.__num
  
  @num.setter
  def num(self, n):
    if (type(n) != int and n > 0):
      print ("dato invalido")
      return 
    self.__num += n

l1 = Lapicero("Azul")
l2 = Lapicero("Negro")
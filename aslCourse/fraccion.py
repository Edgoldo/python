class Fraccion(object):
  
  def __init__(self,num=None,den=None):
    self.num = num
    self.den = den
    
  def __add__ (self, f):
    if (isinstance(f,int)):
      f = Fraccion (f,1)
      
    if (isinstance(f,Fraccion) == True):
      fr = Fraccion()
      fr.den = self.den * f.den
      fr.num = self.num*f.den + f.num*self.den
      return fr
      
  def __mul__(self, f):
    if (isinstance(f,int)):
      f = Fraccion (f,1)
      
    if (isinstance(f,Fraccion) == True):
      fr = Fraccion()
      fr.num = self.num * f.num
      fr.den = self.den * f.den
      return fr

  def __radd__(self,value):
      return self + value

  def __rmul__(self,value):
      return self * value

  def __str__(self):
    return str(self.num) + "/" + str(self.den)
    
  def __setattr__(self, name, value):
    if (name == "den"):
      if (type(value) != int or value == 0):
        value = 1
      object.__setattr__(self,name,value)
        
    if (name == "num"):
      if (type(value) != int):
        value = 1
      object.__setattr__(self,name,value)
      
  def __del__(self):
    print ("lo elimino")
      
class LstFraccion():
  def __init__(self):
    self.datos = []
    
  def append(self,f):
    if (isinstance(f,Fraccion)):
      self.datos.append(f)
    else:
      print ("dato incorrecto")
      
  def insert(self, pos, value):
    if (isinstance(f,Fraccion)):
      self.datos.insert(pos,value)
    else:
      print ("dato incorrecto")
      
  def __setitem__(self,index,value):
    if (not isinstance(value,Fraccion)):
      print ("dato invalido")
      return 
    
    if (0 <= index < len(self.datos)):
      self.datos[index] = value
      
  
  def __getitem__(self,index):
    return self.datos[index]
    
lf = LstFraccion()
f = Fraccion(2,3)
f1 = Fraccion(1,2)
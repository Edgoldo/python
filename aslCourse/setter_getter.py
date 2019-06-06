class Prueba(object):
  def __init__(self):
    self.n = 0
    self.m = 0
    pass
    
  def __getattr__(self, name):
    if (name == "x"):
      self.x = 1
      return 1
    return "atributo no existe"
    
  def __setattr__(self,name,value):
    object.__setattr__(self,name,value+1)
    
    
obj = Prueba()
print (obj.n)
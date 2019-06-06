class LstNotas():
  
  def __init__(self, n):
    self.n = n
    self.notas = [0 for x in range(n)]
  
  def __setitem__(self, index, value):
    if (0 <= index < self.n):
      if (0 <= value <= 20):
        self.notas[index] = value
      else:
        print "valor invalido"
    else:
      print ("fuera de rango")

  def __getitem__(self,index):
    if (0 <= index < self.n):
      return self.notas[index]
    else:
      print ("fuera de rango")
  
  def __str__(self):
    cad = ""
    for n in self.notas:
      cad = cad + str(n)
    return cad 
  
py = LstNotas(3)
#py[0] = 5
# py[0] = 7


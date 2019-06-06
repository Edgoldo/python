def buscar(l,g = None):
  for n in l:
    if (g(n) == True):
      print (n)
    

def es_par(n):
  return (n%2 == 0)
  
def es_impar(n):
  return (n%2 == 1)
  
def es_cinco(n):
  return (n == 5)

l = [5,3,6,5,3,2,1]
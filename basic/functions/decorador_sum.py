"""
Course received at the free software academy (ASL) of FUNDACITE Mérida.

Building decorators
"""
def sumint(fun):
  def contenedor(l):
    a = []
    for i in l:
      if (type(i) == int):
        a.append(i)
      elif (type(i) == tuple):
        a.append(contenedor(i))
        
    return fun(a)
    
  return contenedor

@sumint
def suma(l):
  s = 0
  for i in l:
    s= s + i
  return s


a = ["a",5,6,True,(1,5),5]

print (suma(a))


"""
def divZero(div):
  def div0(a,b):
    if (b==0):
      return "Infinity"
    return div(a,b)
  
  return div0
  

def entero(fun):
  def contenedor(a,b):
    n = fun(a,b)
    if (type (n) == float):
      return int(n)
      
  return contenedor

    
@divZero
@entero
def div(a,b):
  return a/b
  
print (div(5,0))
"""
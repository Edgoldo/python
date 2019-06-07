def Decorador(funcion):
    def contenedor(a):
        print ("El resultado es ",end="") 
        return funcion(a)
 
    return contenedor
    
@Decorador
def func1 (n):
  print (n)
  
func1(5)
  
#func2 = Decorador(func1)
#func2(5)
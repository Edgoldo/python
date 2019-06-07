def numeros():
  n = 0
  paso = 1
  while (True):
    y = yield n
    if (type(y) == int):
      paso = y
    n = n + paso

l = numeros()
  
cont = 0  
while(True):
  print (next(l),end="")
  cont += 1
  if (cont%10==0):
    print()
    print (l.send(cont//10+1),end="")
  if (cont > 60):
    break
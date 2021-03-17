"""
Course received at the free software academy (ASL) of FUNDACITE Mérida.

Reduce and lambda to make filters
"""
from functools import reduce
a = [2,3,2,1,1,3,5,7,-1,5,8]


f = lambda x,y : x+y if (x%2==0 and y%2==0) else x if (x%2==0) else y if (y%2==0) else 0

n  = reduce (f, a)

print (n)

x = ["*",2,"*",2,"*",2,"*",2]

f2 = lambda x,y: 2 if (type(x)==str and type(y)==str) else 1 if (type(x)==str) else x+1 if (type(y)==str) else x

m = reduce (f2,x)

print (m)

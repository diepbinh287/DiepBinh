a=int(input('a= '))
b=int(input('b= '))
c=int(input('c= '))
s=(a+b+c)/2
import math 
d=(s*(s-a)*(s-b)*(s-c))
print('Dien tich: ', math.sqrt(d)) 
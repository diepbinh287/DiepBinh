a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
import math
if (a+b)>c and (a+c)>b and (b+c)>a:
            p=(a+b+c)/2
            s=p*(p-a)*(p-b)*(p-c)
            print('Dien tich=',round(math.sqrt(s),3),sep='')
else: print('Khong hop le')
               
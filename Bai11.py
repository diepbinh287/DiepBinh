n=int(input())
i=0
j=0
if n>0:
    i=i+1
if n<0:
    j=j+1
while n>0 or n<0:
    n=int(input())
    if n>0:
        i=i+1
    if n<0:
        j=j+1
print(i,'so duong')
print(j,'so am')
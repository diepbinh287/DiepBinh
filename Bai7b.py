n=int(input())
while n>=0:
    a=1
    for i in range(1,n+1):
        a=a*i
    print(a)
    n=int(input())
if n==0:
    print('1')
n=int(input('n='))
if 0<=n<=100:
    if n>0:
        a=1
        for i in range(1,n+1):
            a=a*i
        print(n,'!=',a,sep='')
    if n==0:
        print('0!=1')
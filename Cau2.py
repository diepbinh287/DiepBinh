n=int(input('n='))
if n<=30:
    for i in range(1,n+1):
        if i%10==0:
            print(i)
        else:
            print(i,end=' ')
if n>30:
    for i in range(1,31):
        if i%10==0:
            print(i)
        else:
            print(i,end=' ')
    print('...')
    for i in range(41,n+1):
        print(i,end=' ')
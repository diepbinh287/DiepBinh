n=int(input('n='))
i=1
while i<=n<=30:
    if i%10==0:
        print(i)
    else: 
        print(i,end=' ')
    i=i+1
i=1
if n>=31:
    while i<=30:
        if i%10==0:
            print(i)
        else: 
            print(i,end=' ')
        i=i+1
    i=41
    print('...')
    while n>=i>=41:
        print(i,end=' ')
        i=i+1
n=int(input('n='))
if n==2:
    print(n,'la SNT')
if 2<n<=100:
    for i in range(2,n):
        if n%i==0:
            print(n,"khong la SNT")
            break
    else:
        print(n,"la SNT")
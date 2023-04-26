n=int(input())
a=''
if 0<=n<=9999:
    i=str(n)
    for j in i:
        if j=='0':
            a=a+'A'
        elif j=='1':
            a=a+'B'
        elif j=='2':
            a=a+'C'
        elif j=='3':
            a=a+'D'
        elif j=='4':
            a=a+'E'
        elif j=='5':
            a=a+'F'
        elif j=='6':
            a=a+'G'
        elif j=='7':
            a=a+'H'
        elif j=='8':
            a=a+'K'
        elif j=='9':
            a=a+'L'
    print(a)
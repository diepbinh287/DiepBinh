a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
if a>b:
    if b>c:
        print('SLN=',a,sep='')
        print('SNN=',c,sep='')
    else:
        print('SLN=',a,sep='')
        print('SNN=',b,sep='')
elif a<c:
    print('SLN=',b,sep='')
    print('SNN=',a,sep='')
elif a>c:
    print('SLN=',b,sep='')
    print('SNN=',c,sep='')

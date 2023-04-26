a=float(input('a='))
b=float(input('b='))
toantu=str(input('Toan tu:'))
while toantu=='+' or toantu=='-' or toantu=='*' or toantu=='/':
    if toantu=='+':
        print(a,toantu,b,'=',a+b,sep='')
    elif toantu=='-':
        print(a,toantu,b,'=',a-b,sep='')
    elif toantu=='*':
        print(a,toantu,b,'=',a*b,sep='')
    elif toantu=='/':
        if b!=0:
            print(a,toantu,b,'=',a/b,sep='')
    tt=str(input('Tiep tuc:'))
    if tt=='T' or tt=='t':
        break
    else:
        a=float(input('a='))
        b=float(input('b='))
        toantu=str(input('Toan tu:'))
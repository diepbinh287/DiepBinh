a=float(input('Tieu thu='))
if a<=150:
    if a<=100:
        print('Phai tra=',((550*a)*0.1)+550*a,sep='')
    else: 
        print('Phai tra=',((750*a)*0.1)+750*a,sep='')
elif a<=200:
    print('Phai tra=',((950*a)*0.1)+950*a,sep='')
else: 
    print('Phai tra=',((1350*a)*0.1)+1350*a,sep='')
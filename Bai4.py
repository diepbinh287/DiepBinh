t=float(input(''))
l=float(input(''))
h=float(input(''))
dtb=(t*2+l*3+h)/6
if dtb<3:
    print('Kem')
elif dtb<5:
    print('Yeu')
elif dtb<6:
    print('Trung binh')
elif dtb<7:
    print('Trung binh Kha')
elif dtb<8:
    print('Kha')
elif dtb<9:
    print('Giỏi')
else:
    print('Xuat sac')
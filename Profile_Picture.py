pix=int(input())
p=int(input())
Maxpix=10000
Maxpics=1000

if pix > Maxpix and p > Maxpics:
        print('Limit Size Exceeded')
        exit()

for i in range(p):
    Dim=input().split()
    if len(Dim)!=2:
        print('Error')
    elif  int(Dim[0]) == int(Dim[1]) and int(Dim[0])>= pix:
        print('ACCEPTED')
    elif int(Dim[0]) >= pix  and int(Dim[1]) >= pix:
        print('CROP IT')
    else:
        print('UPLOAD ANOTHER')



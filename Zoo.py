x='zzoooo'
Z=0
O=0
ERR=False
for i in x:
    if i=='z':
        if O>0:
            print('No')
            ERR=True
            break
        elif Z>20:
            print('No')
            ERR=True
            break
        else:
            Z = Z+ 1    
    elif i=='o':
        O=O+1
    else:
        print('No')
        ERR=True
        break


if ERR == True:
    print ("string does not match")
else:
    if 2*Z == O:
        print ("Valid")
    else:
        print ("Invalid")

# print(len(Z),len(O))

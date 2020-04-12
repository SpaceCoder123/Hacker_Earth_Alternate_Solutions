n=int(input())
for i in range(n):
    S=input()
    S1=S[::-1]
    if S==S1:
        if len(S)%2==0:
            print('YES EVEN')
        else:
            print('YES ODD')

    else:
        print('N0')

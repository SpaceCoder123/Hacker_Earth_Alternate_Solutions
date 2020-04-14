T=int(input())
for z in range(T):
    x=input().split()
    y=input().split()
    k =  int(x[0])
    lp = len(y) - (int(x[1])% int(x[0])) -1

    for i in range(k):
        print (y[(lp + 1) % k],end=' ')
        lp = (lp + 1) % k

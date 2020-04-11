
S='mohan'
X=[]
for i in S:
    X.append(i)
alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
W=0

for i in range(len(X)):
    for j in range(len(alpha)):         
        if X[i]==alpha[j]:
            print(i,j)
            W=W+(j+1)
print(W)



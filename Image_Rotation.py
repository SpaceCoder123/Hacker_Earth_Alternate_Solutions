R=int(input('Rows '))

matrix=[]
for i in range(R):
    a=[]
    for j in range(R):
        a.append(int(input()))
    matrix.append(a)

#print(matrix)

Result=[]
for i in matrix:
    #print(i)
    Resultant=[]
    for j in matrix[i]:
        print(j)
        #x=R-j
        matrix[i][j]=matrix[x][i]
        Resultant.append(matrix[x][i])
    Result.append(Resultant)

print(Result)



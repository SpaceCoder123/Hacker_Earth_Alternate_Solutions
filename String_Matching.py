
x='ab'
y='abc'
result=''

if len(x)>len(y):
	print('')
for i in range(len(x)):
	for j in range(len(y)):
		if y[j]==x[i]:
			result=result+y[j]			
if x==result:
	print('YES')


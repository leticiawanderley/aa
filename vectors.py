#Codeforces 69A
forces = int(input())
x = 0
y = 0
z = 0
for i in range(forces):
	vector = list(map(int, input().split()))
	x += vector[0]
	y += vector[1]
	z += vector[2]
if x == y == z == 0:
	print('YES')
else:
	print('NO')

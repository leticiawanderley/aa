#URI 1796
q = int(input())
v = list(map(int, input().split()))

count = 0
i = 0
while count <= q/2 and i < q:
	if v[i] == 0:
		count += 1
	i += 1

if count > q/2:
	print("Y")
else:
	print("N")
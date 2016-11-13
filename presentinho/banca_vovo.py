#SPOJ SALDO13
entry = list(map(int, input().split()))
n = entry[0]
s = entry[1]
smallest = s

for i in range(n):
	v = int(input())
	s = s + v
	if smallest > s:
		smallest = s
print(smallest)

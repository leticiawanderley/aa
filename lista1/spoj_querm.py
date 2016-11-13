#Spoj QUERM
n = int(input())
test = 1
while n != 0: 
	entries = list(map(int, input().split()))
	for i in range(n):
		if i + 1 == entries[i]:
			result = i + 1
			break
	print("Teste " + str(test))
	print(result)
	print()
	test += 1
	n = int(input())
#URI 1044
ints = sorted(list(map(int, input().split())))

if ints[1]%ints[0] == 0:
	print("Sao Multiplos")
else:
	print("Nao sao Multiplos")

#URI 1091
t = int(input())
while t != 0:
	point = list(map(int, input().split()))
	for i in range(t):
		result = ''
		home = list(map(int, input().split()))
		if point[0] == home[0] or point[1] == home[1]:
			result = 'divisa'
		else:
			if home[1] > point[1]:
				result += 'N'
			else:
				result += 'S'
			if home[0] > point[0]:
				result += 'E'
			else:
				result += 'O'
		print(result)
	t = int(input())
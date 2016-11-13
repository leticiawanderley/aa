#Codeforces 567A
def distance(a, b):
	if a < 0 and b > 0:
		return b - a
	else:
		return abs(a - b)

n = int(input())
cities = list(map(int, input().split()))
for i in range(len(cities)):
	if i == 0:
		mini = abs(cities[i+1] - cities[i])
		maxi = abs(cities[-1] - cities[i])
	elif i == len(cities) - 1:
		mini = abs(cities[i] - cities[i-1])
		maxi = abs(cities[i] - cities[0])
	else :
		mini = min(abs(cities[i+1] - cities[i]), abs(cities[i] - cities[i-1]))
		maxi = max(abs(cities[-1] - cities[i]), abs(cities[0] - cities[i]))
	print (str(mini) + ' ' + str(maxi))
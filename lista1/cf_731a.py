#Codeforces 731A
name = list(input())
wheel = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 
pos = 0
count = 0
middle = len(wheel)/2
for i in range(len(name)):
	ind = wheel.index(name[i])
	diff = max(ind, pos) - min(ind, pos)
	if diff < middle:
		count += diff
	else:
		count += len(wheel) - diff
	pos = ind

print(count)


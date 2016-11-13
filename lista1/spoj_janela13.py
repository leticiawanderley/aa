#Spoj JANELA13
windows = sorted(list(map(int, input().split())))
total_area = 60000
space = 0
position = 0
for i in range(len(windows)):
	if windows[i] < position:
		space += 200 - (position - windows[i])
	else:
		space += 200
	position = windows[i] + 200

print(total_area - (space*100))
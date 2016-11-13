
#Codeforces 625B
gogol = list(input())
pineapple = list(input())
lg = len(gogol)
lp = len(pineapple)
count = 0
for i in range(0, lg-lp+1):
	if gogol[i:i+lp] == pineapple:
		count += 1
		gogol[i+lp-1] = '#'

print(count)
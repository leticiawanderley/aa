#Codeforces 659A
numbers = list(map(int, input().split()))
n = numbers[0]
a = numbers[1]
b = numbers[2]
if b == 0:
	print(a)
else:
	print(((a-1+b)%n+n)%n+1)
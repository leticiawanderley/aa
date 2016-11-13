#Codeforces 722A
format = input()
time = list(input().split(':'))

if format == '12':
	if time[0] == '00':
		time[0] = '01'
	elif int(time[0]) > 12:
		r = '0'
		if int(time[0])%10 == 0:
			r = '1'
		time[0] = r + time[0][-1]
elif format == '24':
	if int(time[0]) > 23:
		time[0] = '1' + time[0][-1]

if int(time[1]) > 59:
		time[1] = '1' + time[1][-1]

print(time[0] + ":" + time[1])
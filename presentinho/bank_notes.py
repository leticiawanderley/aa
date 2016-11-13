#URI 1018
import math
bank_notes = [100, 50, 20, 10, 5, 2, 1]
value = int(input())
print(value)
notes = [0, 0, 0, 0, 0, 0, 0]
i = 7
while value > 0:
	notes[7 - i] += math.floor(value/bank_notes[7-i])
	value = value%bank_notes[7-i]
	i -=1

print(str(notes[0]) + " nota(s) de R$ 100,00\n"
+ str(notes[1]) + " nota(s) de R$ 50,00\n"
+ str(notes[2]) + " nota(s) de R$ 20,00\n"
+ str(notes[3]) + " nota(s) de R$ 10,00\n"
+ str(notes[4]) + " nota(s) de R$ 5,00\n"
+ str(notes[5]) + " nota(s) de R$ 2,00\n"
+ str(notes[6]) + " nota(s) de R$ 1,00")
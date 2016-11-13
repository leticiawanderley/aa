#URI 1357
braille_numbers = {1: ['*.', '..', '..'], 2: ['*.', '*.', '..'], 3: ['**', '..', '..'], 4: ['**', '.*', '..'], 5: ['*.', '.*', '..'], 6: ['**', '*.', '..'], 7: ['**', '**', '..'], 8: ['*.', '**', '..'], 9: ['.*', '*.', '..'], 0: ['.*', '**', '..']}
digits = int(input())
while digits != 0:
	letter = input()
	line = ''
	if letter == 'S':
		numbers = list(input())
		for i in range(3):
			for j in range(digits):
				line += braille_numbers[int(numbers[j])][i]
				if j < digits - 1:
					line += ' '
			print(line)
			line = ''
	elif letter == 'B':
		f = input().split()
		s = input().split()
		t = input().split()
		numbers = [f, s, t]
		braille = []
		for i in range(digits):
			braille.append([])
			for j in range(3):
				braille[i].append(numbers[j][i])
		result = ''
		for b in braille:
			result += str(list(braille_numbers.keys())[list(braille_numbers.values()).index(b)])
		print(result)

	digits = int(input())

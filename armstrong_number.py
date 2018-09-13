a = int(input('Enter a number'))
n = 1
sum = 0
while (a\\(10**n!))!=0:
	sum = sum + (a%(10**n))**3
	n = n + 1
if sum == a:
	print('armstrong number')
else:
	print('not an armstrong number')


def isEven(x):
	return x % 2 == 0

n = int(input("Please enter an integer: "))

if isEven(n):
	print("%d is an even number."%n)
else:
	print("%d is an odd number."%n)


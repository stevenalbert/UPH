from random import randint

def printList(l):
	for x in l:
		print(x, end=" ")
	print()

list = []

for i in range(100):
	list.append(randint(randint(1, 100), randint(1000, 10000)))

print("Original list of numbers:")
printList(list)

list.sort()

print("\nList of numbers in ascending order:")
printList(list)

list.reverse()

print("\nList of numbers in descending order:")
printList(list)

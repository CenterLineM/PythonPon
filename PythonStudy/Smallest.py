Smallest_so_far = None
print('Before')
for value in [9, 41, 12, 3, 15]:
	if Smallest_so_far is None:
		Smallest_so_far = value
	elif value < Smallest_so_far:
		Smallest_so_far = value
	print(Smallest_so_far,value)
print('After', Smallest_so_far)

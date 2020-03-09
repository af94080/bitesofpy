def sum_numbers(numbers=None):

	# case 1 sum_numbers([]) 
	# empty list should return zero

	if numbers is not None:
		if len(numbers) == 0:
			return 0

	# case 2 sum_numbers() 
	# no argument is provided, 
	# return sum of numbers 1..100.
	# 5050

	if not numbers:
		return sum(list(range(1,101)))

	# case 3 if there is a list add up the numbers
	#  eg [1,2,3,4] should give 10

	return sum(numbers)


# print(sum_numbers([]))
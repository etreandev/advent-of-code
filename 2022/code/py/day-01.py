# Day December 01, 2022

# Read lines
def readlines(file):
	with open(file) as handler:
		return [line.rstrip() for line in handler.readlines()]

# Star 1
def star1(lines):
	max_calories = 0
	cur_calories = 0
	for line in lines:
		if line != '':
			cur_calories += int( line ) 
		else:
			max_calories =  max(max_calories, cur_calories)
			cur_calories = 0
	return max_calories

# Star 2
def star2(lines):
	top_calories = [0, 0, 0, 0]
	cur_calories = 0

	for line in lines:
		if line != '':
			cur_calories += int( line )
		else:
			top_calories[3] = cur_calories
			top_calories.sort(reverse=True)
			cur_calories = 0
	return sum(top_calories[:3])

# Run in the command line
if __name__ == '__main__':
	# Read lines
	lines = readlines('C:\\Users\\andre\\training\\advent-of-code\\2022\\input\\day-01.txt')

	# Call star 1 function
	star1_solution = star1(lines)

	# Print output for star 1
	print(f"The result for star 1 problem is: {star1_solution}")

	# Call star 2 function
	star2_solution = star2(lines)

	# Print output for star 2
	print(f"The result for star 2 problem is: {star2_solution}")

	# Signal end
	print("Routine for day 01 ended successfully!")
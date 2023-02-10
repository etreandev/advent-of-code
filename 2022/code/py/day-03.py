# Day December 03, 2022

# Read lines
def readlines(file):
	with open(file) as handler:
		return [line.rstrip() for line in handler.readlines()]

# Auxiliar variables
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
priorities = dict()
niter = 1
for letter in letters:
	priorities[letter] = niter
	niter += 1

# Star 1
def star1(lines):
	prioritySum = 0
	for line in lines:
		compLen = len(line) // 2 
		compartment1 = set( line[:compLen] )
		compartment2 = set( line[compLen:] )
		commonItem   = list( compartment1.intersection(compartment2) )
		prioritySum += priorities[commonItem[0]]
		
	return prioritySum

# Star 2
def star2(lines):
	prioritySum = 0
	while len(lines) > 0:
		X = set( lines.pop(0) )
		Y = set( lines.pop(0) )
		Z = set( lines.pop(0) )

		badge = list(X.intersection(Y).intersection(Z))[0]
		prioritySum += priorities[badge]

	return prioritySum

# Run in the command line
if __name__ == '__main__':
	# Read lines
	lines = readlines('C:\\Users\\andre\\training\\advent-of-code\\2022\\input\\day-03.txt')
    
	# Call star 1 function
	star1_solution = star1(lines)

	# Print output for star 1
	print(f"The result for star 1 problem is: {star1_solution}")

	# Call star 2 function
	star2_solution = star2(lines)

	# Print output for star 2
	print(f"The result for star 2 problem is: {star2_solution}")

	# Signal end
	print("Routine for day 03 ended successfully!")
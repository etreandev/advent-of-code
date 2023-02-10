# Day December 02, 2022

# Read lines
def readlines(file):
	with open(file) as handler:
		return [line.rstrip() for line in handler.readlines()]

# Star 1
def star1(lines):
	opponentKey = {"A": 1, "B": 2, "C":3}
	myKey       = {"X": 1, "Y": 2, "Z":3}
	score       = 0
	for line in lines:
		match = line.split()
		opponentMove = opponentKey[match[0]]
		myMove       = myKey[match[1]]
		outcome      = myMove - opponentMove
		if outcome in [1, -2]: # I win
			score += myMove + 6
		elif outcome == 0:     # A draw
			score += myMove + 3
		else:                  # I lose
			score += myMove
	return score

# Star 2
def star2(lines):
	opponentKey = {"A": 1, "B": 2, "C":3}
	outcomes    = {"X": 0, "Y": 3, "Z":6}
	myMoves     = [3, 1, 2, 3, 1]
	score       = 0
	for line in lines:
		match = line.split()
		opponentMove = opponentKey[match[0]]
		outcome      = outcomes[match[1]]
		if outcome == 6:        # I win
			myMove = myMoves[opponentMove + 1]
		elif outcome == 3:     # A draw
			myMove = myMoves[opponentMove]
		else:                  # I lose
			myMove = myMoves[opponentMove - 1]

		score += outcome + myMove

	return score

# Run in the command line
if __name__ == '__main__':
	# Read lines
	lines = readlines('C:\\Users\\andre\\training\\advent-of-code\\2022\\input\\day-02.txt')

	# Call star 1 function
	star1_solution = star1(lines)

	# Print output for star 1
	print(f"The result for star 1 problem is: {star1_solution}")

	# Call star 2 function
	star2_solution = star2(lines)

	# Print output for star 2
	print(f"The result for star 2 problem is: {star2_solution}")

	# Signal end
	print("Routine for day 02 ended successfully!")
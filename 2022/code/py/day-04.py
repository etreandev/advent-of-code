# Day December 04, 2022

# Read lines
def readlines(file):
    with open(file) as handler:
        return [line.rstrip() for line in handler.readlines()]

# Star 1
def star1(lines):
    fully_contained = 0
    for line in lines:
        a, b = line.split(",")
        a_range = [int(section) for section in a.split("-")]
        b_range = [int(section) for section in b.split("-")]

        if (a_range[0] <= b_range[0]) and (b_range[1] <= a_range[1]):
            fully_contained += 1

        elif (b_range[0] <= a_range[0]) and (a_range[1] <= b_range[1]):
            fully_contained += 1

    return fully_contained

# Star 2
def star2(lines):
    overlaps = 0
    for line in lines:
        a, b = line.split(",")
        a_range = [int(section) for section in a.split("-")]
        b_range = [int(section) for section in b.split("-")]

        if (a_range[0] > b_range[1]) or (b_range[0] > a_range[1]):
            continue

        overlaps += 1

    return overlaps

# Run in the command line
if __name__ == '__main__':
    # Read lines
    lines = readlines('C:\\Users\\andre\\training\\advent-of-code\\2022\\input\\day-04.txt')

    # Call star 1 function
    star1_solution = star1(lines)

    # Print output for star 1
    print(f"The result for star 1 problem is: {star1_solution}")

    # Call star 2 function
    star2_solution = star2(lines)

    # Print output for star 2
    print(f"The result for star 2 problem is: {star2_solution}")

    # Signal end
    print("Routine for day 04 ended successfully!")
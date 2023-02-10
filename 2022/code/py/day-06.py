# Day December 06, 2022

# Read lines
def readlines(file):
    with open(file) as handler:
        return [line.rstrip() for line in handler.readlines()]

# Star 1
def star1(signal):
    first_packet_at = 1

    while len(signal) > 0:
        if len(list(set(signal[:4]))) == 4:
            return first_packet_at + 3
        else:
            first_packet_at += 1
            signal = signal[1:]


# Star 2
def star2(signal):
    first_packet_at = 1

    while len(signal) > 0:
        if len(list(set(signal[:14]))) == 14:
            return first_packet_at + 13
        else:
            first_packet_at += 1
            signal = signal[1:]



# Run in the command line
if __name__ == '__main__':
    # Read lines
    lines = readlines('C:\\Users\\andre\\training\\advent-of-code\\2022\\input\\day-06.txt')

    # Call star 1 function
    star1_solution = star1(lines[0])

    # Print output for star 1
    print(f"The result for star 1 problem is: {star1_solution}")

    # Call star 2 function
    star2_solution = star2(lines[0])

    # Print output for star 2
    print(f"The result for star 2 problem is: {star2_solution}")

    # Signal end
    print("Routine for day 06 ended successfully!")
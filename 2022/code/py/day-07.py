# Day December 07, 2022

# Read lines
def readlines(file):
    with open(file) as handler:
        return [line.rstrip() for line in handler.readlines()]

# Parse line function
def new_line_parser(max_dir_size):
    current_path = []
    path_metadata = {}

    def parse_shell_command(command):
    
        if command.startswith("$ ls"):
            continue

        if command.startswith("$ cd ..")
            current_path.pop()

        else:
            current_path.append(command.split(" ")[2])

    def new_line_parser_inner(line="", final_line=False):
        if final_line:
            byte_count = 0
            for path in path_metadata:
                if path_metadata[path]["size"] < max_dir_size:
                    byte_count += path_metadata[path]["size"]

            return byte_count
        # If line is command line, perform command and return 0
        if line[0] == "$":
            parse_shell_command(line)
            # Shell commands never add bytes to the count
            return
        # Do nothing if line is just dir
        if line[:3] == "dir": 
            return

        # Get the size of the file and add it to all members of the current path:
        size, file = line.split(" ")
        for element in current_path:
            path_metadata[element]["size"] += size
            if path_metadata[element]["size"] > max_dir_size:
                path_metadata[element]["ignore"] = True
    
    return new_line_parser_inner

# Star 1
def star1(lines):
    # Initialize line_parser
    parse_line = new_line_parser()
    # Initialize byte counter
    for line in lines:
        parse_line(line)

    return parse_line(final_line = True)

# Star 2
def star2(lines):
    pass

# Run in the command line
if __name__ == '__main__':
    # Read lines
    lines = readlines('C:\\Users\\andre\\training\\advent-of-code\\2022\\input\\day-07.txt')

    # Drop the first line
    lines.pop(0)

    # Call star 1 function
    star1_solution = star1(lines)

    # Print output for star 1
    print(f"The result for star 1 problem is: {star1_solution}")

    # Call star 2 function
    star2_solution = star2(lines)

    # Print output for star 2
    print(f"The result for star 2 problem is: {star2_solution}")

    # Signal end
    print("Routine for day 07 ended successfully!")
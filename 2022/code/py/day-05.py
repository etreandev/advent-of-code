# Day December 05, 2022

# Import modules
import re

# Read lines
def readlines(file):
    with open(file) as handler:
        return [line.rstrip() for line in handler.readlines()]

# Get initial conditions:
def get_instructions(lines, preamble):

    # Parse the initial configuration of crates
    def parse_crates(crate_lines):
        crate_config = {
             0: []
            ,1: []
            ,2: []
            ,3: []
            ,4: []
            ,5: []
            ,6: []
            ,7: []
            ,8: []
        }
        letter_positions = [
            1
            ,5
            ,9
            ,13
            ,17
            ,21
            ,25
            ,29
            ,33
        ]
        for crate_line in crate_lines:
            for crate, letter_pos in enumerate(letter_positions):
                try:
                    if crate_line[letter_pos] != " ":
                        crate_config[crate].append(crate_line[letter_pos])
                except Exception as E:
                    continue

        return crate_config

    # Interpret instructions
    def parse_instructions(instruction_lines):
        instructions = []
        for instruction_line in instruction_lines:
           inst = re.split(r"[a-z ]+", instruction_line) 
           instruction = [int(element) for element in inst[1:]]
           instructions.append(instruction)
        return instructions

    crate_lines = lines[:preamble - 1].copy()
    del lines[:preamble + 1]

    crate_config = parse_crates(crate_lines)
    instructions = parse_instructions(lines)
    return crate_config, instructions

# Move Crates:
def move_crates(crate_config, instruction, reverse_order=True):
    if reverse_order:
        for niter in range(instruction[0]):
            crate = crate_config[instruction[1]-1].pop() 
            crate_config[instruction[2]-1].append(crate)
    else:
        crates = crate_config[instruction[1]-1][-instruction[0]:].copy()    
        crate_config[instruction[2]-1].extend(crates)
        del crate_config[instruction[1]-1][-instruction[0]:]
    return crate_config    

# Get Top Letters
def get_top_letters(crate_config):
    top_letters = []
    for key in crate_config:
        top_letters.append(crate_config[key][-1] if len(crate_config[key]) > 0 else "")
    return "".join(top_letters)

# Star 1
def star1(lines):
    # Get initial conditions and movement Instructions
    crate_config, instructions = get_instructions(lines, 9) 

    # Compute changes to initial position
    for instruction in instructions:
        crate_config = move_crates(crate_config, instruction)

    # Return the letters at the top of the array
    return get_top_letters(crate_config)

# Star 2
def star2(lines):
    # Get initial conditions and movement Instructions
    crate_config, instructions = get_instructions(lines, 9) 

    # Compute changes to initial position
    for instruction in instructions:
        crate_config = move_crates(crate_config, instruction, reverse_order=False)

    # Return the letters at the top of the array
    return get_top_letters(crate_config)

# Run in the command line
if __name__ == '__main__':
    # Read lines
    lines = readlines('C:\\Users\\andre\\training\\advent-of-code\\2022\\input\\day-05.txt')

    # Call star 1 function
    star1_solution = star1(lines)

    # Print output for star 1
    print(f"The result for star 1 problem is: {star1_solution}")

    lines = readlines('C:\\Users\\andre\\training\\advent-of-code\\2022\\input\\day-05.txt')

    # Call star 2 function
    star2_solution = star2(lines)

    # Print output for star 2
    print(f"The result for star 2 problem is: {star2_solution}")

    # Signal end
    print("Routine for day 05 ended successfully!")
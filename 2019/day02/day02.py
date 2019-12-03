import copy

def add(instructions, pos_1, pos_2, pos_store):
    num_1 = instructions[pos_1]
    num_2 = instructions[pos_2]
    result = num_1 + num_2

    new_instructions = instructions
    new_instructions[pos_store] = result

    return new_instructions


def multiply(instructions, pos_1, pos_2, pos_store):
    num_1 = instructions[pos_1]
    num_2 = instructions[pos_2]
    result = num_1 * num_2

    new_instructions = instructions
    new_instructions[pos_store] = result

    return new_instructions


# https://stackoverflow.com/questions/434287/what-is-the-most-pythonic-way-to-iterate-over-a-list-in-chunks
def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))


def run_program(instructions):

    for group in chunker(instructions, 4):
        # print(group)

        if group[0] == 1:
            instructions = add(instructions, group[1], group[2], group[3])
        elif group[0] == 2:
            instructions = multiply(instructions, group[1], group[2], group[3])
        elif group[0] == 99:
            break
        else:
            print(f'ERROR: Unknown instruction: {group[0]}')
            break

    return instructions


def get_input():
    with open("input.txt", "r") as f:
        line = f.readline()
    line_as_array = [int(x) for x in line.split(',')]
    return line_as_array


def part_one():
    """
    Before running the program:
    - replace position 1 with the value 12 and
    - replace position 2 with the value 2

    What value is left at position 0 after the program halts?
    """

    instructions = get_input()

    instructions[1] = 12
    instructions[2] = 2

    final_state = run_program(instructions)
    print(final_state[0])


def part_two():
    """
    Before running the program:
    - position 1 is the noun - can be int from 0-99
    - position 2 is the verb - can be int from 0-99

    What what noun/verb combo produces 19690720 at position 0 when the program halts?
    """

    instructions = get_input()

    expected_output = 19690720

    for noun in range(0, 100):
        for verb in range(0, 100):
            test_instructions = copy.copy(instructions)
            test_instructions[1] = noun
            test_instructions[2] = verb
            # print(f'testing noun: {noun}, verb: {verb}')

            final_state = run_program(test_instructions)
            output = final_state[0]
            if output == expected_output:
                answer = 100 * noun + verb
                print(f'noun: {noun} --- verb: {verb} --- answer: {answer}')
                break


def main():
    part_one()
    part_two()


if __name__ == "__main__":
    main()

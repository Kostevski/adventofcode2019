from inputs import Day_2 as inp


def get_inp(x, y):
    _input = list(map(int, inp.split(",")))
    _input[1] = x
    _input[2] = y
    return _input


def comp(x, y):
    inpt = get_inp(x, y)

    for i in range(0, len(inpt), 4):
        opcode = inpt[i]
        if opcode == 1:
            inpt[inpt[i + 3]] = inpt[inpt[i + 1]] + inpt[inpt[i + 2]]
        elif opcode == 2:
            inpt[inpt[i + 3]] = inpt[inpt[i + 1]] * inpt[inpt[i + 2]]
        elif opcode == 99:
            return inpt[0]
        else:
            print("Something wrong")
            return inpt


def main():
    # Part 1
    print(f"PART 1: {comp(12, 2)}")
    # Part 2
    for i in range(100):
        for j in range(100):
            if comp(i, j) == 19690720:
                print(f"PART 2: {100 * i + j}")


if __name__ == "__main__":
    main()

from inputs import Day_3 as inp


mapping = {
    "R": ("x", 1),
    "L": ("x", -1),
    "U": ("y", 1),
    "D": ("y", -1),
}


def get_points():
    lsts = [inpt.split(",") for inpt in inp.split()]
    wires = []

    for wire in lsts:
        result = []
        coordinates = {
            "x": 0,
            "y": 0,
        }
        for coord in wire:
            target, const = mapping.get(coord[0])
            steps = int(coord[1:])

            for i in range(1, steps + 1):
                coordinates[target] += const
                result.append((coordinates["x"], coordinates["y"]))

        wires.append(result)
    return wires[0], wires[1]


def main():
    l1, l2 = get_points()
    intersection = set(l1).intersection(l2)

    minimum_part1 = min(map(lambda x: abs(x[0]) + abs(x[1]), intersection))
    print(f"PART 1: {minimum_part1}")

    minimum_part2 = min(map(lambda x: l1.index(x) + l2.index(x) + 2, intersection))
    print(f"PART 2: {minimum_part2}")


if __name__ == "__main__":
    main()

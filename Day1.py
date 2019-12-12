from inputs import Day_1 as inp


def fuel_recur(num):
    sm = num // 3 - 2
    if sm // 3 - 2 > 0:
        sm += fuel_recur(sm)
    return sm


def fuel(num):
    return num // 3 - 2


def main():
    inpt = list(map(int, inp.split()))
    sm_1 = sum(list(map(lambda x: fuel(x), inpt)))
    print(f"PART 1: {sm_1}")

    sm_2 = sum(list(map(lambda x: fuel_recur(x), inpt)))
    print(f"PART 1: {sm_2}")


if __name__ == "__main__":
    main()

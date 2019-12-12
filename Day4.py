from inputs import Day_4 as inp


def calculate():
    to, fr = map(int, inp.split("-"))

    num1 = 0
    num2 = 0
    for i in range(to, fr):
        string = str(i)
        repeats_1 = 0
        repeats_2 = 0
        is_pass = True
        for j in range(1, len(string)):
            if int(string[j]) < int(string[j - 1]):
                is_pass = False

            if string[j] == string[j - 1]:
                repeats_1 += 1

                try:
                    if string[j - 2] != string[j]:
                        try:
                            if string[j + 1] != string[j]:
                                repeats_2 += 1
                        except IndexError:
                            repeats_2 += 1
                except IndexError:
                    if string[j + 1] != string[j]:
                        repeats_2 += 1
        num1 += is_pass * (repeats_1 > 0)
        num2 += is_pass * (repeats_2 > 0)
    return num1, num2


def main():
    num1, num2 = calculate()
    print(f"PART 1: {num1}")
    print(f"PART 2: {num2}")


if __name__ == "__main__":
    main()

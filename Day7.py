from inputs import Day_7 as inp


class Intcode:

    def __init__(self):
        self.input = list(map(int, inp.split(",")))
        self.ptr = 0
        self.halt = False
        self.message = None
        self.run()

    def advance(self, steps):
        self.mode_1 = 0
        self.mode_2 = 0
        self.mode_3 = 0
        self.ptr += steps
        return self.ptr

    def error(self):
        raise Exception(f'Error at {self.ptr}')

    def run(self):
        self.advance(0)
        while self.halt is False:
            opcode = self.opcode()

            method = getattr(self, "op_" + str(opcode), self.error)
            method()

        return self.input

    def set_modes(self, opcode):
        self.mode_1 = opcode // 10 ** 2 % 10
        self.mode_2 = opcode // 10 ** 3 % 10
        self.mode_3 = opcode // 10 ** 4 % 10

    def opcode(self):
        opcode = self.input[self.ptr]

        if opcode < 100:
            return opcode

        else:
            self.set_modes(opcode)
            return int(str(opcode)[-2:])

    def op_1(self):
        term_1 = self.input[self.input[self.ptr + 1]] if self.mode_1 == 0 else self.input[self.ptr + 1]
        term_2 = self.input[self.input[self.ptr + 2]] if self.mode_2 == 0 else self.input[self.ptr + 2]

        self.input[self.input[self.ptr + 3]] = term_1 + term_2
        self.advance(4)

    def op_2(self):
        term_1 = self.input[self.input[self.ptr + 1]] if self.mode_1 == 0 else self.input[self.ptr + 1]
        term_2 = self.input[self.input[self.ptr + 2]] if self.mode_2 == 0 else self.input[self.ptr + 2]

        self.input[self.input[self.ptr + 3]] = term_1 * term_2
        self.advance(4)

    def op_3(self):
        inp = int(input("Specify input: \n"))
        self.input[self.input[self.ptr + 1]] = inp
        self.advance(2)

    def op_4(self):
        self.message = self.input[self.input[self.ptr + 1]]
        print(f"Output: {self.message}")
        self.advance(2)

    def op_5(self):
        cond = self.input[self.input[self.ptr + 1]] if self.mode_1 == 0 else self.input[self.ptr + 1]
        if cond != 0:
            self.ptr = self.input[self.input[self.ptr + 2]] if self.mode_2 == 0 else self.input[self.ptr + 2]
            self.advance(0)
        else:
            self.advance(3)

    def op_6(self):
        cond = self.input[self.input[self.ptr + 1]] if self.mode_1 == 0 else self.input[self.ptr + 1]
        if cond == 0:
            self.ptr = self.input[self.input[self.ptr + 2]] if self.mode_2 == 0 else self.input[self.ptr + 2]
            self.advance(0)
        else:
            self.advance(3)

    def op_7(self):
        val = self.input[self.input[self.ptr + 1]] if self.mode_1 == 0 else self.input[self.ptr + 1]
        cmp = self.input[self.input[self.ptr + 2]] if self.mode_2 == 0 else self.input[self.ptr + 2]
        if val < cmp:
            result = 1
        else:
            result = 0

        self.input[self.input[self.ptr + 3]] = result
        self.advance(4)

    def op_8(self):
        val = self.input[self.input[self.ptr + 1]] if self.mode_1 == 0 else self.input[self.ptr + 1]
        cmp = self.input[self.input[self.ptr + 2]] if self.mode_2 == 0 else self.input[self.ptr + 2]
        if val == cmp:
            result = 1
        else:
            result = 0

        self.input[self.input[self.ptr + 3]] = result
        self.advance(4)

    def op_99(self):
        print("Opcode 99, halting program")
        self.halt = True


def main():
    for i in range(5):
        Intcode()


if __name__ == "__main__":
    main()

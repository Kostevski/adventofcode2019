from inputs import Day_6 as inp

# inp = """COM)B
# B)C
# C)D
# D)E
# E)F
# B)G
# G)H
# D)I
# D)Z
# Z)Y
# Y)R
# E)J
# J)K
# K)L
# K)YOU
# I)SAN"""

class Tree:

    def __init__(self, name=None, parent=None):
        self.name = name
        self.parent = parent
        self.children = []

    def __str__(self):
        return f"{self.name} --> \n"

    def __repr__(self):
        return f"{self.name} --> \n"

    @property
    def is_terminal(self):
        return len(self.children) == 0

    def count(self, count=0):

        if not self.is_terminal:
            temp = count
            for child in self.children:
                temp += child.count(count + 1)
            count = temp
        return count

    def to_dest(self, dest, orbits=[]):
        if self.is_terminal:
            orbits = [self.name,] if self.name == dest else []
        else:

            for child in self.children:
                temp = []
                temp = child.to_dest(dest, orbits=[])
                if len(temp) > 0:
                    temp.append(self.name)
                    orbits += temp


        return orbits

    def move(self, origin, dest):

        orig = set(self.to_dest(origin)) # - 2
        dest = set(self.to_dest(dest, orbits=[])) # - 2
        import pdb;pdb.set_trace()
        diff = len(dest.difference(orig)) + len(orig.difference(dest)) - 2
        return diff


    def build(self, branches):
        cp = branches.copy()
        for name, branch in cp.items():
            if branch.parent == self.name:
                self.children.append(branches.pop(name)) if name in branches.keys() else None

        for child in self.children:
            child.build(branches)

def main():
    inpt = inp.split()
    branches = {}
    for orbit in inpt:
        parent, child = orbit.split(")")

        Child = Tree(name=child, parent=parent)
        branches.update({child: Child})

        if parent not in branches.keys():
            Parent = Tree(name=parent)
            branches.update({parent: Parent})

    root = branches.pop("COM")
    root.build(branches)
    print(f"PART 1: {root.count()}")
    print(f"PART 2: {root.move('YOU', 'SAN')}")

    return root


if __name__ == "__main__":
    main()

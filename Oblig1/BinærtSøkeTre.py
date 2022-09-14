import timeit
import fileinput


class BinærtSøkeTre:

    def __init__(self, element):
        # self.setliste = set([3, 4]) //Kanskje vi ikke skal bruke liste/set
        self.left = None
        self.right = None
        self.element = element
        self.length = 0
        # self.low = 0
        # self.high = list(self.setliste)[-1]

    def hentMinsteData(self, set):
        if set == None or set.left == None:
            return set
        return self.hentMinsteData(set.left)

    def contains(self, set, element):
        if set == None:
            return False
        if set.element == element:
            return True
        if element < set.element:
            return self.contains(set.left, element)
        if element > set.element:
            return self.contains(set.right, element)

        return False

    def insert(self, set, element):
        if set == None:
            set = BinærtSøkeTre(element)
            self.length += 1
        elif element < set.element:
            set.left = self.insert(set.left, element)

        elif element > set.element:
            set.right = self.insert(set.right, element)

        return set

    def remove(self, set, x):
        if set == None:
            return None
        if x < set.element:
            set.left = self.remove(set.left, x)
            self.length -= 1
        if x > set.element:
            set.right = self.remove(set.right, x)
            self.length -= 1
        if set.right == None:
            self.length -= 1
            return set.left
        if set.left == None:
            self.length -= 1
            return set.right
        u = self.hentMinsteData(set.right)
        set.element = u.element
        set.right = self.remove(set.right, u.element)
        self.length -= 1
        return set

    def size(self):
        print(self.length)
        # return self.length
        # teller = 1
        # if self.right != None:
        #     teller += self.right.size()
        # if self.left != None:
        #     teller += self.left.size()
        # # print(teller)
        # return teller


def hovedprogram():
    set = BinærtSøkeTre(1)
    # print(set)
    fil = open("input_100000.txt")
    # print(fil.readlines())
    antGanger = fil.readline()
    # print(antGanger)

    i = 0
    # print(set.setliste)
    # print()
    while i != int(antGanger):
        #inp = input("Velg mellom insert/contains/remove/size: ").split()
        inp = fil.readline().split()
        # print(fil.readline())

        if inp[0] == "insert":
            set.insert(set, int(inp[1]))
        elif inp[0] == "contains":
            print(set.contains(set, int(inp[1])))
        elif inp[0] == "remove":
            set.remove(set, int(inp[1]))
        elif inp[0] == "size":
            set.size()
        else:
            print("Du har skrevet feil!")
        i += 1


start = timeit.default_timer()
hovedprogram()
stop = timeit.default_timer()
print("Tid brukt: ", stop-start)

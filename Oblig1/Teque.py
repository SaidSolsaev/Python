

class Node:
    def __init__(self, x):
        self.x = x
        self.next = None
        self.prev = None


class Teque:
    def __init__(self):
        #self.teque = []
        self.start = Node(0)
        self.strl = 0

    def __str__(self):
        cur = self.start.next
        out = ""
        while cur:
            out += str(cur.x) + "-"
            cur = cur.next
        return out[:-1]

    def push_front(self, x):
        # Setter inn på starten i lista
        # for i in self.teque:
        node = Node(x)
        node.next = self.start.next
        self.start.next = node
        self.strl += 1

    def push_back(self, x):
        # Setter inn på bakers av lista
        nyNode = Node(x)
        siste = self.start
        while (siste.next != None):
            siste = siste.next
        siste.next = nyNode
        self.strl += 1

    def push_middle(self, x):
        # Setter inn i midten av lista, k=strls på lista. så (k+1)/2
        newNode = Node(x)
        nodeStart = self.start
        teller = (self.strl+1)/2

        if (self.strl % 2 == 0):
            teller = self.strl/2

        while (teller > 0):
            teller -= 1
            nodeStart = nodeStart.next
        newNode.next = nodeStart.next
        nodeStart.next = newNode
        self.strl += 1

    def get(self, i):
        tmpTeller = 0
        node = None
        tmpNode = self.start

        while (tmpNode != None):
            tmpNode = tmpNode.next
            if (tmpTeller == i):
                node = tmpNode
                break
            tmpTeller += 1
        return node.x

    # def pop(self):
    #     fjern = self.start.next
    #     self.start.next = self.start.next.next
    #     self.strl -= 1
    #     return fjern.x

    # def hentStrl(self):
    #     return self.strl

    # def erTom(self):
    #     return self.strl == 0


def main():
    teq = Teque()
    antGanger = input("Hvor mange ganger skal programmet kjøres: ")

    i = 0

    while i != int(antGanger):
        inp = input("push_back/push_front/push_middle/get: ").split()

        # print(fil.readline())

        if inp[0] == "push_back":
            teq.push_back(int(inp[1]))
        elif inp[0] == "push_front":
            teq.push_front(int(inp[1]))
        elif inp[0] == "push_middle":
            teq.push_middle(int(inp[1]))
        elif inp[0] == "get":
            teq.get(int(inp[1]))
        else:
            print("Du har skrevet feil!")
        print(f"Stack: {teq}")
        print(teq.strl)
        i += 1

    # stack = Teque()
    # for i in range(1, 11):
    #     stack.push_front(i)
    # print(f"Stack: {stack}")
    # # stack.push_back(19)
    # stack.push_middle(32)
    # stack.push_back(44)
    # stack.push_back(18)

    # print(f"Stack: {stack}")
    # print(stack.get(4))
    # for _ in range(1, 6):
    #     remove = stack.pop()
    #     print(f"Pop: {remove}")
    # print(f"Stack: {stack}")
    # stack.get(5)


main()

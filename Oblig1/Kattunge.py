class Katteunge:
    def main(self):
        self.st = input()
        self.ali = {}

        while(True):
            s = input()
            i = 1
            if(s == '-1'):
                break
            else:
                hassan = s.split(" ")
                to = hassan[0]
                while i < len(hassan):
                    self.ali[hassan[i]] = to
                    i += 1
                    print(len(hassan))
                    print(self.ali)
        self.mo(self, self.st)

    def mo(self, a):
        print(a, " ")
        if a in self.ali:
            # self.ali.get(self.st)
            self.mo(self, self.ali.get(a))


a = Katteunge

a.main(a)

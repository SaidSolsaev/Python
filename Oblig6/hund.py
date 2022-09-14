
class Hund:

    def __init__(self, alder, vekt, metthet = 10):
        self.alder = int(alder)
        self.vekt = int(vekt)
        self.metthet = int(metthet)
        
    def hentUtAlder(self):
        print("Alderen er:", self.alder)

    def hentUtVekt(self):
        print("Vekta er:", self.vekt, "kg")

    def hentUtMetthet(self):
        print("Mettheten til hunden er: ", self.metthet)

    def spring(self):
        self.metthet -= 1
        if self.metthet < 5:
            self.vekt -= 1
        else:
            pass

    def spis(self):
        self.metthet += 1
        if self.metthet > 7:
            self.vekt += 1
        else:
            pass
    
    def skrivUt(self):
        print("Mettheten til hunden er nå på: ", self.metthet)
        

    



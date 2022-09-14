#Klasse for motorsykkel som skal modellere kjøringen av motorsykkel.
#Et merke, regnr, kmstand.

class Motorsykkel:

    def __init__(self, merke, kmstand, regnr): #lager en konstruktør med merke, kmstand og regnr
        self.merke = merke
        self.kmstand = int(kmstand)
        self.regnr = regnr

    def kjør(self, km): #lager en metode for hver gang registrert kjøring vil det bli ny kmstand
        self.kmstand += km

    def hentKilometerstand(self): #returnerer kmstand
        return self.kmstand

    def skrivUt(self): #skriver ut merke, regnr og kmstand
        print(self.merke, "," ,self.regnr, "," ,self.kmstand)

    

    
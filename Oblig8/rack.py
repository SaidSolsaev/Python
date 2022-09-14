from node import Node


class Rack:
    # Opretter et rack med en liste som skal inneholde noder og med en parameter maks noder en liste kan ha
    def __init__(self, maksAntNoder):
        self._maksAntNoder = maksAntNoder
        self._liste = []

    #Metode som legger til noder i et rack/liste.
    def settInnNode(self, node):
        if len(self._liste) < self._maksAntNoder:# så lenge lengden til lista er minde enn det som er ført som maks noder vil ny node bli plassert i lista
            self._liste.append(node)
            return True

    def getAntNoder(self):  # Metode som returnerer hvor mange noder det er i racket
        return len(self._liste)

    # Metode som skal returnere antall prosessorer i nodene for et rack
    def antProsessorer(self):
        sumProsessorer = 0
        for node in self._liste:  # kjører en for løkke gjennom hele lista
            # bruker en metode som allerede er laget tidligere og kaller på den for å hente antall prosessor for noder i et rack
            pros = node.antProsessorer()
            sumProsessorer += pros
        return sumProsessorer

    # Metode som skal regne sammen alle nodene i racket som er over gitte maks grensa med minne
    def noderMedNokMinne(self, påkrevdMinne):
        noderMedNokMinne = 0
        for e in self._liste:  # for løkke med en if sjekk som sjekker om metoden nokMinne er True om den er true vil det si at den har funnet en node med over angitt grense for minne og da blir den telt.
            if e.nokMinne(påkrevdMinne) is True:
                noderMedNokMinne += 1
        return noderMedNokMinne

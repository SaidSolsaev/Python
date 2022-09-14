from node import Node
from rack import Rack


class Regneklynge:
    def __init__(self, noderPerRack):
        self._noderPerRack = noderPerRack
        self._rackListe = []

    def leggTilNode(self, node):  # Metode som skal legge til en node i en liste med racks dersom det er ledig plass om det fullt skal det lages et nytt rack
        ledigRack = False  # setter først et rack som fullt

        for rack in self._rackListe:  # lager en sjekk for å sjekke om det er plass i racket for å sette inn node
            if rack.settInnNode(node) is True:
                ledigRack = True  # om det er plass så vil det legges til i racket

        if ledigRack is False:  # om det ikke er plass vil det lages et nytt rack i lista med racks
            nyttRack = Rack(self._noderPerRack)
            nyttRack.settInnNode(node)
            self._rackListe.append(nyttRack)

    # metode som skal regne sammen alle prosessorer i hele lista med racks som inneholder noder
    def antProsessorer(self):
        antallPros = 0
        for pros in self._rackListe:
            antallPros += pros.antProsessorer()
        return antallPros

    # metode som skal regne sammen alle nodene med minne som er over maks gitt og skal returnere noder med nok minne
    def noderMedNokMinne(self, påkrevdMinne):
        nokMinne = 0
        for racks in self._rackListe:
            nokMinne += racks.noderMedNokMinne(påkrevdMinne)
        return nokMinne

    def antallRacks(self):  # metode som skal returnere hvor mange racks det er i hele klyngen
        return len(self._rackListe)

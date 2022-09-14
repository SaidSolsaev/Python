from regneklynge import Regneklynge
from node import Node


class Datasenter:

    def __init__(self):  # Lager en ordbok for regneklynger
        self._regneklynger = {}

    # Metode som skal lese regneklynger og legge de til i ordboka
    def lesInnRegneklynge(self, filnavn):
        filinnhold = open(filnavn).read()  # Åpner filen og leser innholdet

        # splitter linjer på linjeskiftet fordi
        linjer = filinnhold.strip().split("\n")
        # lagrer variabel noderPrRack som hvor mange noder et rack kan ha
        noderPrRack = int(linjer[0])

        # lager en ny regneklynge med maks noder for et rack
        nyReg = Regneklynge(noderPrRack)

        # For løkke som skal gå gjennom linje 2 i filen og lagre de forskjellige tingene som minne, prosessor
        for linje in linjer[1:]:
            maskin = linje.split(" ")
            antall = int(maskin[0])
            minne = int(maskin[1])
            prosessor = int(maskin[2])

            # for løkke som går gjennom lengden til hvor mange noder det er i maskinen og legger det inn i en Node
            for e in range(antall):
                node = Node(minne, prosessor)
                nyReg.leggTilNode(node)
        # Når alt er gjennom gått og maks noder for racket er fiksa vil regneklngen bli lagret i ordboken med filnavnet som key
        self._regneklynger[filnavn] = nyReg

    # metode som skal skrive ut alle regneklyngene i en liste

    def skrivUtAlleRegneklynger(self):
        for regneklynge in self._regneklynger:
            print("\n")
            self.skrivUtRegneklynge(regneklynge)

    # Metode som skirver ut regneklyngen vi vil at den skal skrive ut.
    def skrivUtRegneklynge(self, filnavn):
        regklynger = self._regneklynger[filnavn]
        navn = filnavn.split()
        navn = filnavn[:4]
        print(f"Informasjon om regneklyngen: {navn}")
        print(f"Antall rack: {regklynger.antallRacks()}")
        print(f"Antall prosessorer: {regklynger.antProsessorer()}")
        print(f"Noder med minst 32 GB: {regklynger.noderMedNokMinne(32)}")
        print(f"Noder med minst 64 GB: {regklynger.noderMedNokMinne(64)}")
        print(f"Noder med minst 128 GB: {regklynger.noderMedNokMinne(128)}")

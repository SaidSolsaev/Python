class Node:
    def __init__(self, minne, antPros):  # definerer minne og antall prossesorer en node skal ha
        self._minne = minne
        self._antPros = antPros

    def antProsessorer(self):  # metode som returnerer hvor mange prosessorer
        return self._antPros

    # metode for den noden har nok minne til det som kreves av et program
    def nokMinne(self, påkrevdMinne):
        if påkrevdMinne <= self._minne:
            # Hvis den har det returneres True hvis ikke så vil det automatisk bli false.
            return True

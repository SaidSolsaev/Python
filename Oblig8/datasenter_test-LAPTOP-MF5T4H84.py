from datasenter import Datasenter
# test for hele oppgaven!


def hovedprogram():
    datasenter = Datasenter()  # lager et datasenter
    datasenter.lesInnRegneklynge("abel.txt")  # leser inn begge filene
    datasenter.lesInnRegneklynge("saga.txt")
    datasenter.skrivUtAlleRegneklynger()  # skriver ut info om begge


hovedprogram()

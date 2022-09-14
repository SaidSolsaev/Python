def adder(tall1, tall2): #Lager en parameter 
    summen = tall1 + tall2
    print("Summen av de to tallene du har valgt er: ", summen)

adder(5, 4) #kaller på parameter med forskjellige tall
adder(9, 103)


def tellForekomst(minTekst, minBokstav):
    telle = 0
    for indeks in minTekst: #bruker en for loop for å telle hvor mange ganger en valgt bokstav er i en setning
        if indeks == minBokstav:
            telle += 1 #teller for hver gang bokstaven forekommer +1
    print("Bokstaven" , minBokstav, "forekommer", telle, "ganger i setningen,", minTekst)

setning = input("Skriv inn en setning her: ") #ber bruker om å skrive inn en setning
bokstav = input("Srkiv nå en bokstav: ")
tellForekomst(setning, bokstav) #kaller på funksjonen
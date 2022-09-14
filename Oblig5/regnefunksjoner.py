#oppg 1)
def addisjon(tall1, tall2): #skriver en funksjon som adderer to tall med parrametere
    return tall1 + tall2 #Returnerer tallet

sum = int(addisjon(8, 10))
print("summen av de to tallene er", sum) #Srkiver ut prosedyren

#Oppg 2
def subtrasksjon(tall1, tall2):
    return tall1 - tall2
assert subtrasksjon(7, 4) == 3 #assert kommer til å stopp programmet om disse tre assertene er feil
assert subtrasksjon(10, -3) == 13 #både her og på divisjon bruker jeg tre forskjellige assert for å kontrollere at koden over er skrevet sånn at den gjør det jeg ber den om
assert subtrasksjon(-10, -10) == 0

def divisjon(tall1, tall2):
    return tall1/tall2
assert divisjon(10, -2) == -5
assert divisjon(-10, -2) == 5
assert divisjon(100, 20) == 5


#Oppg 3
def tommerTilCm(antallTommer):
    assert antallTommer > 0, "Antall tommer var mindre enn 0" #Bruker assert for å sjekke at tommer er større enn 0
    return antallTommer * 2.54 #Returnerer verdien i cm
cm = float(tommerTilCm(6))
print("I cm er det", cm) #Skriver ut prosedyren

#Oppg 4a&b
def skrivBeregninger(): # lager en prosedyre. inni her henter jeg de andre prosedyrene jeg lagde for å addere, subtrhaere osv.
    print("Utregninger: ")
    første_tall = float(input("Skriv inn tall 1: "))
    andre_tall = float(input("Skriv inn tall 2: ")) #Ber bruker legge inn to tall
    addert = addisjon(første_tall, andre_tall) #henter fra tidligere prosedyre og legger inn tall fra bruker
    print("\n" "Resultat av summering:", addert)
    subtrahert = subtrasksjon(første_tall, andre_tall)
    print("Resultat av subtraksjon", subtrahert)
    dividert = divisjon(første_tall, andre_tall)
    print("Resultat av divisjon:", dividert)
    print("\n" "Konvertering fra tommer til cm: ")
    tommer_tall = float(input("Skriv inn et tall: "))
    tommer = tommerTilCm(tommer_tall)
    print("Resultat:", tommer)

skrivBeregninger()

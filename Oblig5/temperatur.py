#Oppg1)
f = open("max_temperatures_per_month.csv", "r")

def temperatur_ordbok(filnavn):
    ordbok = {}
    for linje in f:
        kolonner = linje.split(",")
        nøkkel = kolonner[0]
        verdi = float(kolonner[1])
        ordbok[nøkkel]=verdi
    return ordbok
skriv_ut = temperatur_ordbok("max_temperatures_per_month.csv")
print(skriv_ut)


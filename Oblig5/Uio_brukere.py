#Oppg 1)
def lagBrukernavn(navn):
    navn_etternavn = navn.lower().split()
    brukernavn = navn_etternavn[0] + navn_etternavn[1][0]
    return brukernavn

#brukernavn = lagBrukernavn(input("Skriv ditt fulle navn her: "))
#print(brukernavn)

#Oppg 2)
def lagEpost(brukernavn, epost):
    epostListe = {}
    epostListe[brukernavn] = epost
    return brukernavn + "@" + epost
    
#epost = lagEpost(input("Skriv ditt brukernavn her: "), input("Skiv din epost suffix: "))
#print(epost)

#Oppg 3)
def skrivUtEposter(ordbok):
    for e in ordbok:
        lagEpost(e, ordbok[e])
        return e + ordbok[e]
SkrivUt = skrivUtEposter({"olan":"ifi.uio.no", "karin":"student.matnat.uio.no"})
print(SkrivUt)
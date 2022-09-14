#Oppg 1)
def returner_bokstaver(): # Lager en funskjon
    skriv_ord = input("Skriv et ord her: ") #Ber bruker om å skrive inn et ord
    return print("Det er", len(skriv_ord), "bokstaver i dette ordet.") #Printer ut lengden på ordet (antall bokstaver)

#returner_bokstaver()

#Oppg 2)
def returner_ordbok():
    skriv_setning = input("Skriv en setning her: ")
    ord = skriv_setning.split()
    telle = 0
    for antall_ganger in skriv_setning.split():
        if antall_ganger == antall_ganger:
            telle += 1
    print(telle)
    

returner_ordbok()
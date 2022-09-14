inp = int(input("Du skal nå gjette et tall fra 0-100. Skriv tallet her: "))
liste = []

if inp == 0:
    print("Du klarte det")
liste.append(inp)

while inp != 0: #bruker en while loop og if test helt til bruker skriver 0 skal den kjøre
    if inp != 0:
        print("feil prøv på nytt")
        inp = int(input("Gjett nytt tall: "))
    if inp == 0:
        print("Du klarte det")
    liste.append(inp) #lagrer hvert tall bruker skriver inn og legger inn i lista
print("Dette er alle tallene du gjetta:", liste)

minSum = 0

for tall in liste: #Bruker en for løkke for å gå inn for hvert tall og plusse på alle
    minSum += tall

print("Summen av tallene i lista er:", minSum) #Skriver ut summen


største_tall = liste[0] #For løkke for å finne det største tallet
for tall in liste:
    if tall > største_tall:
        største_tall = tall
print("Dette er det største tallet i lista:", største_tall)

minste_tall = liste[0]
for tall in liste:
    if tall < minste_tall:
        minste_tall = tall
print("Dette er det minste tallet i lista:", minste_tall)
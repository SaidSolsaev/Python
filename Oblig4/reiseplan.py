steder = [] #lager tre tomme lister
klesplagg = []
avreisedato = []


for x in range(0, 5): #bruker for-løkke med range fra 0-5 sånn at de kan sette inn 5 elementer. gjør dette 3 ganger
    inp = input("Legg til sted du vil reise: ")
    steder.append(inp) #legger til det bruker skriver inn i lista
print(steder)


for x in range(0, 5):
    inp = input("Legg til klesplagg: ")
    klesplagg.append(inp)
print(klesplagg)

for x in range(0, 5):
    inp = input("Legg til avreisedatoer: ")
    avreisedato.append(inp)
print(avreisedato)

reiseplan = [steder, avreisedato, klesplagg] #legger alt i en nøstet liste

print(reiseplan[0][1])

for e in reiseplan: #skriver ut tre lister for hver 
    print(e)


liste_indeks1 = int(input("Skriv inn et tall mellom 0 og 2: ")) #ber bruker om å taste et tall mellom 0 og 2

if liste_indeks1 < 0 and liste_indeks1 > 2: #om tallet er mindre enn 0 eller større enn 2 da skal det printes ut feil
    print("Du har tastet ugyldig tall.")

liste_indeks2 = int(input("Nå skriv et tall mellom 0 og 4: "))

if liste_indeks2 < 0 and liste_indeks2 > 4:
    print("Du har tastet ugyldig tall.")
    
print(reiseplan[liste_indeks1][liste_indeks2]) #printer ut det som står i indeksen bruker har tastet inn.

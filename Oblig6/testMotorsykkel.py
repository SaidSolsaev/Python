from motorsykkel import Motorsykkel #importerer Motorsykkel fra motorsykkel.py filen

def hovedprogram():
    sykkel1 = Motorsykkel("Yamaha", 3100, "DR25123") #legger inn tre msykler med sine "verdier"
    sykkel2 = Motorsykkel("BMW", 2122, "AB12312")
    sykkel3 = Motorsykkel("Ducati", 2000, "AC22442")
    
    sykkel1.skrivUt() #skriver ut alle tre syklene sine "verdier"
    sykkel2.skrivUt()
    sykkel3.skrivUt()

    sykkel3.kjør(10) #siste sykkel har kjørt 10km
    henteKm = sykkel3.hentKilometerstand() #skriver ut den nye kmstanden til sykkel3
    print("Sykkel 3 sin nye kilometerstand er:", henteKm, "km")

hovedprogram()
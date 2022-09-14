from hund import Hund

def hovedprogram():
    hund1 = Hund(int(input("Hvor gammel er hunden: ")), int(input("Hvor mye veier hunden: ")))
    hund1.hentUtAlder(), hund1.hentUtVekt(), hund1.hentUtMetthet()
    
    hund1.spring(), hund1.spring(), hund1.spring(), hund1.spring(), hund1.spring(), hund1.spring()
    print("Hunden har nå løpt \nog vekta til hunden er nå:", hund1.vekt, "kg"), hund1.skrivUt()
    
    hund1.spis(), hund1.spis(), hund1.spis(), hund1.spis()
    print("Hunden har nå spist \nog vekta til hunden etter spist er:", hund1.vekt, "kg"), hund1.skrivUt()

hovedprogram()
from dato import Dato

def hovedprogram():
    dato = Dato(15, 3, 2020)
    
    år = dato.lesÅr()
    print(f"Året er: {år}")

    if dato.sjekkDato(15):
        print("Lønningsdag")
    elif dato.sjekkDato(1):
        print("Ny måned nye muligheter")
    
    streng = str(dato.returnerStr())
    print(f"Datoen idag er: {streng}")
    

hovedprogram()
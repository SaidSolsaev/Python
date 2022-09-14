
class Dato:
    def __init__(self, nyDag, nyMåned, nyttÅr):
        self.nyDag = int(nyDag)
        self.nyMåned = int(nyMåned)
        self.nyttÅr = int(nyttÅr)
    
    def lesÅr(self,):
        return self.nyttÅr
    
    def returnerStr(self):
        return f"{self.nyDag}.{self.nyMåned}.{self.nyttÅr}"
    
    def sjekkDato(self, nyDag):
        if self.nyDag == nyDag:
            return True
        else:
            return False

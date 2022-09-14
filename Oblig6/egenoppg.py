#Egen oppgave om en skole som skal finne gjennomsnitts karakter i et fag.
#lage et system for skolen som inneholder navn, alder og karakter for studenter.
#også lag en klasse for et fag/time de har på skolen der konstruktør skal inneholde navn og maks antall studenter som kan delta
#og finn gjennomsnittskarakteren for elevene

class Student:
    def __init__(self, navn, alder, karakter):
        self.navn = navn
        self.alder = int(alder)
        self.karakter = float(karakter)  # 1 - 6 karakter skala

    def få_karakter(self):
        return self.karakter

class Time:
    def __init__(self, navn, max_studenter):
        self.navn = navn
        self.max_studenter = max_studenter
        self.studenter = [] #lager en liste av studentene

    def leggTil_student(self, student):
        if len(self.studenter) < self.max_studenter:
            self.studenter.append(student)
            return True
        return False #hvis det ikke er plass til å legge til fler studenter i lista returner False

    def gjennomsnitt_karakter(self):
        sum = 0
        for student in self.studenter: #lager en for løkke for hver student i studenter lista skal den legge sammen karakterene.
            sum += student.få_karakter()
        
        return sum/len(self.studenter) #regner ut gjennomsnitt karakter for elevene ved å dele på lengden til lista studenter.

def hovedprogram():
    student1 = Student("Tim", 19, 5)
    student2 = Student("Ali", 19, 3)
    student3 = Student("Said", 18, 6)

    time = Time("Programmering", 2)
    time.leggTil_student(student1)
    time.leggTil_student(student2)
    print(time.leggTil_student(student3)) #returnerer False siden maks antall jeg har satt inn er 2 studenter i faget

    print(time.studenter[1].navn, "har som karakter", time.studenter[1].karakter, "og han er", time.studenter[1].alder)
    print(time.studenter[0].navn, "har som karakter", time.studenter[0].karakter, "og han er", time.studenter[0].alder)

    print("Gjennomsnitt karakteren for faget programmering er:", time.gjennomsnitt_karakter())

hovedprogram()
#Oppgaven handler om å la bruker skrive inn så mange venner de vil og deres bursdag ved å bruke while løkke. Og bruke en ordbok til å sette opp når hver venn har bursdag
#Bruk en for løkke for å skrive ut hver venn og deres bursdag.
venner_bursdag = {}

spørsmål = "ja" #Så lenge dette spm er ja vil while løkken kjøre
while spørsmål == "ja":
    navn = input("Hva heter vennen du vil legge til i bursdagslista: ")
    bursdag = input("Når har han bursdag: ")
    venner_bursdag[navn] = bursdag # legger inn bursdagen og navnet i ordboka
    spørsmål = input("Vil du legge til fler personer: ").lower() #spør om de vil legge til fler, while løkken slutter å kjøre om de skriver noe annet enn "ja"

for navn in venner_bursdag: #bruker en for løkke for å skrive ut når vennene har bursdag.
    print(navn, "har bursdag den", venner_bursdag[navn])
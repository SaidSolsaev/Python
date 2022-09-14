#Et enkelt spill

import turtle #Importerer fra "Turtle"

win = turtle.Screen() #Åpner en fane
win.title("Pong by Said Solsaev") #Gir vinduet et navn
win.bgcolor("black") #bakgrunns farge til vinduet
win.setup(width=800, height=600) #Bestemmer høyde og bredde til vinduet
win.tracer(0) #stopper vinduet til å oppdatere, gjør spillet raskere

# Poeng
poeng_a = 0
poeng_b = 0

#Brett A
brett_a = turtle.Turtle() #objektet brett
brett_a.speed(0) #setter farten i maks
brett_a.shape("square") #formen på brettet
brett_a.color("white") #farge
brett_a.shapesize(stretch_wid=5, stretch_len=1) #hvor lang og høy brettet skal være
brett_a.penup()
brett_a.goto(-350, 0) #plasserer firkanta brettet, på venstre side (koordinater)

#Brett B
brett_b = turtle.Turtle() #objektet brett
brett_b.speed(0) #setter farten i maks
brett_b.shape("square") #formen på brettet
brett_b.color("white") #farge
brett_b.shapesize(stretch_wid=5, stretch_len=1) #hvor lang og høy brettet skal være
brett_b.penup()
brett_b.goto(350, 0) #plasserer firkanta brettet, på høyre side (koordinater)

#Ball
ball = turtle.Turtle() #objektet brett
ball.speed(0) #setter farten i maks
ball.shape("circle") #formen på brettet
ball.color("white") #farge
ball.penup()
ball.goto(0, 0) #plasserering (koordinater)
ball.dx = 0.2 #farten på ballen i x kordinater, hver gang ballen beveger seg er det i 0.3 piksler
ball.dy = -0.2 #samme i y kordniat

# Pen
pen = turtle.Turtle() #lager en poengtavle
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Spiller A:0   Spiller B:0 ", align="center", font=("Courier", 24, "normal"))


#Funksjoner
def brett_a_opp():
    y = brett_a.ycor() #returnerer y-kordinat
    y += 30 #plusser på 30 piksler på y kordinatet fordi opp plusser på i y-kordinatet og ned er minus
    brett_a.sety(y) #plasserer brettet på den nye plassen

def brett_a_ned():
    y = brett_a.ycor() #returnerer y-kordinat
    y -= 30 #minus 30 piksler på y kordinatet fordi opp plusser på i y-kordinatet og ned er minus
    brett_a.sety(y) #plasserer brettet på den nye plassen

def brett_b_opp():
    y = brett_b.ycor() #returnerer y-kordinat
    y += 30 #plusser på 30 piksler på y kordinatet fordi opp plusser på i y-kordinatet og ned er minus
    brett_b.sety(y) #plasserer brettet på den nye plassen

def brett_b_ned():
    y = brett_b.ycor() #returnerer y-kordinat
    y -= 30 #minus 30 piksler på y kordinatet fordi opp plusser på i y-kordinatet og ned er minus
    brett_b.sety(y) #plasserer brettet på den nye plassen


# Keybord binding
win.listen() #får vinduet til å gjøre det keybordet sier
win.onkeypress(brett_a_opp, "w") #når man trykker på "w" går brettet a opp
win.onkeypress(brett_a_ned, "s") #når man trykker "s" går den ned
win.onkeypress(brett_b_opp, "Up") # Høyre side opp
win.onkeypress(brett_b_ned, "Down") #Høyre side ned


#Main game loop
while True:
    win.update() #hver gang man kjører loop oppdaterer spillet

    # Ball bevegelse
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Spill map check
    if ball.ycor() > 290: #siden hele vinduet er 600 er den y kordinatet oppe 300 og nede er -300, men husk ballen er 20*20 også derfor 290
        ball.sety(290)
        ball.dy *= -1 #bytter om plassen til ballen sånn at når den treffer toppen vil den reversere
    
    if ball.ycor() < -290: #siden hele vinduet er 600 er den y kordinatet oppe 300 og nede er -300, men husk ballen er 20*20 også derfor 290
        ball.sety(-290)
        ball.dy *= -1 #bytter om plassen til ballen sånn at når den treffer toppen vil den reversere

    if ball.xcor() > 390:
        ball.goto(0, 0) #om ballen går ut på sidene vil vi putte den i midten igjen
        ball.dx *= -1
        poeng_a += 1
        pen.clear()
        pen.write("Spiller A: {}  Spiller B: {}".format(poeng_a, poeng_b), align="center", font=("Courier", 24, "normal"))
    
    if ball.xcor() < -390:
        ball.goto(0, 0) #om ballen går ut på sidene vil vi putte den i midten igjen
        ball.dx *= -1
        poeng_b += 1
        pen.clear()
        pen.write("Spiller A: {}  Spiller B: {}".format(poeng_a, poeng_b), align="center", font=("Courier", 24, "normal"))
    
    # Når ballen treffer brettet
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < brett_b.ycor() + 40 and ball.ycor() > brett_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < brett_a.ycor() + 40 and ball.ycor() > brett_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1

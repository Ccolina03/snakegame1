from turtle import Turtle

STARTINGPOSITIONS=[(0, 0), (-20, 0), (-40, 0)]
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:
    def __init__(self,):
        self.wholesnake=[]
        self.creationstart()#this is to state this is a method of the class
        self.head=self.wholesnake[0]
    def creationstart(self):
        for position in STARTINGPOSITIONS:  # repeats three times because there is three things in the list and start with the first item , then continues with the second after finishing the loop
            self.add_segment(position)  #will do the for loop and check the position list in order

    def add_segment(self,position): #why position here because later on you want to indicate the exact position where you wanna do this function.
        options = Turtle()
        options.shape("square")
        options.color("green")
        options.penup()
        options.goto(position)
        self.wholesnake.append(options)  # appending to

    def extend(self):
        self.add_segment(self.wholesnake[-1].position()) #Calling the function to add a block more to the position of the last block in the list of wholesnake(which represents the tail).In other words, number 2.
        #turtle.position() gives you the coordinates of a specific object you are looking for

    def move(self):
        for segnum in range(len(self.wholesnake) - 1, 0, -1):  # This means: start=2, stop=0, step=-1. Osea step seria la logica va de 2 despues a 1porque el step es -1. No va al cero porque el range es (2,0) so el 0 no seria tocado
            # si sustraes -2 al len la cola osea EL 2 se quedaria atras y nunca avanzaria.
            # como la cola de la serpiente es 2 y la punta 0. Queremos que la cola se vuelva el medio, el medio la cabeza y la cabeza avanze 20
            newcoordx = self.wholesnake[segnum - 1].xcor()  # aca primero tomamos las coordenadas del medio
            newcoordy = self.wholesnake[segnum - 1].ycor()  # aca primero tomamos la coordenada del medio
            self.wholesnake[segnum].goto(newcoordx, newcoordy)  # y como la cola es 2 y queremos avanzar para adelante vamos a tomar las coordenadas del de medio. Y asi sucesivamente. Recuerdo que -1 en una lista se va para el final de una lista asi que como es 0, 1, 2 . cuando el bloque 0 osea la cabeza esta buscando donde ir este ira a dond
            # CUANDO ACABA EL FOR LOOP EL 2 Y 1 estan en la COORDENADA DEL 0.

        self.head.forward(20)  # aqui para hacer avanza por 1 a la serpiente y asi tengo nuevas coordenadas del 0 que es la cabeza
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading()!= LEFT:
            self.head.setheading(RIGHT)

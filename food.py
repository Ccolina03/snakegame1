from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()  #valores de turtle son iplementados a Food
        self.shape("circle")  #asi de esta forma puedo llamar los atributos y methods de turtle
        self.penup()  #recuerda misma linea que EL SUPER.
        self.color("blue")
        self.shapesize(0.5,0.5) #stretch length, width
        self.speed("fastest")
        self.movement() #calling the method to do this without actually calling it
    def movement(self):
        xrandom=random.randint(-280,280)
        yrandom=random.randint(-280,280)
        self.goto(xrandom,yrandom)
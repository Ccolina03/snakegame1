from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.superscore=0
        self.penup()
        self.goto(0, 270)  # moves the written part to above
        self.increase()

    def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Arial", 30, "normal"))

    def increase(self):
        self.clear()
        self.color("white") #to make the text white
        self.hideturtle()  #this will hide the cursor or the turtle when you want to write a text.
        self.write(f"Score: {self.superscore}", align="center",font=("Arial",20,"normal")) #COULD STATE ALIGNMENT AND FONT AS CONSTANTS ABOVE
        self.superscore += 1


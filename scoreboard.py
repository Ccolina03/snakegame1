from turtle import Turtle

class Scoreboard(Turtle):  #ScoreBoard properties

    def __init__(self):
        super().__init__()
        self.superscore=-1 #score will start 0 since it increases after increase() is called
        with open("textito.txt") as file:
            self.high_score=int(file.read())  #Here it indicates the first highest score as 0 first and saves it.
        self.penup()
        self.goto(0, 270)  # moves the written part to above
        self.increase()
    def update_scoreboard(self): #score will update itself
        self.clear()
        self.write(f"Score: {self.superscore} Highest score: {self.high_score}", align="center",
                   font=("Arial", 20, "normal"))  # COULD STATE ALIGNMENT AND FONT AS CONSTANTS ABOVE
    def highest(self):
        if self.superscore>self.high_score:
            self.high_score=self.superscore
            with open("textito.txt", mode="w") as file:  #Here the highest possible score will update itself and will be saved in the text file.
                file.write(f"{self.high_score}")
        self.superscore=0
        self.update_scoreboard()

    def increase(self): #score will increase every time the function is called and will update in screen
        self.color("white")
        self.superscore += 1
        self.update_scoreboard()



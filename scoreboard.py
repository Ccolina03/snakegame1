from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.superscore=-1
        with open("textito.txt") as file:
            self.high_score=int(file.read())  #AQUI INDICA AL high score como 0 primero y lo guarda como esa variable
        self.penup()
        self.goto(0, 270)  # moves the written part to above
        self.increase()
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.superscore} Highest score: {self.high_score}", align="center",
                   font=("Arial", 20, "normal"))  # COULD STATE ALIGNMENT AND FONT AS CONSTANTS ABOVE
    def highest(self):
        if self.superscore>self.high_score:
            self.high_score=self.superscore
            with open("textito.txt", mode="w") as file:  #aqui al ocurrir esto. el self.high_score se reactualizara para cambiar lo que habia antes con la nueva variable. Y a partir de replicara el resultado hasta que acabe el juego.
                file.write(f"{self.high_score}")
        self.superscore=0
        self.update_scoreboard()

    # def gameover(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align="center", font=("Arial", 30, "normal"))

    def increase(self):
        self.color("white")
        self.superscore += 1
        self.update_scoreboard()



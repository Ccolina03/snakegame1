from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen= Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")   #background color of window
screen.tracer(0)  #necessary for it to be off/the screen is not going to show off whatever we do to until we update it
screen.title("My Snake Game")

snake1=Snake() #first define the object and then state when will it be activated
food1=Food()  #food appears in the screen for the first time
scoreboard1=Scoreboard()

screen.listen()
screen.onkey(snake1.up ,"Up")  #here you will activate the method of snake 1 when you press the key up
screen.onkey(snake1.down, "Down")
screen.onkey(snake1.right, "Right")
screen.onkey(snake1.left, "Left")



gameison=True
while gameison:
    screen.update() #makes the 3 blocks move in one step
    time.sleep(0.15)
    snake1.move()
    #Detect collision with food
    if snake1.head.distance(food1)<15:  #if the distance between the head of snake 1 object with the random located food is less than 15 pixels then there is a collision
        food1.movement() #this method will happen if collision occurs
        #remember when you first named object food1 was when you first initialized the
        scoreboard1.increase()
        snake1.extend() #extends the length of the snake every timew

    #Detect collision with wall

    if snake1.head.xcor()>280 or snake1.head.xcor()<-280 or snake1.head.ycor()>280 or snake1.head.ycor()<-280:
        scoreboard1.highest()
        snake1.reset()  #the scoreboard has the same attributes but when it touches the wall, it appears the score and the new messages terminating the loop

    #Detect collision with tail
    for partofthebody in snake1.wholesnake[1:]: #the foor loop check for each item in the list of snake1 (so each object created)
        if snake1.head.distance(partofthebody)<10:  #if distance between head and part of the body is less than 10 pixels you lost.
            scoreboard1.highest()
            snake1.reset()

screen.exitonclick()


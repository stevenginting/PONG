from turtle import Turtle , Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Papan
import time

screen = Screen()
screen.setup(height = 600, width=800)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.tracer(0)

kanan_Turtle = Paddle((350, 0))
kiri_Turtle = Paddle((-350 , 0))
bola = Ball()
papan = Papan()

screen.listen()
screen.onkey(kanan_Turtle.Up , "Up")
screen.onkey(kanan_Turtle.Down , "Down")
screen.onkey(kiri_Turtle.Up , "w")
screen.onkey(kiri_Turtle.Down , "s")

game_is_on = True
while game_is_on:
    time.sleep(bola.kecepatan)
    screen.update()
    bola.move()
    
    if bola.xcor() > 280 or bola.ycor() < -280:
        bola.pantul_y()        
    #Set dan kiri posisi
    if bola.xcor() > 380:
        bola.setposisi()
        papan.kiri_point()
    #Set posisi dan Xcor
    if bola.xcor() < -380:
        bola.setposisi()
        papan.kanan_point()
#DIstance
    if bola.distance(kanan_Turtle) < 50 and bola.xcor() > 340 or bola.distance(kiri_Turtle) < 50 and bola.ycor() > -340:
        bola.pantul_x()
        print("Hello World")

screen.exitonclick()
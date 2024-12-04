from turtle import Turtle

class Paddle(Turtle , ):
    def __init__(self , position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1,  stretch_wid=5)
        self.penup()
        self.goto(position)
    
    def Up(self):
        kor_y = self.ycor() + 20
        self.goto(self.xcor() , kor_y)    

    

    def Down(self):
        kor_y =self.ycor() - 20
        self.goto(self.xcor() , kor_y)
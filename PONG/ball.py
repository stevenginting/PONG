from turtle import Turtle

class Ball(Turtle):
    def __init__(self, ):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.gerak_x = + 10
        self.gerak_y = + 10
        self.kecepatan = 0.1

    def move(self):
        x_cor = self.xcor() + self.gerak_x
        y_cor = self.ycor() + self.gerak_y
        self.goto(x_cor , y_cor)
    
    def setposisi(self):
        self.goto(0,0)
        self.pantul_x()

    def pantul_y(self):
        self.gerak_y *= -1
        self.kecepatan *= 0.9

    def pantul_x(self):
        self.gerak_x *= -1
        self.kecepatan *= 0.9

    # def tambah_kecepatan(self):
    #     self.kecepatan *= 2
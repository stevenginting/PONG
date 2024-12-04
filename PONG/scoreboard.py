from turtle import Turtle

class Papan(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.kananscore = 0
        self.kiriscore = 0

    def update_papan(self):
            self.clear()
            self.goto(-100 , 200)
            self.write(self.kananscore , align="center" , font=("italic", 80 , "normal"))
            self.goto(100 , 200)
            self.write(self.kiriscore , align="center" , font=("italic", 80 , "normal"))
        
    def kiri_point(self):
         self.kiriscore +=1
         self.update_papan()
    
    def kanan_point(self):
         self.kananscore +=1
         self.update_papan()
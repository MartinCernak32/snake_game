from turtle import Turtle
with open('data.txt', 'r') as file:
    content = file.read()
try:
    highscore = int(content)
except:
    print("ERROR")


class Scoreboard(Turtle):
    
    def __init__(self):
       super().__init__()
       self.highscore = highscore
       self.score = 0
       self.goto(0,270)
       self.color("white")
       self.hideturtle()
       self.update_points()
       
       
    def update_points(self):
        self.clear()
        self.write(f"Your score is: {self.score} High Score: {self.highscore}", False, align='center', font=('Arial', 15, 'normal'))
         
              
    def add_points(self):
        self.score = self.score + 1
        self.clear()
        self.write(f"Your score is: {self.score}", False, align='center', font=('Arial', 15, 'normal'))
    
    #def game_over(self):
        #self.goto(0, 0)
        #self.write("GAME OVER", False, align='center', font=('Arial', 15, 'normal'))
    
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open('data.txt', 'w') as file:
                file.write(str(self.score))
                          
        self.score = 0
        self.update_points()
    

           
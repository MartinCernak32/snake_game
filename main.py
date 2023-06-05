from turtle import Screen, write
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
WALL = 280





screen = Screen()
screen.colormode(255)
screen.title("My snake game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)



snake = Snake()
food = Food()
score = Scoreboard() 
screen.update()    
            
screen.listen()      
screen.onkey(key="w", fun=snake.move_up)
screen.onkey(key="d", fun=snake.move_right)
screen.onkey(key="a", fun=snake.move_left)
screen.onkey(key="s", fun=snake.move_down) 

game_is_on = True
while game_is_on:
    
    screen.update()
    time.sleep(0.1)
    snake.move()
    score.update_points()
    # Detect when you collect food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.add_points()        
        snake.extend()
        time.sleep(0.1)
        screen.update()
   
    
    

    #Detect colision with wall
    if (snake.segments[0]).xcor() > WALL or (snake.segments[0]).xcor() < -WALL:    
        snake.hide_snake()
        score.reset()
        snake.reset()
        score.update_points()

    elif (snake.segments[0]).ycor() > WALL or (snake.segments[0]).ycor() < -WALL:
        snake.hide_snake()
        score.reset()
        snake.reset()
        score.update_points()

    
    #detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()

  
  
screen.exitonclick()


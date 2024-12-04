import turtle
import time
import random

postpone = 0.1

#Window Configuration; 
window = turtle.Screen()
window.title("SNAKE GAME - Elias D. Franco")
window.bgcolor("aquamarine")
window.setup(width = 600, height = 600)
window.tracer(0)

#Snake Head;
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.penup()
head.goto(0,0)
head.direction = "stop"
head.color=("white")

#Food Creation
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.penup()
food.goto(0,100)
food.color=("red")

#Segmets | Body of the snake;
segmet = turtle.Turtle()



#Funtions
def up():
     head.direction = "up"

def down():
     head.direction = "down"
 
def left():
     head.direction = "left"

def right():
     head.direction = "right"
 
 
def movement():
    if head.direction == "up":
         y = head.ycor()
         head.sety(y + 20)

    if head.direction == "down":
         y = head.ycor()
         head.sety(y - 20)

    if head.direction == "left":
         x = head.xcor()
         head.setx(x - 20)

    if head.direction == "right":
         x = head.xcor()
         head.setx(x + 20)

#Keyboard Settings
window.listen()
window.onkeypress(up, "Up")
window.onkeypress(down, "Down")
window.onkeypress(left, "Left")
window.onkeypress(right, "Right")

while True:
    window.update()
    if head.distance(food) < 20:
         x = random.randint(-280,280)
         y = random.randint(-280,280)
         food.goto(x,y)

         new_segment = turtle.Turtle()
         new_segment.speed(0)
         new_segment.shape("square")
         new_segment.penup()
         new_segment.color=("grey")
    
    movement()
    time.sleep(postpone)


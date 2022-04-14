import turtle as tur  
import time  
import random as rdm  

#Constants
delay = 0.1  
score = 0  
high_score = 0  

#Create game window  
win = tur.Screen()  
win.title("A Simple Snake Game")  
win.bgcolor("black")   
win.setup(width = 750, height = 750)
win.tracer(0)  
   
   
#Create the head of the snake  
head = tur.Turtle()  
head.shape("square")  
head.color("white")  
head.penup()  
head.goto(0, 0)  
head.direction = "Stop"  
   
   
#Create food
food = tur.Turtle()  
colors = rdm.choice(['pink', 'yellow', 'blue'])  
shapes = rdm.choice(['triangle', 'square', 'circle'])  
food.speed(0)  
food.shape(shapes)  
food.color(colors)  
food.penup()  
food.goto(0, 100)  

#Gameplay keys   
def move():  
    if head.direction == "up":  
        y = head.ycor()  
        head.sety(y + 23)  
    if head.direction == "down":  
        y = head.ycor()  
        head.sety(y - 23)  
    if head.direction == "left":  
        x = head.xcor()  
        head.setx(x - 23)  
    if head.direction == "right":  
        x = head.xcor()  
        head.setx(x + 23)  
   
def go_up():  
    if head.direction != "down":  
        head.direction = "up"  
def go_down():  
    if head.direction != "up":  
        head.direction = "down"  
def go_right():  
    if head.direction != "left":  
        head.direction = "right"    
def go_left():  
    if head.direction != "right":  
        head.direction = "left"  
        
win.listen()  
win.onkeypress(go_up, "w")  
win.onkeypress(go_down, "s")  
win.onkeypress(go_left, "a")  
win.onkeypress(go_right, "d")  
  
objects = []  

#Text
pen = tur.Turtle()  
pen.speed(0)  
pen.shape("square")  
pen.color("white")  
pen.penup()  
pen.hideturtle()  
pen.goto(0, 320)
pen.write("A simple snake game:", align = "center",  
          font = ("Consoles", 18, "bold"))
pen.goto(0, 280)
pen.write("Up - w, Down - s, Left - a, Right - d", align = "center",  
          font = ("Consoles", 18, "bold"))

#Main code
while True:  
    win.update()

    #if end of window reached - restart
    if head.xcor() > 340 or head.xcor() < -340 or head.ycor() > 340 or head.ycor() < -340:  
        time.sleep(1)  
        head.goto(0, 0)  
        head.direction = "Stop"  
        colors = rdm.choice(['pink', 'blue', 'yellow'])  
        shapes = rdm.choice(['square', 'triangle'])  
        for object1 in objects:  
            object1.goto(1050, 1050)  
        objects.clear()  
        score = 0  
        delay = 0.1  
        pen.clear()  
        pen.write("High Score: {} ".format(  
            high_score), align = "center", font = ("Consoles", 18, "bold"))  
    if head.distance(food) < 20:  
        x = rdm.randint(-250, 250)  
        y = rdm.randint(-250, 250)  
        food.goto(x, y)  
   
        #Add tail
        new_object1 = tur.Turtle()  
        new_object1.speed(0)  
        new_object1.shape("square")
        #tail color
        new_object1.color("green")  
        new_object1.penup()  
        objects.append(new_object1)
        #increase speed for every point gained
        delay -= 0.0001  
        score += 1
        #replace high score with score if higher
        if score > high_score:  
            high_score = score  
        pen.clear()  
        pen.write("Score : {}".format(  
            score), align = "center", font = ("Consoles", 18, "bold"))  
    #Check if the snake eats itself  
    for index in range(len(objects)-1, 0, -1):  
        x = objects[index - 1].xcor()  
        y = objects[index - 1].ycor()  
        objects[index].goto(x, y)  
    if len(objects) > 0:  
        x = head.xcor()  
        y = head.ycor()  
        objects[0].goto(x, y)  
    move()
    #randomize food
    for object1 in objects:  
        if object1.distance(head) < 20:  
            time.sleep(1)  
            head.goto(0, 0)  
            head.direction = "stop"  
            colors = rdm.choice(['pink', 'blue', 'yellow', 'red', 'orange', 'cyan'])  
            shapes = rdm.choice(['square', 'triangle', 'circle', 'rectangle'])  
            for object1 in objects:  
                object1.goto(1050, 1050)  
            object1.clear()  
   
            score = 0  
            delay = 0.1  
            pen.clear()  
            pen.write("High Score: {} ".format(  
                high_score), align = "center", font = ("Consoles", 18, "bold"))  
    time.sleep(delay)  
   
win.mainloop()

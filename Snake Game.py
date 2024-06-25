#Import Modules


import turtle
import time
import random


#Define Control Functions


def moveRight():
    global direction
    if direction !='l':
        direction='r'
def moveUp():
    global direction
    if direction != 'd':
        direction='u'
def moveDown():
    global direction
    if direction != 'u':
        direction='d'
def moveLeft():
    global direction
    if direction != 'r':
        direction='l'


#Create Screen and Turtle and Border


wn=turtle.Screen()
wn.setup(height=600, width=600)
wn.tracer(0)

t=turtle.Turtle()
t.shape("square")
t.penup()
t.speed(1)

t.goto(-300,300)
t.pendown()

count=0
while count<4:

    t.forward(600)
    t.right(90)
    count+=1
t.penup()
t.goto(0,0)
t.speed(1)


#Create a random food and obstacle genrator


food=turtle.Turtle()
food.shape('square')
food.penup()
food.color('red')

x=20*(random.randint(-14,14))
y=20*(random.randint(-14,14))
food.goto(x,y)

obs=0
obstacle=[]

while obs < 5:
    ob=turtle.Turtle()
    ob.shape('square')
    ob.color('gray')
    ob.penup()
    a=20*(random.randint(-14,14))
    b=20*(random.randint(-14,14))
    ob.goto(a,b)
    obstacle.append([a,b])
    obs=obs+1
print(obstacle)


#Main Game


snake=[t]

wn.listen()

wn.onkeypress(moveRight,"Right")
wn.onkeypress(moveUp,"Up")
wn.onkeypress(moveDown,"Down")
wn.onkeypress(moveLeft,"Left")


rand=random.randint(0,3)
if rand==0:
    direction = 'r'
elif rand==1:
    direction = 'u'
elif rand==2:
    direction = 'l'
elif rand==3:
    direction = 'd'
    


stop=False

while not stop:
    wn.update()
    time.sleep(0.1)
    
    #catching food and regenerating food if it gets generated on snake or on any obstacle

    
    if t.xcor() == food.xcor() and t.ycor() == food .ycor():
        
        x=20*(random.randint(-14,14))
        y=20*(random.randint(-14,14))
        a=len(snake)-1
        while a>0:
            if [x,y] == [snake[a].xcor() , snake[a].ycor()]:
                x=20*(random.randint(-14,14))
                y=20*(random.randint(-14,14))
                print("Food got generated on snake body")
            a=a-1

            while [x,y] in obstacle:
                print("Food got generated on obstacle")
                x=20*(random.randint(-14,14))
                y=20*(random.randint(-14,14))
            
        food.goto(x,y)
            
        p=turtle.Turtle()
        p.shape('square')
        p.penup()
        snake.append(p)
        
    #moving pieces

        
    i=len(snake)-1
    while i>0:
        snake[i].goto(snake[i-1].xcor(),snake[i-1].ycor())
        i=i-1
        
        
    #moving head

        
    if direction == 'r':
        t.goto(t.xcor()+20,t.ycor())
        if t.xcor()>280:
            t.goto(-280,t.ycor())
    elif direction == 'u':
        t.goto(t.xcor(),t.ycor()+20)
        if t.ycor()>280:
            t.goto(t.xcor(),-280)
    elif direction == 'l':
        t.goto(t.xcor()-20,t.ycor())
        if t.xcor()<-280:
            t.goto(280,t.ycor())
    elif direction == 'd':
        t.goto(t.xcor(),t.ycor()-20)
        if t.ycor()<-280:
            t.goto(t.xcor(),280)
            

    #Game over if head collides with body?

            
    i=len(snake)-1
    while i>0:
        if t.xcor()==snake[i].xcor() and t.ycor() == snake[i].ycor():
            print("GAME OVER!!!!! Snake collision with itself")
            stop=True
            break
        i=i-1
        

    #collision with obstacle

    
    if [t.xcor(),t.ycor()]in obstacle:
        print("GAME OVER!!!!! Snake collision with obstacle")
        stop=True
        break





   

        

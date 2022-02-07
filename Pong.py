import turtle

wn = turtle.Screen()
wn.title("Pong by JediBoro")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)

#Paddles
#Paddle One
paddle_one = turtle.Turtle()
paddle_one.speed(0)
paddle_one.shape("square")
paddle_one.color("white")
paddle_one.shapesize(stretch_wid=5,stretch_len=1)
paddle_one.penup()
paddle_one.goto(-350,0)

#Paddle Two
paddle_two = turtle.Turtle()
paddle_two.shape("square")
paddle_two.color("white")
paddle_two.shapesize(stretch_wid=5,stretch_len=1)
paddle_two.penup()
paddle_two.goto(+350,0)

#Paddle Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.1
ball.dy = -0.1

# Score
p1score = 0
p2score = 0
scoreTable = turtle.Turtle
scoreTable.speed(0)
scoreTable.goto(0,0)

# Function
def paddle_one_up():
    y = paddle_one.ycor()
    y+=20
    if y < 250 :
        paddle_one.sety(y)
        
def paddle_one_down():
    y = paddle_one.ycor()
    y-=20
    if y > -250:
        paddle_one.sety(y)

def paddle_two_up():
    y = paddle_two.ycor()
    y+=20
    if y < 250 :
        paddle_two.sety(y)
        
def paddle_two_down():
    y = paddle_two.ycor()
    y-=20
    if y > -250:
        paddle_two.sety(y)

# Keyboard Input
wn.listen()
wn.onkeypress(paddle_one_up, "w")
wn.onkeypress(paddle_one_down,"s")
wn.onkeypress(paddle_two_up, "8")
wn.onkeypress(paddle_two_down,"2")    
 
# MAIN
while True:
    wn.update()
    ball.setx(ball.xcor()-ball.dx)
    ball.sety(ball.ycor()-ball.dy)
    
    #Border Check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        
    #Hit and miss
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_two.ycor() +40 and ball.ycor() > paddle_two.ycor() -40):
        ball.setx(340)
        p2score += 1
        ball.dx *= -1
                
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_one.ycor() +40 and ball.ycor() > paddle_one.ycor() -40):
        ball.setx(-340)  
        p1score +=1
        ball.dx *= -1
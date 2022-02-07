import turtle

wn = turtle.Screen()
wn.title("Pong by JediBoro")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)


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
paddle_two.speed(0)
paddle_two.shape("square")
paddle_two.color("white")
paddle_two.shapesize(stretch_wid=5,stretch_len=1)
paddle_two.penup()
paddle_two.goto(+350,0)

#Paddle Ball
Ball = turtle.Turtle()
Ball.speed(0)
Ball.shape("square")
Ball.color("white")
Ball.penup()
Ball.goto(0,0)
Ball.dx = 0.1
Ball.dy = 0.1

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
    bxm = Ball.setx(Ball.xcor()-Ball.dx)
    bym = Ball.sety(Ball.ycor()-Ball.dy)
    #Border Check
    
    
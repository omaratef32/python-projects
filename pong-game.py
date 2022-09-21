import turtle

wind = turtle.Screen()
wind.title("pong game")
wind.setup(width=800, height=500)
wind.bgcolor("black")
wind.tracer(0)


##___(OBJECTIVS)___##

# PAD 1
pad1 = turtle.Turtle()
pad1.speed(0)
pad1.penup()
pad1.color("blue")
pad1.shape("square")
pad1.shapesize(stretch_wid=5, stretch_len=1)
pad1.goto(-380, 0)

# PAD 2
pad2 = turtle.Turtle()
pad2.speed(0)
pad2.penup()
pad2.color("red")
pad2.shape("square")
pad2.shapesize(stretch_wid=5, stretch_len=1)
pad2.goto(370, 0)

# BALL
ball = turtle.Turtle()
ball.speed(0)
ball.color("white")
ball.shape("square")
ball.penup()
ball.goto(0, 0)
ball.dx = 4
ball.dy = 4

# SCORE
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, -220)
score.write("player one 0 \t\t\t\t player two 0", align="center", font=("Courier", 16, "normal"))


##___(PADS MOVEMENT)___##

# funcions

def pad1_up():
    y = pad1.ycor()
    y += 40
    pad1.sety(y)

def pad1_down():
    y = pad1.ycor()
    y -= 40
    pad1.sety(y)

def pad2_up():
    y = pad2.ycor()
    y += 40
    pad2.sety(y)

def pad2_down():
    y = pad2.ycor()
    y -= 40
    pad2.sety(y)


# keyboard bingins 

wind.listen()
wind.onkeypress(pad1_up, "w")
wind.onkeypress(pad1_down, "s")
wind.onkeypress(pad2_up, "Up")
wind.onkeypress(pad2_down, "Down")

##___(MAIN LOOP)___##
import time

_tick2_frame=0
_tick2_fps=20000000 # real raw FPS
_tick2_t0=time.time()

def tick(fps=60):
    global _tick2_frame,_tick2_fps,_tick2_t0
    n=_tick2_fps/fps
    _tick2_frame+=n
    while n>0: n-=1
    if time.time()-_tick2_t0>1:
        _tick2_t0=time.time()
        _tick2_fps=_tick2_frame
        _tick2_frame=0

while True:
    tick(60)
    wind.update()

    #_(BALL MOVMENT)_#

    ball.sety(ball.ycor() + ball.dy)
    ball.setx(ball.xcor() + ball.dx)


    # up and down wall

    if ball.ycor() > 240:
        ball.sety(240)
        ball.dy *= -1
    
    if ball.ycor() < -240:
        ball.sety(-240)
        ball.dy *= -1


    # right and left wall

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score1 += 1
        score.clear()
        score.write(f"player one {score1} \t\t\t\t player two {score2}", align="center", font=("Courier", 16, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write(f"player one {score1} \t\t\t\t player two {score2}", align="center", font=("Courier", 16, "normal"))


    # BALL AND PAD COLLISION

    if ball.xcor() > 350 and ball.xcor() < 360 and ball.ycor() < pad2.ycor() + 40 and ball.ycor() > pad2.ycor() - 40:
        ball.setx(350)
        ball.dx *= -1
    
    if ball.xcor() < -360 and ball.xcor() > -370 and ball.ycor() < pad1.ycor() + 40 and ball.ycor() > pad1.ycor() - 40:
        ball.setx(-360)
        ball.dx *= -1

    if score1 == 10 or score2 == 10:
        break
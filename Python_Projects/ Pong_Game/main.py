import turtle as t

playerAScore = 0
playerBScore = 0

#------------------------------------------------------------------------------------
# Set up the screen
window = t.Screen()
window.title("Pong Game")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)  # Turns off the screen updates

#------------------------------------------------------------------------------------
# Creating Left Paddle A
leftPaddle = t.Turtle() 
leftPaddle.speed(0)  #This sets the speed of the turtle to the maximum
leftPaddle.shape("square")
leftPaddle.color("white")
leftPaddle.shapesize(stretch_wid=6, stretch_len=1)
leftPaddle.penup()
leftPaddle.goto(-350, 0)  # Positioning the paddle on the left side of the screen


# Creating Right Paddle B
rightPaddle = t.Turtle()
rightPaddle.speed(0)
rightPaddle.shape("square")
rightPaddle.color("white")
rightPaddle.shapesize(stretch_wid=6, stretch_len=1)
rightPaddle.penup()
rightPaddle.goto(350, 0)  # Positioning the paddle on the right side of the screen


# Creating the Ball
ball = t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)  # Positioning the ball at the center of the screen
ballxdirection = 0.9 # Ball movement speed
ballydirection = 0.9 # Ball movement speed

# Creating pen for scorecard update
pen = t.Turtle()
pen.speed(0)
#pen.color("blue")
pen.color("#f1c40f")  # golden score
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
#pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))
pen.write("score", align="center", font=("Arial", 24, "normal"))

#------------------------------------------------------------------------------------
# Function to move the left paddle Up
def leftPaddleUp():
    y = leftPaddle.ycor()
    if y < 250:  # prevent going off top
        y = y + 90
        leftPaddle.sety(y)

# Function to move the left paddle Down
def leftPaddleDown():
    y = leftPaddle.ycor()
    if y > -250:  # prevent going off bottom
        y = y - 90
        leftPaddle.sety(y)

# Function to move the right paddle Up
def rightPaddleUp():
    y = rightPaddle.ycor()
    if y < 250:  # prevent going off top
        y = y + 90
        rightPaddle.sety(y)

# Function to move the right paddle Down
def rightPaddleDown():
    y = rightPaddle.ycor()
    if y > -250:  # prevent going off bottom
        y = y - 90
        rightPaddle.sety(y)


#------------------------------------------------------------------------------------
# Assign keys to play
window.listen()
window.onkeypress(leftPaddleUp, "w")  # Press 'w' to move left paddle up
window.onkeypress(leftPaddleDown, "s")  # Press 's' to move left paddle down
window.onkeypress(rightPaddleUp, "Up")  # Press 'Up' arrow to move right paddle up
window.onkeypress(rightPaddleDown, "Down")  # Press 'Down' arrow to move right paddle down


#------------------------------------------------------------------------------------# Main game loop
while True:
    window.update()  # Update the screen

    #Moving the ball
    ball.setx(ball.xcor() + ballxdirection)
    ball.sety(ball.ycor() + ballydirection)

    #SetingUp the border
    if ball.ycor() > 290:
        ball.sety(290)
        ballydirection *= -1
        #ballydirection = ballydirection * -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ballydirection *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ballxdirection *= -1
        playerAScore += 1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(playerAScore, playerBScore), align="center", font=("Arial", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ballxdirection *= -1
        playerBScore += 1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(playerAScore, playerBScore), align="center", font=("Arial", 24, "normal"))

    # Paddle and ball collision
    if (340 < ball.xcor() < 350) and (rightPaddle.ycor() - 40 < ball.ycor() < rightPaddle.ycor() + 40):
        ball.setx(340)
        ballxdirection *= -1
    if (-350 < ball.xcor() < -340) and (leftPaddle.ycor() - 40 < ball.ycor() < leftPaddle.ycor() + 40):
        ball.setx(-340)
        ballxdirection *= -1



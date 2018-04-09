from Paddle import Paddle
from Ball import Ball
from Score import Score

def setup():
    size(800,600)
    global paddleLeft, paddleRight, ball, scoreRed, scoreBlue, paddlespeed
    paddle_width = 30
    paddle_height = 100
    radius = 15
    paddlespeed = 17
    
    paddleLeft = Paddle(50, height/2-paddle_height/2, paddle_width, paddle_height, color(255,0,0)) # left paddle, red
    paddleRight = Paddle(width-50-paddle_width, height/2-paddle_height/2, paddle_width, paddle_height, color(0,0,255)) # right paddle, blue
    
    ball = Ball(width/2, height/2-radius, radius, color(255,128,0))
    scoreRed = Score(0,width/2 - 50, 50, color(255,0,0)) #score left side
    scoreBlue = Score(0,width/2 + 50, 50, color(0,0,255)) # score right side
   
## Key input
def keyPressed():
    if key == CODED:
        if keyCode == UP:
                paddleRight.yspd = -paddlespeed
        if keyCode == DOWN:
                paddleRight.yspd = paddlespeed
    else:
        if (key == 'w' or key == 'W'):
            paddleLeft.yspd = -paddlespeed
        if (key == 's' or key == 'S'):
            paddleLeft.yspd = paddlespeed

def keyReleased():
    if key == CODED:
        if keyCode == UP:
                paddleRight.yspd = 0
        if keyCode == DOWN:
                paddleRight.yspd = 0
    else:
        if (key == 'w' or key == 'W'):
            paddleLeft.yspd = 0
        if (key == 's' or key == 'S'):
            paddleLeft.yspd = 0

def draw():
    ##Add score and reset ball
    if(ball.x+ball.r>=width):
        scoreRed.addPoint(1)
        ball.reset()
    if(ball.x-ball.r<=0):
        scoreBlue.addPoint(1)
        ball.reset()
    
    ##Collision
    if ((ball.y - (ball.r/2) > paddleRight.y) and (ball.y + (ball.r/2) < paddleRight.y+paddleRight.h) and (ball.x + (ball.r/2) > paddleRight.x)):
        ball.xspd *= -1
    if ((ball.y - (ball.r/2) > paddleLeft.y) and (ball.y + (ball.r/2)< paddleLeft.y+paddleLeft.h) and (ball.x - (ball.r/2) < paddleLeft.x+paddleLeft.w)):
        ball.xspd *= -1
    
    #draw
    background(color(255, 255, 255))
    paddleLeft.display()
    paddleRight.display()
    ball.display()
    
    #update
    paddleLeft.move(paddlespeed)
    paddleRight.move(paddlespeed)
    ball.move()
    
    #draw score
    scoreRed.display()
    scoreBlue.display()

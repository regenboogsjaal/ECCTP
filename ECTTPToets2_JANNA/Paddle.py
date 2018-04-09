class Paddle(object):

    def __init__(self,x,y,w,h,c):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.c = c
        self.yspd = 0
        
    def move(self, paddlespeed):
        if ((self.yspd == -paddlespeed)and(self.y-paddlespeed <= 0)):
            self.yspd = 0
        elif ((self.yspd == paddlespeed)and(self.y+paddlespeed+self.h >= height)):
            self.yspd = 0
        self.y += self.yspd
        
    def display(self):
        fill(self.c)
        rect(self.x,self.y,self.w,self.h)

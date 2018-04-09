class Ball(object):

    def __init__(self,x,y,r,c):
        self.x = x
        self.startx = x
        self.y = y
        self.starty = y
        self.r = r
        self.c = c
        self.yspd = 7
        self.xspd = 5
        
    def display(self):
        fill(self.c)
        ellipse(self.x,self.y,self.r*2,self.r*2)
        
    def move(self):
        self.x += self.xspd
        self.y += self.yspd
        
        if((self.y+self.r>=height)or(self.y-self.r<=0)):
            self.yspd *= -1
    
    def reset(self):
        self.x = self.startx
        self.y = self.starty

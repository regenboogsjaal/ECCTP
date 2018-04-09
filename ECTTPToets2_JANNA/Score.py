class Score(object):
    
    def __init__(self,startpoints,x,y,c):
        self.points = startpoints
        self.x = x
        self.y = y
        self.c = c

    def addPoint(self,value):
        self.points += value
        
    def display(self):
        textSize(30);
        fill(self.c)
        text(self.points,self.x,self.y)

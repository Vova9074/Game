x,y = 1000,1000
dim=50
x1=x/2
y1=900
dy=0
speed=15
platform=[]
class Platform(object):
    def __init__(self,fill_colorr,fill_colorb,fill_colorg, xpos, ypos):
        self.fill_colorr = fill_colorr
        self.fill_colorb = fill_colorb
        self.fill_colorg = fill_colorg
        self.xpos = xpos
        self.ypos = ypos
    def draw(self):
        fill(self.fill_colorr,self.fill_colorb,self.fill_colorg)
        square(self.xpos, self.ypos, 50)
for i in range(15):
    Pi=Platform(random(0,255),random(0,255),random(0,255), random(10,1450), random(10,950))
    platform.append(Pi)
def setup():
    global x,y
    size(1500,1000)
    background(255,0,0)
    frameRate(100)
def keyPressed():
    global x1,speed
    if key == 'a':
        x1=x1-speed
    if key == 'd':
        x1=x1+speed
def keyReleased():
    global dy
    if key == ' ' and -0.5< dy < 0.5:
        dy=dy-12

def draw():
    background(255,0,0)
    global dim,y1,x1,dy,Pi
    dy=dy+0.2
    if y1+dy > height-dim/2 :
        dy=-0.5*dy
    y1=y1+dy
    if y > height:
        dy=dy*-1
    if x1<-dim/2:
        x1=width-dim/2
    if x1>width+dim/2:
        x1=dim/2
    fill(0,0,0)
    ellipse(x1,y1,dim,dim)
    if y1-dim/2<0:
        x1=random(60,1450)
        y1=950
        dy=0
        for i in range(15): 
            platform.pop(i)
            for i in range(15):
                Pi=Platform(random(0,255),random(0,255),random(0,255), random(10,1450), random(10,950))
                platform.append(Pi)
    for i in range(15):
        platform[i].draw()
        if x1 > platform[i].xpos-dim/2 and x1< platform[i].xpos+dim/2+50 and y1 > platform[i].ypos-dim/2 and y1<platform[i].ypos+50+dim/2:
            dy=-0.2
            x1=x1
            if y1>platform[i].ypos+40:
                dy=1
            if x1 > platform[i].xpos and y1> platform[i].ypos:
                x1=x1+speed
            if x1 < platform[i].xpos+50 and y1> platform[i].ypos:
                x1=x1-speed

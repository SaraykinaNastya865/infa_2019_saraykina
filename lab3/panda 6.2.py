from graph import *

brushColor ("#F4A460")
penColor ("#F4A460")
rectangle (0, 0, 1000, 700)

def myline (x, y, sh_x, sh_y, d):
    p1=[]
    p1.append((x,y))
    for i in range (5):
        x += sh_x
        y += sh_y
        sh_y -= d
        p1.append((x,y))
    return p1

def list(r,x,y,sh_x,sh_y):
    r0 = 2
    n = -4
    while r0 <= r:
        for i in range(n+5):
            circle(x,y,r0)
            x += sh_x
            y += sh_y
        n += 5
        r0 += 1
    n += 7
    while r0 >= 2:
        for i in range(n-5):
            circle(x,y,r0)
            x += sh_x
            y += sh_y
        n -= 5
        r0 -= 1

def ear1(x,y,k):
    p0 = myline(x,y,2*k,4*k,1*k)
    tmp = p0[-1]
    x = tmp[0]
    y = tmp[1]
    p1 = myline(x,y,6*k,-4*k,1*k)
    tmp = p1[-1]
    x = tmp[0]
    y = tmp[1]
    p2 = myline(x,y,-3*k,-3*k,-1*k)
    tmp = p2[-1]
    x = tmp[0]
    y = tmp[1]
    p3 = myline(x,y,-3*k,1*k,-0.3*k)
    tmp = p3[-1]
    x = tmp[0]
    y = tmp[1]
    tmp = p0[0]
    x1 = tmp[0]
    y1 = tmp[1]
    p4 = []
    p4.append((x,y))
    p4.append((x1,y1))
    polygon(p0+p1+p2+p3+p4)

def ear2(x,y,k):
    p0 = myline(x,y,-3*k,0.1*k,-1*k)
    tmp = p0[-1]
    x = tmp[0]
    y = tmp[1]
    p1 = myline(x,y,5*k,8*k,1*k)
    tmp = p1[-1]
    x = tmp[0]
    y = tmp[1]
    p2 = myline(x,y,2*k,-0.2*k,1*k)
    tmp = p2[-1]
    x = tmp[0]
    y = tmp[1]
    p3 = myline(x,y,-1*k,-3*k,-0.3*k)
    tmp = p3[-1]
    x = tmp[0]
    y = tmp[1]
    tmp = p0[0]
    x1 = tmp[0]
    y1 = tmp[1]
    p4 = []
    p4.append((x,y))
    p4.append((x1,y1))
    polygon(p0+p1+p2+p3+p4)

def branch (x, y, sh_x, sh_y, d) :
    p = []
    p.append((x,y))
    for i in range (15):
        x += sh_x
        y -= sh_y
        p.append((x,y))
        sh_y -= d
    polyline(p)

def Tree(x1,y1,x2,y2,):
    brushColor ("#2E8B57")
    penColor ("#2E8B57")
    width = x2 - x1
    high = y1 - y2
    rectangle (x1,y1,x2,y2)
    y1 = y2 - 10
    y2 = y1 - high - 10
    high = y1 - y2
    rectangle (x1,y1,x2,y2)
    branch (x2+3,y2+8,width/3,high/10,1) #right_down branch
    branch (x1-3,y2+high/2,-width/3,high/10,1)
    points1 = [(x1 + width/2, y2 - 10), (x1 - width/6, y2 - 15),
               (x1 + width/2, y2 - 10 - high*2/3),
               (x1 + 7*width/6, y2 - 5 - high*2/3),
               (x1 + width/2, y2 - 10)]
    polygon (points1)
    branch (x1-width/6-5,y2-20,-width/2,high/9,1) #left_up branch
    branch (x1+7*width/6+5,y2 - 10 - high*2/3,width/2,high/9,1)
    points2 = [(x2, y2 - 15 - high*2/3),
               (x2 - width/2, y2 - 20 - high*2/3),
               (x2 + 10, y2 - 20 - high*5/3),
               (x2 + 10 + width/2, y2 - 15 - high*5/3),
               (x2, y2 - 15 - high*2/3)]
    polygon (points2)

def ellipse (a,b,x0,y0):
    for x in range (-a,a):
        for y in range (-b,b):
            if (x**2/a**2+y**2/b**2<=1):
                point(x+x0,y+y0)

def head (x,y,k):
    brushColor ("#FFFFFF")
    penColor ("#FFFFFF")
    p1 = myline(x,y,k*15,k*8,k*5)
    p0 = []
    p2 = []
    p3 = []
    tmp0 = p1[0]
    tmp2 = p1[-1]
    x0 = tmp0[0]
    y0 = tmp0[1]
    x2 = tmp2[0]
    y2 = tmp2[1]
    p0.append((x0-k*10,y0-k*65))
    p0.append((x0-k*9,y0-k*15))
    p0.append(tmp0)
    p2.append(tmp2)
    p2.append((x2+k*15,y2-k*15))
    p3.append((x2+k*17,y2-k*17))
    p3.append((x2+k*20,y0-k*75))
    p4 = myline(x2+k*20,y0-k*75,-8*k,-13*k,-2*k)
    tmp4 = p4[-1]
    x4 = tmp4[0]
    y4 = tmp4[1]
    p5 = myline(x4,y4,-12*k,-1*k,-3*k)
    p5.append((x0-k*10,y0-k*65))
    polygon(p0+p1+p2+p3+p4+p5)

def leg1(x,y,k):
    penSize(3)
    penColor("#000000")
    brushColor("#000000")
    p0 = []; p1 = []; p2 = []; p3 = []; p4 = []
    p0.append((x,y))
    p0.append((x-k*35,y))
    p1 = myline(x-k*35,y,-3*k,4*k,-7*k)
    tmp = p1[-1]
    x1 = tmp[0]
    y1 = tmp[1]
    p2 = myline(x1,y1,5*k,5*k,0.5*k)
    tmp = p2[-1]
    x1 = tmp[0]
    y1 = tmp[1]
    p3.append((x1,y1))
    p3.append((x1+k*30,y1-k*35))
    tmp = p3[-1]
    x1 = tmp[0]
    y1 = tmp[1]
    p4.append((x1,y1))
    p4.append((x,y))
    polygon(p0+p1+p2+p3+p4)

def leg2(x,y,k):
    penSize(3)
    penColor("#000000")
    brushColor("#000000")
    p0 = []; p1 = []; p2 = []
    p3 = []; p4 = []; p5 = []
    p0.append((x,y))
    p0.append((x-k*60,y+k*140))
    p1 = myline(x-k*60,y+k*140,-5*k,1*k,-2*k)
    tmp = p1[-1]
    x1 = tmp[0]
    y1 = tmp[1]
    p2 = myline(x1,y1,6*k,8*k,2*k)
    tmp = p2[-1]
    x1 = tmp[0]
    y1 = tmp[1]
    p3.append((x1,y1))
    p3.append((x1+k*30,y1-k*25))
    tmp = p3[-1]
    x1 = tmp[0]
    y1 = tmp[1]
    p4.append((x1,y1))
    p4.append((x1+25*k,y1-45*k))
    p5.append((x1+25*k,y1-45*k))
    p5.append((x,y))
    polygon(p0+p1+p2+p3+p4+p5)

def leg3 (x,y,k):
    penSize(3)
    penColor("#000000")
    brushColor("#000000")
    p0 = []; p1 = []; p2 = []; p3 = []
    p0 = myline(x,y,k*10,-15*k,k*5)
    tmp = p0[-1]
    x1 = tmp[0]
    y1 = tmp[1]
    p1 = myline(x1,y1,-3*k,-6*k,-2*k)
    tmp = p1[-1]
    x1 = tmp[0]
    y1 = tmp[1]
    p2 = myline(x1,y1,-16*k,21*k,0.5*k)
    tmp = p2[-1]
    x1 = tmp[0]
    y1 = tmp[1]
    p3 = myline(x1,y1,9*k,13*k,3*k)
    polygon(p0+p1+p2+p3)

def panda():
    #big panda
    penColor("#FFFFFF")
    ellipse(101,55,468,405)    #body
    leg1(411,408,1.1)
    leg2(488,355,1.1)
    leg3(510,545,1)
    head (380,440,1.1)
    brushColor ("#000000")
    penColor ("#000000")
    circle(415,405,16)        #eye
    ellipse(11,16,378,398)    #eye
    ellipse(13,9,384,440)     #nose
    penSize(4)
    ear1(358,338,1.1)
    ear2(470,317,1.1)
    #smal panda
    penColor("#FFFFFF")
    ellipse(60,28,290,540)    #body
    leg1(250,540,0.65)
    leg2(300,500,0.65)
    leg3(315,615,0.55)
    head(235,557,0.65)
    brushColor ("#000000")
    penColor ("#000000")
    circle(258,535,10)        #eye
    ellipse(7,10,233,530)     #eye
    ellipse(9,6,238,558)      #nose
    ear1(223,495,0.65)
    ear2(290,485,0.65)

windowSize(800,650)
canvasSize(800,650)
penSize(2)
Tree(80, 475, 88, 425)
Tree(200, 480, 205, 425)
Tree(320, 470, 345, 370)
Tree(635, 460, 642, 375)
#tree leaves
for i in range (5):
    ellipse(3,10,20+9*i,338-i*3)       #tree1
    ellipse(3,10,110+9*i,295+i*3)
    ellipse(3,10,160+7*i,330-i)        #tree2
    ellipse(3,10,220+7*i,300+i)
    list(5,141+20*i,153+i+i+i,-0.2,0.6)#tree3
    list(5,521-20*i,90+i+i+i,0.2,0.6)
    ellipse(3,15,585+9*i,200+i*11)     #tree4
    ellipse(3,15,655+9*i,195-i*12)
for i in range (3):
    ellipse(3,10,40+7*i,400-i*10)      #tree1
    ellipse(3,10,110+7*i,355+i*10)
    ellipse(3,10,175+7*i,390-i*10)     #tree2
    ellipse(3,10,230-7*i,375-i*12)
    list(5,206+23*i,243+i+i+i,-0.2,0.6)#tree3
    list(5,406+23*i,203-i-i-i,0.2,0.6)
    ellipse(3,10,605+7*i,280+i*8)      #tree4
    ellipse(3,10,655+7*i,260-i*10)
panda()

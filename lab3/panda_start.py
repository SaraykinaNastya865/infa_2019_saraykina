from graph import *

brushColor ("#F4A460")
penColor ("#F4A460")
rectangle (0, 0, 1000, 600)

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

def ear1(x,y):
    p0 = myline(x,y,2,4,1)
    tmp = p0[-1]
    x = tmp[0]
    y = tmp[1]
    p1 = myline(x,y,6,-4,1)
    tmp = p1[-1]
    x = tmp[0]
    y = tmp[1]
    p2 = myline(x,y,-3,-3,-1)
    tmp = p2[-1]
    x = tmp[0]
    y = tmp[1]
    p3 = myline(x,y,-3,1,-0.3)
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

def ear2(x,y):
    p0 = myline(x,y,-3,0.1,-1)
    tmp = p0[-1]
    x = tmp[0]
    y = tmp[1]
    p1 = myline(x,y,5,8,1)
    tmp = p1[-1]
    x = tmp[0]
    y = tmp[1]
    p2 = myline(x,y,2,-0.2,1)
    tmp = p2[-1]
    x = tmp[0]
    y = tmp[1]
    p3 = myline(x,y,-1,-3,-0.3)
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
              (x1 + width/2, y2 - 10 - high*2/3), (x1 + 7*width/6, y2 - 5 - high*2/3),
              (x1 + width/2, y2 - 10)]
    polygon (points1)
    branch (x1-width/6-5,y2-20,-width/2,high/9,1) #left_up branch
    branch (x1+7*width/6+5,y2 - 10 - high*2/3,width/2,high/9,1)
    points2 = [(x2, y2 - 15 - high*2/3), (x2 - width/2, y2 - 20 - high*2/3),
              (x2 + 10, y2 - 20 - high*5/3), (x2 + 10 + width/2, y2 - 15 - high*5/3),
              (x2, y2 - 15 - high*2/3)]
    polygon (points2)

def ellipse (a,b,x0,y0):
    for x in range (-a,a):
        for y in range (-b,b):
            if (x**2/a**2+y**2/b**2<=1):
                point(x+x0,y+y0)

def head (x,y):
    brushColor ("#FFFFFF")
    penColor ("#FFFFFF")
    p1 = myline(x,y,15,8,5)
    p0 = []
    p2 = []
    p3 = []
    tmp0 = p1[0]
    tmp2 = p1[-1]
    x0 = tmp0[0]
    y0 = tmp0[1]
    x2 = tmp2[0]
    y2 = tmp2[1]
    p0.append((x0-10,y0-65))
    p0.append((x0-9,y0-15))
    p0.append(tmp0)
    p2.append(tmp2)
    p2.append((x2+15,y2-15))
    p3.append((x2+17,y2-17))
    p3.append((x2+20,y0-75))
    p4 = myline(x2+20,y0-75,-8,-13,-2)
    tmp4 = p4[-1]
    x4 = tmp4[0]
    y4 = tmp4[1]
    p5 = myline(x4,y4,-12,-1,-3)
    p5.append((x0-10,y0-65))
    polygon(p0+p1+p2+p3+p4+p5)
    brushColor ("#000000")
    penColor ("#000000")
    circle(x4-20,y2-25,15)
    ellipse(10,15,378,358)
    ellipse(12,8,384,400)

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
        penColor("#FFFFFF")
        ellipse(92,50,460,370)
        leg1(406,368,1)
        leg2(480,315,1)
        leg3(500,495,0.9)
        head (380, 400)
        penSize(4)
        ear1(360,305)
        ear2(463,285)

windowSize(700,600)
canvasSize(700,600)
penSize(2)
Tree(320, 470, 345, 370)
Tree(200, 480, 205, 425)
for i in range (5):
    list(5,141+20*i,153+i+i+i,-0.2,0.6)
    list(5,521-20*i,90+i+i+i,0.2,0.6)
    ellipse(3,10,160+7*i,330-i)
    ellipse(3,10,220+7*i,300+i)
for i in range (3):
    list(5,206+23*i,243+i+i+i,-0.2,0.6)
    list(5,406+23*i,203-i-i-i,0.2,0.6)
    ellipse(3,10,175+7*i,390-i*10)
    ellipse(3,10,230-7*i,375-i*12)
panda()

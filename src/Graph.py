import math,re,random,json, tkinter as tk
from Function import Function

mousedown = False
prev_x, prev_y = 0, 0

class Graph:
    def __init__(self, canvas):
        self.functions = [None, None, None, None, None]
        self.width = 800
        self.height = 800
        self.canvas = canvas
        self.zoom = 1 # 1 number = 40 pixels
        self.xMin = -10
        self.xMax = 10
        self.yMin = -10
        self.yMax = 10
        self.useAsDefVar = 'x'
        self.orig = (self.width / 2, self.height / 2)
        self.Xrange = range(-math.floor(len(range(math.floor(self.xMin), math.floor(self.xMax), 1))/2),math.floor(len(range(math.floor(self.xMin), math.floor(self.xMax), 1))/2),1) # label for rendering
        self.Yrange = range(-math.floor(len(range(math.floor(self.yMin), math.floor(self.yMax), 1))/2),math.floor(len(range(math.floor(self.yMin), math.floor(self.yMax), 1))/2),1)
        self.font = ('Arial 15 bold')
        self.functionDefs = list() # all parsed functions at the ready
        self.dx = 0
        self.dy = 0
        self.PREC = 400
        self.bounce = False
        self.userDefinedVars = {"A":0, "B":0, "C":0, "D":0, "E":0} # special extra utility vars
    def init(self):
        self.drawLinesAndAxes()
        self.drawNumbers()
    def render(self): # render entire graph as user drags through. 
        # bind events
        for f in self.functions:
            if f != None:
                f.parse(f.raw) # parse again then graph
                f.graph(400, self)
    def drawLinesAndAxes(self):
        self.canvas.create_line(0, self.orig[1]+ self.dy, self.width , self.orig[1]+ self.dy, fill="black", width=2)
        self.canvas.create_line(self.orig[0] + self.dx, 0, self.orig[0] + self.dx, self.height, fill="black", width=2)
        # place arrows for decoration
        points = [
            [self.orig[0]+ self.dx, 0, self.orig[0]-10+ self.dx, 15,self.orig[0]+10+ self.dx , 15],
            [self.orig[0]+ self.dx,self.height,self.orig[0]-10+ self.dx,self.height-15, self.orig[0]+10+ self.dx,self.height-15],
            [0,self.orig[1]+ self.dy,15,self.orig[1]+10+ self.dy, 15, self.orig[1]-10+ self.dy],
            [self.width, self.orig[1]+ self.dy, self.width-15, self.orig[1]-10+ self.dy, self.width-15, self.orig[1]+10+ self.dy]
        ]
        for x in points:
                self.canvas.create_polygon(x, fill="blue")
    def drawNumbers(self):
        lx, ly = len(self.Xrange), len(self.Yrange)
        n = 0
        for i in range(lx):
            dx = self.width / lx
            self.canvas.create_text(dx*n, (self.height/2)+self.dy+10,font="Arial 10", text=self.Xrange[n]) # draw number at x pos
            n+=1
        n = 0
        for i in range(ly):
            dy = self.height / ly
            if self.Yrange[n] != 0:
                self.canvas.create_text((self.width/2)+self.dx-10, self.height-(dy*n),font="Arial 10", text=self.Yrange[n]) # draw number at x pos
            n+=1

    def onscroll(self, event):
        global prev_x, prev_y
        if mousedown:
            self.clear()
            #print(prev_x, prev_y, self.dx, self.dy)
            curr_x, curr_y = event.x, event.y
            dx, dy = curr_x - prev_x, curr_y - prev_y
            self.dx, self.dy = dx , dy 
        
            self.Xrange = range(-math.floor((len(range(math.floor(self.xMin), math.floor(self.xMax), 1))/2)+(dx/40)),math.floor((len(range(math.floor(self.xMin), math.floor(self.xMax), 1))/2)-(dx/40)),1)
            self.Yrange = range(-math.floor((len(range(math.floor(self.yMin), math.floor(self.yMax), 1))/2)-(dy/40)),math.floor((len(range(math.floor(self.yMin), math.floor(self.yMax), 1))/2)+(dy/40)),1)
            self.drawLinesAndAxes()
            self.drawNumbers()
            self.render()
        if self.bounce:
            prev_x, prev_y = event.x, event.y #Bouncy graph. Stupid feature that mesmerizes me
    def clear(self):
        self.canvas.delete("all")
    def togMouse(self):
        global mousedown
        mousedown = not mousedown
    def togPrev(self, event):
        global prev_x, prev_y
        prev_x, prev_y = event.x - self.dx, event.y - self.dy
    def prevDelta(self):
        global prev_x, prev_y
        prev_x, prev_y = event.x, event.y
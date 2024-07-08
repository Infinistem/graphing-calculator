import math,re,random,json, tkinter as tk

WIDTH = 800 # canvas width and height
HEIGHT = 800
class Function:
    def __init__(self, equation, color):
        self.raw = equation
        self.show = True
        self.color = color
        self.parsed = None
    def parse(self, raw): # parse only before graphing
        print('parsing...')
        raw = str(raw)
        PREFIX = 'math.'   
        FUNCTIONS_A = ["sin", "cos", "tan", "sec", "csc", "cot", "fact", "max", "min", "asin", "acos", "atan", "sinh", "cosh", "tanh", "log", "ceil", "floor"]     
        new = {"E": math.exp(1), "PI":math.pi, "fact":"factorial", "deg":"degrees", "rand":"random.random"} # non default replacements
        for x in FUNCTIONS_A:
            if x in new.keys():
                raw = raw.replace(x, PREFIX + new[x])
            else:
                raw = raw.replace(x, PREFIX + x)
        regex_coeff=r'(-?\d+)x' 
        coefficients = re.findall(regex_coeff, raw) 
 
        coefficients = [float(coef) for coef in coefficients] 
        for x in coefficients:
            if int(x) == x:
                coefficients[coefficients.index(x)] = int(x)
        for x in coefficients:
            raw = raw.replace(str(x), str(x) + '*')
        raw = raw.replace("^", "**")
        self.parsed = raw
    def isNum(x):
        if x is int:
            return True
        return type(x)
    def displayError(Err):
        pass
    def graph(self, PREC, plot):
        canvas = plot
        prev_mx, prev_my = plot.xMin, plot.yMin
        prevPoint = ()
        for i in range(-math.floor(PREC), math.floor(PREC*5), 1):
            px = i / PREC
            X = (px * (plot.xMax - plot.xMin) + plot.xMin);
            Y = -1 * self.evl(X) # evaluate function
            py =  (Y - plot.yMin) / (plot.yMax - plot.yMin)
            mx = (px * WIDTH)+plot.dx
            my = (py * HEIGHT)+plot.dy
            plot.canvas.create_line(prev_mx, prev_my, mx, my, fill=self.color, width=1)
            prev_mx, prev_my = mx, my
            

            # replace variable with whatever px, py value needed
    def evl(self, x):
        function = self.parsed
        function = function.replace('x', str(x))
        try:
            e = eval(function)
        except ValueError:
            return "skip"
        return e
    def generateTable():
        pass
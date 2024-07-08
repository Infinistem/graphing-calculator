# a nice graphing tool in python
# MAY ADD: Matrix & Vector operations
import math,re,random,json, tkinter as tk
from PIL import ImageTk, Image
import pyautogui as pg # for screenshot
from tkinter import * 
from threading import Timer

from Graph import Graph, mousedown, prev_x, prev_y
from Function import Function

WIDTH = 800 # canvas width and height
HEIGHT = 800
PREC = 400 # graphing precision
BRKAT = 10000 # utility var - defines end of any used while loops just to prevent infinite recursion
COLORS = ['blue', 'black', 'green', 'red', 'goldenrod']
LIM = 5
saveloc = "saves\graph.png"

# main utilities for io
def functionsl():
    win = createMenuWindow(400, 380, "Supported Functions")
    Label(win, text="Functions: sin cos tan sec csc cot asin acos atan cosh sinh tanh log ceil floor fact max min deg (radians to degrees) rand. Integrated Variables: PI, E", width=200, wraplength=200).pack()

def clearall():
    pass
def lm():
    root.config(background="white")
def dm():
    root.config(background="black")
def about():
    win = createMenuWindow(400, 380, "About The App")
    Label(win, text="I created this app as a simple programming project to document on my github, however noticing it is practical for use I have provided an executable to make it easier for anyone else to use it. ", width=300, wraplength=370).pack()
def savepng():
    x, y = canvas.winfo_rootx(), canvas.winfo_rooty()
    w, h = canvas.winfo_width(), canvas.winfo_height()
    pg.screenshot(saveloc, region=(x, y, w, h))
def editSaveLoc():
    pass
def cl(event):
     graph.togMouse()
     graph.togPrev(event)
def clb(event):
    graph.togMouse()
    graph.togPrev(event)
def grph():
    current = 0 # entry widget were on
    for x in root.winfo_children():
        if x.winfo_class() == "Entry":
            val = x.get()
            if graph.functions[current] != None:
                if graph.functions[current].raw != val:
                    graph.functions[current].raw = str(val)
                    graph.functions[current].color = COLORS[current]
            else:
                if val != "":
                    graph.functions[current] = Function(str(val), COLORS[current])
                    graph.functions[current].color = COLORS[current]
            current+=1
    print(graph.functions)
    graph.render()
def bounce():
    graph.bounce = not graph.bounce
def resize():
    graph.dx = 0
    graph.dy = 0
    graph.clear()
    graph.xMin = -10
    graph.xMax = 10
    graph.yMin = -10
    graph.yMax = 10
    graph.Xrange = range(-math.floor(len(range(math.floor(graph.xMin), math.floor(graph.xMax), 1))/2),math.floor(len(range(math.floor(graph.xMin), math.floor(graph.xMax), 1))/2),1) # label for rendering
    graph.Yrange = range(-math.floor(len(range(math.floor(graph.yMin), math.floor(graph.yMax), 1))/2),math.floor(len(range(math.floor(graph.yMin), math.floor(graph.yMax), 1))/2),1)
    graph.drawLinesAndAxes()
    graph.drawNumbers()
    graph.render()


def editvars():
    win = createMenuWindow(300, 380, "Edit Variables")
    func1a,func2a,func3a,func4a,func5a = Entry(win, font=("Arial", 18),foreground="blue"),Entry(win, font=("Arial", 18),foreground="blue"),Entry(win, font=("Arial", 18),foreground="blue"),Entry(win, font=("Arial", 18),foreground="blue"),Entry(win, font=("Arial", 18),foreground="blue")
    l1a, l2a, l3a, l4a, l5a = Label(win,foreground="blue", font=("Arial", 18), text="A="),Label(win,foreground="blue", font=("Arial", 18), text="B="),Label(win,foreground="blue", font=("Arial", 18), text="C="),Label(win,foreground="blue", font=("Arial", 18), text="D="),Label(win,foreground="blue", font=("Arial", 18), text="E=")
    func1a.place(x=50, y=100, width=210, height=39)
    func2a.place(x=50, y=150, width=210, height=39)
    func3a.place(x=50, y=200, width=210, height=39)
    func4a.place(x=50, y=250, width=210, height=39)
    func5a.place(x=50, y=300, width=210, height=39)
    l1a.place(x=10, y=100)
    l2a.place(x=10, y=150)
    l3a.place(x=10, y=200)
    l4a.place(x=10, y=250)
    l5a.place(x=10, y=300)
    Button(win, text="Update", command=lambda:saveVars(win)).place(x=20, y=50, width=110)
    Button(win, text="Free All").place(x=140, y=50, width=110)
    win.mainloop()
def saveVars(win):
    last = None
    for x in win.winfo_children():
        if x.winfo_class() == 'Label':
            last = x.cget("text")
        elif x.winfo_class() == "Entry":
            graph.userDefinedVars[last] = x.get()
    print(graph.userDefinedVars)

def createMenuWindow(width, height, title): # returns widget
    window = tk.Toplevel(root)
    window.geometry("%sx%s+10+10"%(width, height))
    window.title(title)
    return window

root, graph = Tk(), None
root.title("Graphing Calculator - Windows Edition")
root.resizable(False, False)
root.geometry("1100x800+10+10")
root.config(background="white")
canvas = Canvas(root, background="white", width=WIDTH, height=HEIGHT)
canvas.place(x=0, y=0)
graph = Graph(canvas)
graph.init()
canvas.bind("<Button-1>", cl)
canvas.bind("<ButtonRelease-1>", clb)
canvas.bind("<Motion>", graph.onscroll)
Label(root, text="Functions", font=("Arial", 22), foreground="blue").place(x=810, y=0)
l1, l2, l3, l4, l5 = Label(root,foreground="blue", font=("Arial", 18), text="Y="),Label(root,foreground="black", font=("Arial", 18), text="Y="),Label(root,foreground="green", font=("Arial", 18), text="Y="),Label(root,foreground="red", font=("Arial", 18), text="Y="),Label(root,foreground="goldenrod", font=("Arial", 18), text="Y=")
l1.place(x=810, y=100)
l2.place(x=810, y=150)
l3.place(x=810, y=200)
l4.place(x=810, y=250)
l5.place(x=810, y=300)
func1,func2,func3,func4,func5 = Entry(root, font=("Arial", 18),foreground="blue"),Entry(root, font=("Arial", 18),foreground="black"),Entry(root, font=("Arial", 18),foreground="green"),Entry(root, font=("Arial", 18),foreground="red"),Entry(root, font=("Arial", 18),foreground="goldenrod")
func1.place(x=850, y=100, width=210, height=39)
func2.place(x=850, y=150, width=210, height=39)
func3.place(x=850, y=200, width=210, height=39)
func4.place(x=850, y=250, width=210, height=39)
func5.place(x=850, y=300, width=210, height=39)
b=Button(root, text="Graph", command=grph)
b.place(x=850, y=350, width=100, height=38)
Button(root, text="Clear").place(x=960, y=350, width=100, height=38)
menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label="Save graph as png", command=savepng)
filemenu.add_command(label="Generate table")
filemenu.add_command(label="Intersections")
filemenu.add_command(label="Bounce Graph", command=bounce)
filemenu.add_command(label="Reset Scale", command=resize)
filemenu.add_command(label="Get y at")
editmenu = Menu(menubar)
editmenu.add_command(label="Delete all functions", command=clearall)
editmenu.add_command(label="Edit user variables", command=editvars)
editmenu.add_command(label="Graph Circle")

thememenu = Menu(menubar)
thememenu.add_command(label="Light Mode",command=lm)
thememenu.add_command(label="Dark Mode",command=dm)
helpmenu = Menu(menubar)
helpmenu.add_command(label="Functions Supported", command=functionsl)
helpmenu.add_command(label="About app",command=about)
helpmenu.add_command(label="How to use")




menubar.add_cascade(label="File & Graph", menu=filemenu)
menubar.add_cascade(label="Edit Graph", menu=editmenu)
menubar.add_cascade(label="App Theme", menu=thememenu)
menubar.add_cascade(label="Help", menu=helpmenu)




root.config(menu=menubar)




root.mainloop()

#File : Save Graph as png, Save Graph as svg, Generate Table, Get y at
# Edit : Delete All, Variables, Default Variable, Equation Colors
# Theme : Light Mode, Dark Mode, System Default
# Help



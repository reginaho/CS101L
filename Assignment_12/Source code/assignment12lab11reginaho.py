########################################################################
##
## CS 101 Lab
## Program #Assignment 12
## Name: Regina Ho
## Email: uhhvng@umkc.edu
##
## PROBLEM : Describe the problem
## Use the turtle module to draw on the screen.
#
# ALGORITHM : 
# Step 1: import turtle
# 
# Step 2: Creating our super class
##
# Step 3: create a new class called Box that inherits from Point
#       Now create an __init__ method that has parameters; self, x1, y1, width, height, color.
# Since we are inherited from point, we can have the super class setup our our instance.
# After that in the init you want to set the width and height for the self instance
## 
# Step 4: Create BoxFilled class.
#       Create another class in the solution called BoxFilled that inherits from Box.
#       Then create an init method that takes x1, y1, width, height, color and fillcolor as parameters.
# Step 5: Creating a Circle class
#Create a Circle class that inherits from the Point class.  The init parameters will be x1, y1, radius and color.
# Make sure you call the init for the super class. You’ll have to save the radius.
#In the draw_action called turtle.circle() and pass it the radius to draw a circle.

# Step 6: Creating a CircleFilled class
# Create a CircleFilled class that inherits from the Circle class.  The init parameters will be x1, y1, radius, color and fill color. 
# Use the same tactics we learned from earlier to only save the new fill color in the instance and test your results.
# In the draw action, you should call the Circle draw_action method like we did with BoxFilled, but call fillcolor, begin_fill first and then end_fill afterwards.
  #Call super().__init__() method.  Remember we are inheriting from Box this time so pass it the values that Box needs to be instantiated.  ( we don't’ have to pass self to the super init 

# Step 7: draw all the circle, box
##
##
##
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################
import turtle

class Point(object):
    def __init__(self,x,y,color):
        self.x=x
        self.y=y
        self.color=color

    def draw(self):
        turtle.penup()
        turtle.goto(self.x,self.y)
        turtle.pendown()
        turtle.color(self.color)
        turtle.setheading(0)
        self.draw_action()

    def draw_action(self):
        turtle.dot()

class Box(Point):
    def __init__(self, x1, y1, width, height, color):
        super().__init__(x1, y1, color)
        self.width=width
        self.height=height

    def draw(self):
        turtle.penup()
        turtle.goto(self.x,self.y)
        turtle.pendown()
        turtle.color(self.color)
        turtle.setheading(0)
        self.draw_action()

    def draw_action(self):
        turtle.forward(self.width)
        turtle.right(90)
        turtle.forward(self.height)
        turtle.right(90)
        turtle.forward(self.width)
        turtle.right(90)
        turtle.forward(self.height)
        turtle.right(90)

class BoxFilled(Box):
    def __init__(self,x1,y1,width,height,color,fillcolor):
        super().__init__(x1,y1,width,height,color)
        self.fillcolor=fillcolor

    def draw(self):
        turtle.penup()
        turtle.goto(self.x,self.y)
        turtle.pendown()
        turtle.color(self.color)
        turtle.setheading(0)
        self.draw_action()

    def draw_action(self):
        turtle.begin_fill()
        turtle.color(self.fillcolor)
        Box.draw_action(self)
        turtle.end_fill()

class Circle(Point):
    def __init__(self, x1, y1, radius, color):
        super().__init__(x1, y1, color)
        self.radius = radius

    def draw_action(self):
        turtle.circle(self.radius)

class CircleFilled(Circle):
    def __init__(self, x1, y1, radius, color, fillcolor):
        super().__init__(x1, y1, radius, color)
        self.fillcolor = fillcolor

    def draw_action(self):
        turtle.fillcolor(self.fillcolor)
        turtle.begin_fill()
        Circle.draw_action(self)
        turtle.end_fill()

p=Point(-100,100,"blue")
p.draw()

b=Box(100,110,50,40,"red")
b.draw()

b = BoxFilled(180, 150, 100, 50, "green", "blue")
b.draw()

c=Circle(-200,210,50,"green")
c.draw()

c1=CircleFilled(-200,210,50, "green", "red")
c1.draw()
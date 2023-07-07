import turtle
import time
x = turtle.Turtle() #it will create a turtle
x.shape("turtle")       #changes the shape of turtle
x.color("red","black")      #first argument is line colour and second is color of turtle

srn = turtle.Screen()
srn.bgcolor("yellow")
srn.title("bhanu")
srn.screensize(500,500)
#we can use background image also
# #to use image python and image both should be in same folder and file format must be gif
# #````srn.bgpic("path")

# x.setheading(90)    #now it will make 90 deg angle
# x.setheading(180)
# a = 100

# for i in range(4):
#     x.forward(a)
#     x.left(90)

# #to change position of turtle--
# x.setpos(-250,-250) 
# #OR
# x.goto(250,250)
# x.setx(0)
# x.sety(0)
# x.home()    #move the turtle to the origin


# #CIRCLE METHOD
# #arg1 - radius of circle
# #arg2 - extent(means angle that the circle will cover)
# #arg3 - steps(means number of edges)
# x.circle(50)    
# #to make a regular polygon 
# x.circle(100,5)
# #to make a semicircle-
# x.circle(100,1/2,100)


# #DOT Method--
# #arg1 - size that defines the diameter
# #arg2 - that defines the color
# x.dot(50,"red")
# x.forward(100)

# #turtle.stamp--
# #make a turtle shape object at the current turtle position
# #return an integer id that can be used to delete it in future
# x.stamp()
# x.backward(500)
# #x.clearstamp()  this function requires the id of turtle to be deleted
# #clearstamps--
# #arg - if n is none clear all stamps
# # if n is pos clear first n stamps
# # if n is -ive clear last n stamps
# x.clearstamps(-1) #delete last stamp

# #undo 
# for i in range(12):
#     x.undo()   #undos the last action

# #position
# x.position()    #returns the position
# x.xcor()    #returns x coordinate
# x.ycor()    #returns y coordinate
# x.heading() #returns the eading angle
# x.distance(2,3)    #returns the distance from (x,y)


# #fill colour
# x.begin_fill()
# x.fillcolor("red")
# x.circle(100,steps=6)
# x.end_fill()

# x.reset()   #returns to home position
# x.clear()      #delete drawings of turtle

#till here I'm commenting out
#turtle state--


x.ht()  #hides the turtle
x.forward(200)
x.st()  #show turtle


#appearane-
x.shape("triangle")
x.tilt(90)  #change the turtle angle but don't change its heading


#USING EVENTS--
#arg1 - a function with two arguments it will be called
#arg2 - number of the mouse button 1 for left
#arg3 - if true a new binding will be added
def turn(u,v):
    x.left(180)
    x.backward(250)
srn.onclick(turn) #turn 180 left
srn.onclick(None) #binding will be removed


turtle.done()
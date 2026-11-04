import turtle
#switched over the VS Code app to code from this point on.

turtle.bgcolor("black")
print("Welcome to Spooky Clicker! Check out the separate window to see the visuals :>")

#turtles:
pen = turtle.Turtle()
p = turtle.Turtle()

#main/official colors (ideally..?):
pen.color("orange")
p.color("red")

#for a cool intro of sorts!
p.hideturtle()

#turtle window's title
turtle.title("Spooky Clicker")

#title
pen.penup()
pen.goto(-200, 200)
pen.write("Spooky Clicker", align = "left", font = ("Impact", 30, "bold"))

#title styling
pen.penup()
pen.goto(-210, 195)
for formatting in range(8):
    pen.pendown()
    pen.forward(25)
    pen.penup()
    pen.forward(25)




#play button circle shape attempt
p.penup()
p.color("white")
p.goto(-150, 0)
p.goto(-70, 0)
p.dot(80, "green")

#inner play button (triangle)
p.color("white")
p.pensize(15)
#p.fillcolor("white")    #fills in weirdly
#p.begin_fill()
p.penup()
p.home()
p.backward(80)  #85
p.right(90)
p.backward(12.5)  #might be too far down on the play button..?    #25
p.pendown()
p.forward(25)   #50
p.left(120)
p.forward(25)   #50
p.left(120)
p.forward(25)  #50
#p.end_fill()

#"Click to Play" message
#p.hideturtle()
p.penup()
p.left(120)
p.forward(90)
p.right(90)
p.forward(50)
p.write("Click to Play!", align = "left", font = ("Verdana", 15, "normal"))



#menu button thingy ma jiggy 2
p.showturtle()
p.goto(0, 0)
p.fillcolor("green")  #why is there not a light green  :<
p.color("green")
#moved smth from here can't recall what (begin fill..?)
p.penup()
#p.goto(-250, 0) #used to be and still is commented out for a reason XD
p.goto(0, -150)
p.begin_fill()
#p.forward(100) #used to be commented out
#p.left(45) #used to be commented out
p.setheading(0)
p.pendown()
#p.left(45)
#p.forward(50)
#p.right(45)  #dupe
p.forward(100)
p.right(45)
p.forward(50)
p.right(90)
p.forward(50)
p.right(45)
p.forward(100)
p.right(45)
p.forward(50)
p.right(90)  #this and the other line, below to make a rounded button shape
p.forward(50)  #this and the other line, above to make a rounded button shape
p.end_fill()

#menu button's text
p.penup()
p.hideturtle()
p.setheading(0)
p.right(90)
p.forward(25)
p.setheading(0)
p.forward(50)
p.right(90)
p.forward(25)
p.color("white")
p.write("MENU", align = "center", font = ("Verdana", 25, "bold"))


#wip line of code below:
click_play_range = range()


pen.hideturtle()
turtle.done()


#A DOORWAY!!
#p.showturtle()
#p.goto(0, 0)
#p.fillcolor("green")  #why is there not a light green  :<
p.color("green")
#    #moved smth from here can't recall what (begin fill..?)
#p.penup()
#    #p.goto(-250, 0) #used to be and still is commented out for a reason XD
#p.goto(0, -150)
#p.begin_fill()
#    #p.forward(100) #used to be commented out
#    #p.left(45) #used to be commented out
#p.setheading(0)
#p.pendown()
#p.left(45)
#p.forward(50)
#p.left(45)  #dupe
#p.forward(100)
#p.right(45)
#p.forward(50)
#p.right(90)
#p.forward(50)
#p.right(45)
#p.forward(100)
#p.right(45)
#p.forward(50)
#p.end_fill()
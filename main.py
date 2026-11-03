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
p.goto(-150, 0)
p.goto(-70, 0)
p.dot(80, "green")

#play button
p.color("green")
p.penup()
p.goto(-250, 0)
p.showturtle()
p.forward(100)
p.left(45)
p.pendown()
p.forward(50)
p.right(45)
p.forward(100)
p.right(45)
p.forward(50)
p.right(90)
p.forward(50)
p.right(45)
p.forward(100)
p.right(45)
p.forward(50)

#inner play button (triangle)
p.color("white")
p.penup()
p.home()
p.backward(85)
p.right(90)
p.backward(25)  #might be too far down on the play button..?
p.pendown()
p.forward(50)
p.left(120)
p.forward(50)
p.left(120)
p.forward(50)

#"Click to Play" message
#p.hideturtle()
p.penup()
p.left(120)
p.forward(90)
p.right(90)
p.forward(50)
p.write("Click to Play!", align = "left", font = ("Verdana", 15, "normal"))





pen.hideturtle()
turtle.done()
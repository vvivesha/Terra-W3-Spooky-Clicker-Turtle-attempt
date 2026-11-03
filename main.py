import turtle
#switched over the VS Code app to code from this point on.

turtle.bgcolor("black")
print("Welcome to Spooky Clicker! Check out the separate window to see the visuals :>")

#turtles:
pen = turtle.Turtle()
p = turtle.Turtle()

pen.color("orange")
p.color("red")

#title
pen.penup()
pen.goto(-200, 200)
pen.write("Spooky Clicker", align = "left", font = ("Arial", 30, "bold"))

#title styling
pen.penup()
pen.goto(-210, 195)
for formatting in range(8):
    pen.pendown()
    pen.forward(25)
    pen.penup()
    pen.forward(25)

p.penup()
p.goto(-250, 0)
p.pendown()
p.forward(100)


pen.hideturtle()
turtle.done()
#moved import turtle down to delay the opening of the turtle window
import time
from time import sleep
import random
mystery_item = "unchosen"
game = "off"
mystery_item_chosen = "false"
#stats:
hype = "0"
upkeep = "30"  #this is your budget for upgrades; currently 30% of all earnings before uptime bills (yes, we will bill you for using our hosting services). You start off with $30 bucks!
morale = "50"  #(you are stressed out.)
earnings = "0"  #what matters in the end; it is spent on your Halloween costume.

def slow_print(text, delay):
    for letter in text:
        print(letter, flush = True, end = "")
        sleep(delay)

print("WELCOME to:  Get Rich Before Halloween So You Can Buy a Good Costume Simulator")
print(" ")
more_wait = input("Enable fast mode?  TYPE:  y/n                (The introduction will go by *rapidly*; you'll still have to read to understand what is going on, if this is your first attempt at this game)  ")
if more_wait == "y" or "Y":
    wait_time = 2.5
    print("<Alright, we'll take it a bit slower>")
if more_wait == "n" or "N":
    wait_time = 1.5
    slow_print("<Get ready!>")
for gap in range(5):
    print(" ")
time.sleep(1.5)
slow_print("Think of this game like a tycoon!", 0.01)
print(" ")
slow_print("Your objective: ", 0.01)
print(" ")
slow_print("Make a Spooky Clicker app --> get $$$ --> buy yourself a costume!", 0.01)
time.sleep(1.5)
print(" ")
time.sleep(0.1)
for gap in range(2):
    print(" ")
slow_print("Today is... Thursday, October 29th, 2026", 0.01)
print(" ")
time.sleep(1.5)
print("Pssssst:  yep, you have THREE days before Halloween night. So you're definitely on a time crunch; good luck!!")
time.sleep(1.5)

for gap in range(3):
    print(" ")

for gap in range(5):
    print("")

slow_print("You will recieve a Spooky Clicker window: it will be how you earn $$$ for your Halloween costume. You have...  7  days. Goodluck!", 0.01)
for gap in range(3):
    print(" ")

slow_print("BUT: first, you need a game plan: ", 0.1)
time.sleep(3)
print(" ")
print("<you can ONLY PICK ONE game plan>")
for gap in range(3):
    print(" ")
print("=========================================")
print("-->  1)  contact everybody that you know")
print("-->  2)  get a flashy marketing page")
print("=========================================")
for gap in range(3):
    print(" ")

plan = input("Option 1 or 2?  ")
time.sleep(1.5)
if plan == "1":
    print(" ")
    print(" ")
    slow_print("You hit up all of your buddies at school. Nice that you spent time making the connections beforehand!", 0.005)
    hype = hype + 15
input("<Press ENTER to recieve your Spooky Clicker window>")

import turtle

def store(enter_or_exit):
    pen,showturtle()
    pen.goto(0,0)
    pen.clear
    p.clear
    pen.color("orange")
    pen.goto(-200, 200)
    pen.write("STORE", align = "left", font = ("Impact", 30, "bold"))   #store title
    pen.goto(-210, 195)  #store title underline dashed
    for formatting in range(8):
        pen.pendown()
        pen.forward(25)
        pen.down()
        pen.forward(25)
    #store's contents:
    pen.goto(0, 0)


turtle.Screen().listen()
turtle.Screen().onkey(store, "q")


slow_print("<You have... $15.00>", 0.008)
print(" ")
slow_print("Here is a brief guide to the game. Screenshot for convenience!")
for gap in range(3):
    print(" ")

slow_print("STATS:    (4 categories to keep track of)", 0.001)
for gap in range(3):
    print(" ")
print("MORALE:  this is your mental well-being! You start off with 50/100. Dip below 10 morale, and now you are dangerously depressed!!!")
input("<Press ENTER to continue>  (1/4)")
print(" ")
print("HYPE:  this is how excited the world is to try out your Spooky Clicker app! Currently, there is no hype. Better start spreading the word!")
input("<Press ENTER to continue>  (2/4)")
print(" ")
print("UPKEEP:  this is 30 percent of your total money! This is the number shown that you are allowed to spend on upgrades to your app. You start off with $15.")
input("<Press ENTER to continue>  (3/4)")
print(" ")
print("and finally...")
print("EARNINGS:  THIS is the money that needs to grow to at least $50 by the end of the 3 days. (Else you'll be going trick-or-treating in rags!)")
time.sleep(1)
print("You will start out with $0 under EARNINGS because you are spending your last $15 on getting this site up and going.")
input("<Press ENTER to continue ()>  (4/4)")
for gap in range(3):
    print(" ")
slow_print("To visit the store, press 'q' on the separate window. To purchase an upgrade, type its corresponding number into the following box:  ", 0.01)
print(" ")
slow_print("Now I\'m going to make you visit the store with me :>  ", 0.01)
store_visit_done = input("All done?  (y/n)")
if store_visit_done == "y":
    store(exit)
while vist_store == "true":
    buy = input("Pick a number, any number!  ")
    if buy not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        for gap in range(3):
            print(" ")
    slow_print("HEY... stop messing with me, please!!")
    print(" ")
    time.sleep(0.1)
    buy = input("Please pick an *acutal* option, and THEN we can discuss purchasing that upgrade.  ")



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
p.write("Press p to Play!", align = "left", font = ("Verdana", 15, "normal"))



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

#turtle.Screen().listen()
turtle.Screen().onkey(play_pressed, "p")  #so apparently it is case-sensitive to the point that a "P" would expect shift + P to activate the code...

def play_pressed():
    play_triggered = "yes"
    print("<pressed play>")
    game_on()
    p.clear()



def game_on():
    global game
    game = "on"
    print("<game has begun>")
    turtle.bgcolor("gray")
    p.showturtle()
    time.sleep(0.2)
    p.setheading(0)
    seconds = 4
    p.color("red")
    for countdown in range(3):
        p.clear()
        p.color("red")
        seconds -= 1
        p.hideturtle()
        p.color("white")
        p.goto(0, -100)
        p.write(str(seconds), align = "center", font = ("Impact", 100, "bold"))
        time.sleep(4.2)
        #item_randomizer()



#add a green border-flash for fun if time allows!!

def item_randomizer(options):
    p.clear()
    pen.goto(0, -100)
    pen.write("Rolling the clickable item...", align = "center", font = ("Impact", 20, "bold"))
    items = ["A", "B", "C"]
    mystery_item_chosen = "false"
    while mystery_item_chosen == "false":
        for randomizer in range(12):
            global mystery_item
            mystery_item = random.choice(items)
            if mystery_item == "A":
                mystery_item = "PUMPKIN"
            if mystery_item == "B":
                mystery_item == "BLACK CAT"
            if mystery_item == "C":
                mystery_item == "CANDY"
            p.write(random.choice(mystery_item), align = "center", font = ("Impact", 25, "bold"))
            time.sleep(0.1)
            p.clear()
        mystery_item_chosen = "true"
        break
    time.sleep(1.5)
    pen.write("You rolled... ", align = "center", font = ("Courier New", 25, "normal"))
    pen.write(mystery_item, align = "left", font = ("Verdana", 30, "normal"))

pen.write("Check the terminal and input a number. Then, return to this window  :)  (1-3) ", align = "center", font = ("Courier New", 15, "normal"))
input = slow_print("Pick a number, 1-3.", 0.01)
item_randomizer(input)






    
if game == "on":
    pen.hideturtle()
    pen.goto(0,-250)
    pen.write("Use WASD to move!", align = "center", font = ("Courier New", 20, "normal"))

pen.hideturtle()
turtle.done()


#A DOORWAY!!
#p.showturtle()
#p.goto(0, 0)
#p.fillcolor("green")  #why is there not a light green  :<
#p.color("green")   #but that's a syntax error of a cmd...
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
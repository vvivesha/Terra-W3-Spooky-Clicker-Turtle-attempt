#moved import turtle down to delay the opening of the turtle window
import time
from time import sleep
import random
mystery_item = "unchosen"
game = "off"
mystery_item_chosen = "false"
upgrade_option = 0
stress = 100        #(of 100 max)
engagement_level = 0
#stats:
hype = 0
upkeep = 30  #this is your budget for upgrades; currently 30% of all earnings before uptime bills (yes, we will bill you for using our hosting services). You start off with $30 bucks!
morale = 50  #(you are stressed out.)
earnings = 0  #what matters in the end; it is spent on your Halloween costume.

def slow_print(text, delay):
    for letter in text:
        print(letter, flush = True, end = "")
        sleep(delay)

import turtle
#turtles:
pen = turtle.Turtle()
p = turtle.Turtle()

def upgrade_store(enter_or_exit):
    #------- - -- - -- - -- - -- -
    pen.penup()
    pen.goto(-200, 200)
    pen.pendown()
    pen.write("Upgrades Store!", align = "left", font = ("Impact", 30, "bold"))   #store title
    pen.penup()
    pen.setheading(0)
    pen.goto(-210, 195)  #store title underline dashed
    #pen.clear()
    #p.clear()
    for formatting in range(8):
        pen.pendown()
        pen.forward(25)
        pen.penup()
        pen.forward(25)
    pen.penup()
    #store's contents:
    pen.penup()
    pen.goto(0, 20)  #not sure of this part just yet
    pen.color("black")
   #------------------------------------
    pen.right(90)
    pen.forward(200)
    #===================================
    pen.setheading(0)
    pen.pendown()
    pen.fillcolor("white")
    pen.begin_fill()
    pen.forward(150)
    pen.left(90)
    pen.forward(300)
    pen.left(90)
    pen.forward(300)
    pen.left(90)
    pen.forward(300)
    pen.left(90)
    pen.forward(150)
    pen.end_fill()
    pen.penup()
    pen.forward(150)
    pen.left(90)
    pen.forward(170)
    pen.pendown()
    pen.fillcolor("green")
    pen.begin_fill()
    pen.right(120) #first angle of acute triangle "view next upgrade" button thingy
    pen.forward(30)
    pen.right(120)
    pen.forward(30)
    pen.right(120)
    pen.forward(30)
    pen.end_fill() #end of the triangle next button thingy
    pen.penup()
    pen.setheading(0)
    pen.right(90)
    pen.forward(30)
    pen.left(90)
    pen.forward(10)
    pen.setheading(0)
    pen.right(180)
    pen.forward(30)
    pen.write("Press n", align = "right", font = ("Courier New", 15, "normal"))  #keyboard button "n" triggers showing the next upgrade.
    pen.setheading(0)
    pen.goto(0, 0)
    pen.right(90)
    pen.forward(50)
    pen.pendown()
    pen.color("black")
    pen.setheading(0)
    pen.right(180)
    pen.forward(100)
    pen.right(90)
    pen.forward(50)
    pen.write("Buy it: gain 10 hype!", align = "left", font = ("Courier New", 15, "normal"))
    pen.penup()
    pen.goto(0, -200)
    #store's contents:
    pen.penup()
    pen.goto(0, 20)  #not sure of this part just yet
    pen.color("black")
    pen.pendown()
    pen.write("Dark/Light mode option: ", align = "center", font = ("Courier New", 15, "underline"))
    pen.penup()
    pen.right(90)
    pen.forward(200)
    #===================================
    pen.penup()
    pen.setheading(0)
    pen.goto(0, 0)
    pen.right(90)
    pen.forward(200)
    pen.showturtle() #temporarily
    turtle.bgcolor("black")
    pen.color("orange")
    pen.pendown()
    pen.write(enter_or_exit + "ed store. Your budget is: $" + str(upkeep))
    pen.penup()

def next_upgrade():
    global upgrade_option
    global engagement_level
    global hype
    global stress
    global upkeep
    if upgrade_option > 3:
        upgrade_option = 0
    if upgrade_option == 1:
        if upkeep >= 5:
            #Engagement upgrade level goes up
            engagement_level += 1
            upkeep -= 5
            if engagement_level in [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]:
                hype += 10
                p.showturtle()
                p.goto(0, -200)
                p.color("blue")
                p.write("+ 10 hype!", align = "center", font = ("Impact", 15, "underline"))
                return
            else:
                p.showturtle()
                p.goto(0, -200)
                p.color("blue")
                p.write("Upgrade purchased!", align = "center", font = ("Courier New", 15, "normal"))
                return
        else:
            p.showturtle()
            p.goto(0, -200)
            p.color("red")
            p.write("Insufficient funds. See terminal for more details.", align = "center", font = ("Courier New", 15, "underline"))
            print("<You can\'t afford this upgrade!!>")
            poor_by = 5 - upkeep
            print("*You need $" + poor_by + " more upkeep money*")
            return
    if upgrade_option == 2:
        if upkeep >= 12:
            #Offline-able clicker upgrade level goes up
            upkeep -= 12
            stress -=10
            p.showturtle()
            p.goto(0, -200)
            p.color("blue")
            p.write("+ 10 morale and hype!", align = "center", font = ("Impact", 15, "underline"))
            return
        else:
            p.showturtle()
            p.goto(0, -200)
            p.color("red")
            p.write("Insufficient funds. See terminal for more details.", align = "center", font = ("Courier New", 15, "underline"))
            print("<You can\'t afford this!")
            poor_by = 12 - upkeep
            print("*You need $" + poor_by + " more upkeep money*")


    #["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    

turtle.Screen().onkey(next_upgrade, "n")
turtle.Screen().listen()

#commented out this because it is no longer needed for this week's version of this project. (clutters the turtle window, too)
#def game_on():
   # global game
   # game = "on"
   # print("<game has begun>")
   # turtle.bgcolor("gray")
   # p.showturtle()
   # time.sleep(0.2)
   # p.setheading(0)
   # seconds = 4
   # p.color("red")
  #  for countdown in range(3):
   #     p.clear()
    #    p.color("red")
   #     seconds -= 1
    #    p.hideturtle()
     #   p.color("white")
   #     p.goto(0, -100)
   #     p.write(str(seconds), align = "center", font = ("Impact", 100, "bold"))
  #  time.sleep(4.2)
   #     #item_randomizer()

        

turtle.Screen().onkey(upgrade_store, "q")
turtle.Screen().listen()



time.sleep(1.5)
slow_print("WELCOME TO.. ", 0.1)
print(" ")
slow_print("𓄿  Make-a-Sp00ky-Clicker-App-So-You-Can-Buy-a-Good-Costume-for ☠︎︎  Halloween ☠︎︎   Simulator  𓆙", 0.08)
print(" ")
print("<You have the option to make the intro go be rapidly, or a bit more slowly>")
time.sleep(0.5)
fast_mode = input("Enable fast mode?  Type: (y/n)")
if fast_mode in ["y", "Y"]:
    wait_time = 1.5
    delay_time = 0.01
    print(" ")
    slow_print("<Get ready!>", delay_time)
if fast_mode in ["n", "N"]:
    wait_time = 2.5
    delay_time = 0.1
    print(" ")
    slow_print("<Alright, we'll take it a bit slower>", delay_time)
for gap in range(5):
    print(" ")
time.sleep(1.5)
slow_print("Think of this game like a tycoon!", delay_time)
print(" ")
slow_print("Your objective: ", delay_time)
print(" ")
slow_print("Make a Spooky Clicker app --> get $$$ --> buy yourself a costume!", delay_time)
time.sleep(wait_time)
print(" ")
time.sleep(0.1)
for gap in range(2):
    print(" ")
slow_print("Today is... Thursday, October 29th, 2026", delay_time)
print(" ")
time.sleep(wait_time)
print("Pssssst:  yep, you have THREE days before Halloween night. So you're definitely on a time crunch; good luck!!")
time.sleep(wait_time)

for gap in range(3):
    print(" ")

for gap in range(5):
    print("")

slow_print("You will recieve a Spooky Clicker window: it will be how you earn $$$ for your Halloween costume. You have...  7  days. Goodluck!", delay_time)
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
print("-->  2)  get a flashy marketing strategy")
print("=========================================")
for gap in range(3):
    print(" ")

plan = input("Option 1 or 2?  ")
time.sleep(wait_time)
if plan == "1":
    print(" ")
    print(" ")
    slow_print("You hit up all of your buddies at school. Nice that you spent time making the connections beforehand!", delay_time)
    hype = int(hype) + 15
if plan == "2":
    print(" ")
    print(" ")
    slow_print("Woah! Nice advertisements! ", delay_time)
input("<Press ENTER to see your stats>")



print(" ")
slow_print("Your current stats: ", 0.1)
for gap in range(3):
    print(" ")
slow_print("MORALE: " + str(morale), 0.01)
print(" ")
slow_print("UPKEEP: " + str(upkeep), 0.01)
print(" ")
slow_print("HYPE: " + str(hype), 0.01)
print(" ")
slow_print("EARNINGS: " + str(earnings), 0.01)

for gap in range(3):
    print(" ")

slow_print("STATS INFO:    (4 categories to keep track of)", delay_time)
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
time.sleep(wait_time)
print("You will start out with $0 under EARNINGS because you are spending your last $15 on getting this site up and going.")
input("<Press ENTER to continue>  (4/4)")
for gap in range(3):
    print(" ")
slow_print("<You have... $15.00>", 0.1)
print(" ")
slow_print("Now I\'m going to make you visit the store with me :>  ", delay_time)
print(" ")
print("redirecting you to upgrades store...")
store_visit = "y"
if store_visit == "y":
    upgrade_store("enter")
#while store_visit == "y":
   #buy = input("Pick a number, any number!  ")
    #if buy not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
   #     for gap in range(3):
    #        print(" ")
   # slow_print("HEY... stop messing with me, please!!", 0.1)
   # print(" ")
   # time.sleep(0.1)
  #  buy = input("Please pick an *acutal* option, and THEN we can discuss purchasing that upgrade.  ")







def customer_screen():
#switched over the VS Code app to code from this point on.
    turtle.bgcolor("black")
    print("Customer's screen ===>  Welcome to Spooky Clicker! Check out the separate window to see the visuals :>")
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

def play_pressed():
    play_triggered = "yes"
    print("<pressed play>")
    game_on()
    p.clear()

#turtle.Screen().listen()
turtle.Screen().onkey(play_pressed, "p")  #so apparently it is case-sensitive to the point that a "P" would expect shift + P to activate the code...
turtle.Screen().listen()




#add a green border-flash for fun if time allows!!


#got rid  of a useless def function because it was jumbling up on the turtle output window.


#pen.write("Check the terminal and input a number. Then, return to this window  :)  (1-3) ", align = "center", font = ("Courier New", 15, "normal"))
#input = slow_print("Pick a number, 1-3.", 0.01)
#item_randomizer(input)






    
#if game == "on":
  #  pen.hideturtle()
   # pen.goto(0,-250)
  #  pen.write("Use WASD to move!", align = "center", font = ("Courier New", 20, "normal"))

pen.hideturtle()
turtle.done()



#imports
import turtle
import time

#defining 
t = turtle.Turtle()
t.shape("turtle")
t.penup()
t.hideturtle()

#start screen
def stats(lvl, chance):
    t.setposition(-275,245)
    t.write(f"Lvl: {lvl}", align ="right")
    t.setposition(-205,230)
    t.write(f"chance of falling:{chance}%", align= "right")

#intro
stats(0, 0)
t.goto(-225,100)
t.write("Welcome to Card Tower! Answer questions to increase your chances of completing your tower!")
t.pendown()
t.forward(475)
t.right(360)
t.penup()
time.sleep(3)
t.clear()

#start



#outside card
def outside_card():
    t.pendown()
    t.left(145)
    t.forward(50)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(100)
    t.left(180)
    t.forward(100)
    t.right(125)
    t.penup()
    
def inside_a():
    t.pendown()
    t.forward(80)
    t.right(135)
    t.forward(50)
    t.right(45)
    t.forward(20)
    t.penup()
    t.right(56)
    t.forward(45)
    t.right(125)
    t.forward(80)
    
    t.penup()
    
    
    
def inside_b():
    t.pendown()
    t.left(130)
    t.forward(100)
    t.left(130)
    t.penup()
  
    
def top():
    t.pendown()
    t.forward(80)
    t.right(45)
    t.forward(50)
    t.right(135)
    t.forward(80)
    t.right(45)
    t.forward(50)
    t.right(31)
    t.penup()

def rewrite_stats():
    t.goto(-275,245)
    t.pendown()
    t.color("white")
    t.left(10)
    t.pensize(100)
    t.forward(100)
    t.penup()
    t.pensize(1)
    t.color("black")

def clear_text():
    t.penup()
    t.goto(0,100)
    t.pensize(100)
    t.color("white")
    t.pendown()
    t.setheading(0)
    t.forward(300)
    t.penup()
    t.pensize(1)
    t.pencolor("black")
    
def per_check(percentage):
    score = percentage
    if score >= 100:
        t.clear()
        t.goto(-100, 0)
        t.write("GAME OVER", font= ("Veranda", 15, "normal"))
        time.sleep(3)
        quit()
    
    
    
#Start #####################################################################################################################    
percentage = 0
level = 0
stats(level, percentage)

t.goto(125,100)

################################################question 1################################################
level =1

t.write("question 1: what is 1 + 1?")
answer = int(input("type your answer here:"))
if answer == 2:
    print("Correct!")
    percentage = percentage + 0
else:
    percentage = percentage + 3
    ("Wrong")
time.sleep(3)
rewrite_stats()
stats(level, percentage)
per_check(percentage)
clear_text()

#card 1
t.goto(-225, -125)
t.color("blue")
outside_card()

################################question 2##########################################################
level = 1

t.goto(0,100)
t.color("black")
t.write("question 2: what the capital of Ireland?")
answer = input("type your answer here:")
if answer == "Cork":
    print("Correct!")
    percentage = percentage + 0
else:
    percentage = percentage + 5
    print("Wrong, its actually Cork ._.")
time.sleep(3)
rewrite_stats()
stats(level, percentage)
per_check(percentage)
clear_text()

#card2
t.right(70)
t.goto(-169,-43)
t.color("red")
inside_a()

################################question 3###########################################
level = 1

t.goto(0,100)
t.color("black")
t.write("question 3: what is Sinead's middle name?")
answer = input("type your answer here:")
if answer == "Mary":
    print("Correct!")
    percentage = percentage + 0
else:
    percentage = percentage + 5
    print("Wrong, its Mary (#fake friend)")
time.sleep(3)
rewrite_stats()
stats(level, percentage)
per_check(percentage)
clear_text()

#card 3
t.right(70)
t.goto(-142,-120)
t.color("blue")
inside_b()

#########################question 4#######################
level = 1

t.goto(0,100)
t.color("black")
t.write("question 4: how many months of the year have 28 days?")
answer = int(input("type your answer here(in number format):"))
if answer == 12:
    print("Correct!")
    percentage = percentage + 0
else:
    percentage = percentage + 5
    print("Wrong, all of them (12)")
time.sleep(3)
rewrite_stats()
stats(level, percentage)
per_check(percentage)
clear_text()

#card 4
t.right(170)
t.goto(-90,-30)
top()

############################question 5###################################################
level = 1

t.goto(0,100)
t.color("black")
t.write("question 5: what is the best animal?")
answer = input("type your answer here:")
if answer == "jaguar":
    print("Correct!")
    percentage = percentage + 0
else:
    percentage = percentage + 5
    print("Wrong, the answer was jaguar")
time.sleep(3)
rewrite_stats()
stats(level, percentage)
per_check(percentage)
clear_text()

#card 4
5
t.right(65)
t.goto(-90,-30)
t.color("red")
inside_a()

############################question 6###################################################
level = 1

t.goto(0,100)
t.color("black")
t.write("question 6: what is 2^10")
answer = int(input("type your answer here:"))
if answer == 1024:
    print("Correct!")
    percentage = percentage + 0
else:
    percentage = percentage + 5
    print("Wrong, the answer was 1024")
time.sleep(3)
rewrite_stats()
stats(level, percentage)
per_check(percentage)
clear_text()

#card 6
5
t.right(65)
t.goto(-58,-102)
t.color("blue")
inside_b()


############################question 7###################################################
level = 1

t.goto(-20,100)
t.color("black")
t.write("question 7: David’s father has three sons: Snap, Crackle, and _________?")
answer = input("type your answer here:")
if answer == "David":
    print("Correct!")
    percentage = percentage + 0
else:
    percentage = percentage + 5
    print("Wrong, its David")
time.sleep(3)
rewrite_stats()
stats(level, percentage)
per_check(percentage)
clear_text()

#card 7
t.right(168)
t.goto(-18,-11)
top()



############################question 8###################################################
level = 1

t.goto(0,100)
t.color("black")
t.write("question 8: what gets wet while drying?")
answer = input("type your answer here(answer format:* *****):")
if answer == "a towel":
    print("Correct!")
    percentage = percentage + 0
else:
    percentage = percentage + 5
    print("Wrong, the answer is a towel")
time.sleep(3)
rewrite_stats()
stats(level, percentage)
per_check(percentage)
clear_text()

#card 8
t.right(60)
t.goto(-18,-11)
t.color("red")
inside_a()

############################question 9 ###################################################
level = 1
"""
t.goto(125,100)
t.color("black")
t.write("question 9: what is 12 + 3?")
answer = int(input("type your answer here:"))
if answer == 15:
    print("Correct!")
    percentage = percentage + 0
else:
    percentage = percentage + 3
    print("Wrong")
time.sleep(3)
rewrite_stats()
stats(level, percentage)

clear_text()

#card 9
t.right(65)
t.goto(20,-83)
t.color("blue")
inside_b()
"""

############################question 10 ###################################################
level = 1
"""
t.goto(125,100)
t.color("black")
t.write("question 10: what is 14 + 3?")
answer = int(input("type your answer here:"))
if answer == 17:
    print("Correct!")
    percentage = percentage + 0
else:
    percentage = percentage + 3
    print("Wrong")
time.sleep(3)
rewrite_stats()
stats(level, percentage)

clear_text()

#card 10
t.right(167)
t.goto(60,5)
top()
"""

############################question 11 ###################################################
level = 1
"""
t.goto(125,100)
t.color("black")
t.write("question 11: what is 17 + 3?")
answer = int(input("type your answer here:"))
if answer == 20:
    print("Correct!")
    percentage = percentage + 0
else:
    percentage = percentage + 3
    print("Wrong")
time.sleep(3)
rewrite_stats()
stats(level, percentage)

clear_text()

#card 10
t.right(58)
t.goto(60,5)
t.color("red")
inside_a()
"""

############################question 9 ###################################################
level = 2
percentage = percentage + 20
t.goto(0,100)
t.color("black")
t.write("question 9: what was the answer to question 2")
answer = input("type your answer here:")
if answer == "Cork":
    print("Correct!")
    percentage = percentage + 0
else:
    percentage = percentage + 15
    print("Wrong, the answer was Cork")
time.sleep(3)
rewrite_stats()
stats(level, percentage)
per_check(percentage)
clear_text()

#card 10
t.left(178)
t.goto(-150, 68)
t.color("blue")
outside_card()

############################question 10 ###################################################
level = 2

t.goto(-200,100)
t.color("black")
t.write("question 10: What 4-letter word can be written forward, backward, or upside down, and can still be read from left to right?")
answer = input("type your answer here(in capital letters):")
if answer == "NOON":
    print("Correct!")
    percentage = percentage + 0
else:
    percentage = percentage + 5
    print("Wrong, the answer is NOON")
time.sleep(3)
rewrite_stats()
stats(level, percentage)
per_check(percentage)
t.goto(-200,100)
t.pendown()
t.color("white")
t.setheading(0)
t.pensize(25)
t.forward(200)
t.penup()
clear_text()

#card 10
t.right(70)
t.goto(-113, 45)
t.color("red")
inside_a()
#t.goto(0,0)

############################question 11 ###################################################
level = 2

t.goto(0,100)
t.color("black")
t.write("question 11: what is a hundred plus another hundred?")
answer = int(input("type your answer here:"))
if answer == 200 :
    print("Correct!")
    percentage = percentage + 0
else:
    percentage = percentage + 15
    print("Wrong, the answer is 200")
time.sleep(3)
rewrite_stats()
stats(level, percentage)
per_check(percentage)
clear_text()

#card 10
t.right(69)
t.goto(-90, -25)
t.color("blue")
inside_b()
#t.goto(0,0)
#################################qurstion 12##################################
level = 2

t.goto(0,100)
t.color("black")
t.write("question 12: what has a head and tail but no body?")
answer = input("type your answer here(answer format: * ****):")
if answer == "a coin":
    print("Correct!")
    percentage = percentage + 0
else:
    percentage = percentage + 15
    print("Wrong, the answer is a coin")
time.sleep(3)
rewrite_stats()
stats(level, percentage)
per_check(percentage)
clear_text()

#card 10
t.right(70)
t.goto(-40, 60)
t.color("red")
inside_a()
#t.goto(0,0)

#################################qurstion 13##################################
level = 2
t.goto(0,100)
t.color("black")
t.write("question 13: what always ends everything?")
answer = input("type your answer here:")
if answer == "g":
    print("Correct!")
    percentage = percentage + 0
else:
    percentage = percentage + 15
    print("Wrong, the answer is g")
time.sleep(3)
rewrite_stats()
stats(level, percentage)
per_check(percentage)
clear_text()

#card 10
t.right(170)
t.goto(-38, 57)
t.color("black")
top()
#t.goto(0,0)

#################################qurstion 14##################################
level = 3
percentage = percentage + 10
t.goto(-250,100)
t.color("black")
t.write("question 14: The man who invented it doesn’t need it. The man who bought it doesn’t want it. What is it?")
answer = input("type your answer here(answer format: * ******):")
if answer == "a coffin":
    print("Correct!")
    percentage = percentage + 0
else:
    percentage = percentage + 25
    print("Wrong, the answer is a coffin")
time.sleep(3)
rewrite_stats()
stats(level, percentage)
per_check(percentage)
t.goto(-250,100)
t.pendown()
t.color("white")
t.pensize(20)
t.setheading(0)
t.forward(300)
t.color("white")
t.penup()
clear_text()

#card 10
t.right(180)
t.goto(-100, 153)
t.color("blue")
outside_card()
#t.goto(0,0)

################################qurstion 15##################################
level = 3
t.goto(0,100)
t.color("black")
t.write("question 15: what kind of band never plays music?")
answer = input("type your answer here(answer format: * ****** ****:")
if answer == "a rubber band":
    print("Correct!")
    percentage = percentage + 0
else:
    percentage = percentage + 25
    print("Wrong, the naswer was a rubber band")
time.sleep(3)
rewrite_stats()
stats(level, percentage)
per_check(percentage)
clear_text()

#card 10
t.right(75)
t.goto(-60, 127)
t.color("red")
t.pendown()
t.forward(80)
t.right(45)

t.clear()
t.penup()
t.color("black")
t.goto(-50,0)
time.sleep(3)
t.write("YOU WIN!!!!!!",font= ("Veranda", 15, "normal"))
 

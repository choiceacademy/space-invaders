#space_invaders.py
import time
from datetime import datetime
import turtle
import os
import math    
import random
import winsound
import csv

minutes = 0
seconds = 0
# get current time
start = time.time()

#set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.bgpic("space_invaders_background.gif")

#define the gaem over turtle
game_over = turtle.Turtle()
			
#register the shapes
turtle.register_shape("invader.gif")
turtle.register_shape("player.gif")
#draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)

for side in range(4):
	border_pen.fd(600)
	border_pen.lt(90)
border_pen.hideturtle() 

#Ask the player's name
name = turtle.textinput("Enter your name" , "What is your name?")

file = open('top_three.txt','r')
str1 = file.read();
file.close()
leng=len(str1)-1
ln = str1.index(",")
name1 = str1[0:ln]
score1 = str1[ln+1:leng+1]
high_score = int(score1)
print (name1 , high_score)
#set the score to 0
score = 0

#draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-270,260)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

#create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0,-250)
#set the player pointing up
player.setheading(90)

#declare player speed
playerspeed = 20

#chose number of enemies 
number_of_enemies = 5
#create an empty list of enimies
enemies = []
#add enemies to the list
for i in range(number_of_enemies):
	#create the enemy
	enemies.append(turtle.Turtle())

#for all enemies, do the following	
for enemy in enemies:
	enemy.color("red")
	enemy.shape("invader.gif")
	enemy.penup()
	enemy.speed(0)
	x = random.randint(-200,200)
	y = random.randint(100,250)
	enemy.setposition(x,y)

#declare enemy speed
enemyspeed = 10

#create the player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 150

#define bullet state
#ready - ready to fire
#fire - bullet is firing
bulletstate = "ready"

#move the player left and right
def move_left():
        #idenify current x cordinate of player and move over playerspeed value
	x = player.xcor()
	x -= playerspeed
	#set left boundary
	if x < -280:
		x = -280
	player.setx(x)

def move_right():
	#idenify current x cordinate of player and move over playerspeed value
	x = player.xcor()
	x += playerspeed
	#set right boundary
	if x > 280:
		x = 280
	player.setx(x)
	return
def fire_bullet():
	#declare bullet state as global if it needs to be changed 
	global bulletstate
	if bulletstate == "ready":
		bulletstate = "fire"
		#move the bullet to just above the player
		x = player.xcor()
		y = player.ycor() 
		bullet.setposition(x,y + 10)
		bullet.showturtle()
	return
#create collisions for bullet and enemy
def isCollision(t1, t2):
	distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
	if distance < 30:
		return True
	else:
		return False

#create keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet,"space")

#main game loop
while True:
	for enemy in enemies:
		#move enemy
		x = enemy.xcor()
		x += enemyspeed
		enemy.setx(x)
		
		#move the enemy back and down
		if enemy.xcor() > 280:
			for e in enemies:
				y = e.ycor()
				y -= 40
				e.sety(y)
			enemyspeed *= -1
                        
		if enemy.xcor() < -280:
			for e in enemies:
				y = e.ycor()
				y -= 40
				e.sety(y)
			enemyspeed*= -1
			
		#Check for a collision between a bullet and the enemy
		if isCollision(bullet, enemy):
			#reset the bullet
			bullet.hideturtle()
			bulletstate = "ready"
			bullet.setposition(0,-400)
			#reset the enemy
			enemy.setposition(-200,230)
			winsound.PlaySound("cannon_x", winsound.SND_ASYNC | winsound.SND_ALIAS) 
			#update the score
			score += 10
			scorestring = "Score: %s" %score
			score_pen.clear()
			score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal")) 
			
		if isCollision(player,enemy) or enemy.ycor() < -280:
			player.hideturtle()
			bullet.hideturtle()
			game_over.hideturtle()
			for e in enemies:
				e.hideturtle()
			game_over.goto(0,-100)
			game_over.speed("fastest")
			game_over.pencolor("white")
			s = ("Game Over\nScore = ") + str(score)
			highlist = [  ["Julie", 30], ["Jim", 20], ["Jasmine", 10] ]
			winner = [name, score]
			victory = 0
			for i in range(0,3):
				if(score > highlist[i][1]):
				#insert your name and score here. insert winner into highlist
					highlist.insert(i,winner)
					victory = 1
					print("You set a high score!!!")
					print("Name =", name.title(), " Your score is:" , score)
					break
			if victory == 1:
				file = open('top_three.txt','w')
				for i in range(0,3):
					str1 = highlist[i][0] + "," + str(highlist[i][1])
					file.write(str1)
				file.close()
			else:
				print("You didn't set the high score. Better luck next time! (The current high scores are above.)" )
			
			winsound.PlaySound("fanfare2.wav", winsound.SND_FILENAME)
			game_over.write(s, align="center", font=("Calibri", 70))
			#  end of program
			seconds = time.time() - start
			# show the time stamp
			now = datetime.now()
			print("The current date and time is:",now)
			# print the time difference in minutes and seconds
			print('Your game time is = %7.2f' % seconds,"seconds")
			time.sleep(5)
			quit()
			
	#move the bullet
	if bulletstate == "fire":
		y = bullet.ycor()
		y += bulletspeed
		bullet.sety(y)

	#check to see if the bullet has gone to the top
	if bullet.ycor()> 275:
		bullet.hideturtle()
		bulletstate = "ready"


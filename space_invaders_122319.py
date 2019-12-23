#space_invaders.py
import time
import turtle
import os
import math    
import random
#set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")

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

#create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
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
	enemy.shape("circle")
	enemy.penup()
	enemy.speed(0)
	x = random.randint(-200,200)
	y = random.randint(100,250)
	enemy.setposition(x,y)

#declare enemy speed
enemyspeed = 2

#create the player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 30

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
	
#create collisions for bullet and enemy
def isCollision(t1, t2):
	distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
	if distance < 15:
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
			enemyspeed *= -1
			y = enemy.ycor()
			y -= 40
			enemy.sety(y)
			

		if enemy.xcor() < -280:
			enemyspeed*= -1
			y = enemy.ycor()
			y -= 40
			enemy.sety(y)
			
			
		#Check for a collision between a bullet and the enemy
		if isCollision(bullet, enemy):
			#reset the bullet
			bullet.hideturtle()
			bulletstate = "ready"
			bullet.setposition(0,-400)
			#reset the enemy
			enemy.setposition(-200,230)
				
		if isCollision(player,enemy):
			player.hideturtle()
			enemy.hideturtle()
			player.goto(0,-50)
			colors=['red', 'black']
			player.speed("fastest")
			for j in range (20):
				for c in colors:
					player.pencolor(c)
					time.sleep(0.01)
					player.write("Game Over", align="center", font=("Arial", 80, "bold"))
			breakpoint


	#move the bullet
	if bulletstate == "fire":
		y = bullet.ycor()
		y += bulletspeed
		bullet.sety(y)

	#check to see if the bullet has gone to the top
	if bullet.ycor()> 275:
		bullet.hideturtle()
		bulletstate = "ready"
			




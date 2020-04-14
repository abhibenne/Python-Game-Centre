import turtle
import time
import random
delay=.1
segments=[]
score=0
high_score=0
w=turtle.Screen()
w.title("My Snake Game")
w.bgcolor("green")
w.setup(width=600,height=500)
w.tracer(0)#Cant update or refresh screen
#Pen-written content,also turtle tegobeku
pen=turtle.Turtle()
pen.shape("square")
pen.speed(0)
pen.color("white")
pen.hideturtle()
pen.penup()
pen.goto(0,200)
pen.write("Score:0 High Score:0",align="center",font=("Courier",24,"normal"))

#Snake Head
head=turtle.Turtle()
head.shape("square")
head.color("black")
head.speed(0)
head.goto(0,0)
head.penup() #line baratte or else
head.direction="stop"


#Snake Food
food=turtle.Turtle()
food.shape("circle")
food.color("red")
food.speed(0)
food.penup() #before go to else a line will come
food.goto(random.randint(-290,290),random.randint(-240,240))


#Functions 
def move_it():
	if head.direction=="up":
		y=head.ycor()
		head.sety(y+20)
	if head.direction=="down":
		y=head.ycor()
		head.sety(y-20)
	if head.direction=="left":
		x=head.xcor()
		head.setx(x-20)
	if head.direction=="right":
		x=head.xcor()
		head.setx(x+20)
def up():
	if head.direction !="down":
		head.direction="up"
def down():
	if head.direction!="up":
		head.direction="down"
def left():
	if head.direction!="right":
		head.direction="left"
def right():
	if head.direction!="left":
		head.direction="right"
def quit():
	pen.hideturtle()
	head.hideturtle()
	food.hideturtle()
	turtle.bye()
	w.bye()
#keyboard entering
w.listen()
w.onkeypress(up,"Up")#can be w also,but for cursor it is Up
w.onkeypress(down,"Down")
w.onkeypress(left,"Left")
w.onkeypress(right,"Right")
w.onkeypress(quit,"q")

while True:
	w.update()
	#checking for collision with food
	if head.distance(food)<20:
		x=random.randint(-290,290)
		y=random.randint(-240,240)
		food.goto(x,y)
		#new segment should appear
		new=turtle.Turtle()
		new.shape("square")
		new.color("grey")
		new.speed(0)
		new.penup()
		segments.append(new)
		#increase difficuty as food increases,so delay time increased
		delay-=.001
		score+=10
		if score>high_score:
			high_score=score
		pen.clear()
		pen.write("Score:{} High Score:{}".format(score,high_score),align="center",font=("Courier",24,"normal"))
	#move last segment to before one for continuous tail
	for i in range(len(segments)-1,0,-1):
		x=segments[i-1].xcor()
		y=segments[i-1].ycor()
		segments[i].goto(x,y)
	#moving segment 0 each time to where head is there
	if len(segments)>0:
		x=head.xcor()
		y=head.ycor()
		segments[0].goto(x,y)
	
	if head.xcor()>290 or head.ycor()>240 or head.ycor()<-240 or head.xcor()<-290:
		time.sleep(1)
		head.goto(0,0)
		head.direction="stop"
		for segment in segments:
			segment.goto(1000,1000)
		segments.clear()
		score=0
		pen.clear()
		pen.write("Score:{} High Score:{}".format(score,high_score),align="center",font=("Courier",24,"normal"))
	move_it()
	#collsion with body part
	for segment in segments:
		if segment.distance(head) < 20:
			time.sleep(1)
			head.goto(0,0)
			head.direction="stop"
			for segment in segments:
				segment.goto(1000,1000)
			segments.clear()
			score=0
			pen.clear()
			pen.write("Score:{} High Score:{}".format(score,high_score),align="center",font=("Courier",24,"normal"))
	time.sleep(delay)
w.mainloop()
import pygame
import time
import random
pygame.init()
#crash_sound=pygame.mixer.Sound("carstarthonkbackfire.mp3")
#pygame.mixer.music.load("Dee_Yan-Key_-_18_-_Good_Bye.mp3")
#display width and height of screen
w=800
h=600
#from image at hand
car_w=125
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
green=(0,200,0)
light_green=(0,255,0)
light_blue=(0,0,255)
blue=(0,0,150)
l=[black,red,green,blue,light_blue]
#setting window-pass tuple
disp_game=pygame.display.set_mode((w,h))
clock=pygame.time.Clock()
high_score=0
carimg=pygame.image.load("car3.png")
pause=False
def car(x,y):
	disp_game.blit(carimg,(x,y))
def quitgame():
	pygame.quit()
#creates text with button
def button(msg,x,y,w,h,ic,ac,action=None):
	mouse=pygame.mouse.get_pos()
	click=pygame.mouse.get_pressed()
	if (x+w) > mouse[0] > x and y+h > mouse[1] > y:
		pygame.draw.rect(disp_game,ac,(x,y,w,h))
		if click[0]==1 and action:
			action()
		"""	if action=="play":
				game_loop()
			if action=="quit":
				pygame.quit()
				quit()"""
	else:
		pygame.draw.rect(disp_game,ic,(x,y,w,h))
	small_text=pygame.font.SysFont("comicsansms",20)
	textsurf,textrect=text_object(msg,small_text)
	textrect.center=(x+(w/2),y+(h/2))
	disp_game.blit(textsurf,textrect)
#create blocks and place them at different spots
#same name inside function,can change tho
def blocks(bx,by,bh,bw,color):
	pygame.draw.rect(disp_game,color,[bx,by,bw,bh])
def text_object(text,font):
	text_surf=font.render(text,True,red)
	return text_surf,text_surf.get_rect()
def crash():
	#pygame.mixer.music.stop()
	#pygame.mixer.Sound.play(crash_sound)
	#disp_game.fill(white)
	text_type=pygame.font.SysFont("comicsansms", 72)
	surface,rectangle=text_object("You Crashed",text_type)
	rectangle.center=(w/2,h/2)
	disp_game.blit(surface,rectangle)
	while True:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
		button("Play Again",150,380,100,50,green,light_green,game_loop)
		button("Quit",500,380,100,50,blue,light_blue,quitgame)

		pygame.display.update()
		clock.tick(10)
"""def Message(text):
	text_type=pygame.font.SysFont("comicsansms", 72)
	surface,rectangle=text_object(text,text_type)
	rectangle.center=(w/2,h/2)
	disp_game.blit(surface,rectangle)
	pygame.display.update()
	time.sleep(3)

	game_loop()"""
def scoring(s,hs):
	font=pygame.font.Font(None,20)
	text=font.render("Score : "+str(s)+" High Score : "+str(hs),True,black)
	disp_game.blit(text,(0,0))
def intro():
	intro=True
	while intro:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
		disp_game.fill(white)
		text_type=pygame.font.SysFont("comicsansms", 72)
		surface,rectangle=text_object("Best racing car game",text_type)
		rectangle.center=(w/2,h/2)
		disp_game.blit(surface,rectangle)
		""" mouse=pygame.mouse.get_pos()
			if (150+100) > mouse[0] > 150 and 380+50 > mouse[1] > 380:
				pygame.draw.rect(disp_game,light_green,(150,380,100,50))
			else:
				pygame.draw.rect(disp_game,green,(150,380,100,50))
			if (500+100) > mouse[0] > 500 and 380+50 > mouse[1] > 380:
				pygame.draw.rect(disp_game,light_blue,(500,380,100,50))
			else:
				pygame.draw.rect(disp_game,blue,(500,380,100,50))
			small_text=pygame.font.SysFont("comicsansms",20)
			textsurf,textrect=text_object("GO!",small_text)
			textrect.center=(150+50,380+25)
			disp_game.blit(textsurf,textrect)"""
		button("GO!",150,380,100,50,green,light_green,game_loop)
		button("Quit",500,380,100,50,blue,light_blue,quitgame)
		pygame.display.update()
		clock.tick(10)
def unpause():
	global pause
	pygame.mixer.music.unpause()
	pause=False
def paused():
	#pygame.mixer.music.pause()
	disp_game.fill(white)
	text_type=pygame.font.SysFont("comicsansms", 72)
	surface,rectangle=text_object("Paused",text_type)
	rectangle.center=(w/2,h/2)
	disp_game.blit(surface,rectangle)
	global pause
	while pause:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
		button("Continue",150,380,100,50,green,light_green,unpause)
		button("Quit",500,380,100,50,blue,light_blue,quitgame)
		pygame.display.update()
		clock.tick(10)
def game_loop():
	global pause
	#plays indefinetly if -1
	#pygame.mixer.music.play(-1)
	x=w*.45
	y=h*.7
	x_change=0
	bx=random.uniform(0,w)
	by=-300
	#initialize score
	score=0
	global high_score
	#speed of block
	speed=5
	bw=75
	bh=75
	color=random.choice(l)
	game_exit=False
	pygame.display.set_caption("Racer")
	while not game_exit:
		for event in pygame.event.get():
			if event== pygame.QUIT:
				pygame.quit()
				quit()
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_LEFT:
					x_change=-5
				if event.key==pygame.K_RIGHT:
					x_change=5
				if event.key==pygame.K_p:
					pause=True
					paused()
			if event.type==pygame.KEYUP:
				if event.key==pygame.K_LEFT:
					x_change=0
				if event.key==pygame.K_RIGHT:
					x_change=0
		x+=x_change
		"""This also wrks fine
		if x>(w*.87) or x<(0-somepart):
			crash=True
                        print("Crashed")"""
		
		#without any parameter updates all frames ,with parameter only updates that.Can use flip also ,it updates all only
		#updates 60 frames in a second 
		disp_game.fill(white)
		blocks(bx,by,bh,bw,color)
		by+=speed
		car(x,y)
		scoring(score,high_score)
		if x>(w-car_w) or x<(0-car_w*.1):
			crash()
		if by>h:
			by=0-bh
			bx=random.uniform(0,w)
			color=random.choice(l)
			score+=1
			if score> high_score:
				high_score=score
			speed+=.1
			if score>10:
				bw+=speed*.5
		#COLLISION Logic
		#x is the left and topmost point and so is y, i took two if loops and found out if bth x or both y is intersecting or not
		#original logic i wrote,can be simplified as :
		#if y<(by+bh) and (x>(bx) and x<(bx+bw)): 
		#	print("collision") 
		#if y<(by+bh) and ((x+car_w)>(bx) and (x+car_w)<(bx+bw)):
		#	print("again collision")
		#if y<(by+bh) and x+(car_w/2)>bx and x+(car_w/2)<(bx+bw) :
		#	print("mid collision")
		if y<(by+bh):
			if (x>(bx) and x<(bx+bw)) or ((x+car_w)>(bx) and (x+car_w)<(bx+bw)) or x+(car_w/2)>bx and x+(car_w/2)<(bx+bw):
				print("collision")
				crash()
		pygame.display.update()
		clock.tick(60)
intro()
game_loop()
pygame.quit()

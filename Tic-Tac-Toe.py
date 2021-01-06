''' Source code owned by Seth Whalen @smwhalen94 '''
''' Written on 05/29/2018 - 05/31/18 '''

import turtle
import time
#import emoji
from random import randint

turtle.speed(0)
turtle.hideturtle()

##############Simplifying Turtle functions#############
def left(angle):
	turtle.left(angle)
	return
def right(angle):
	turtle.right(angle)
	return
def forward(length):
	turtle.forward(length)
	return
def back(length):
	turtle.backward(length)
	return	

def circle(radius):
	turtle.circle(radius)
	return	
def square():
	i = 0	
	while i < 4:
		forward(100)
		right(90)
		i += 1
	return	

def black():
	turtle.pencolor("black")
	return
def blue():
	turtle.pencolor("blue")
	return
def green():
	turtle.pencolor("green")
	return
def red():
	turtle.pencolor("red")
	return

def cyan():
	turtle.pencolor("cyan")
	return	
def magenta():
	turtle.pencolor("magenta")
	return

def penup():
	turtle.penup()
	return

def pendown():
	turtle.pendown()
	return	

def clear():
	turtle.clear()
	return
def home():
	turtle.home()
	return		

def draw_1():
	turtle.write('1', False, "center", ("Times", 50, "normal"))
	return	
def draw_2():
	turtle.write('2', False, "center", ("Times", 50, "normal"))
	return	
def draw_3():
	turtle.write('3', False, "center", ("Times", 50, "normal"))
	return	
def draw_4():
	turtle.write('4', False, "center", ("Times", 50, "normal"))
	return	
def draw_5():
	turtle.write('5', False, "center", ("Times", 50, "normal"))
	return	
def draw_6():
	turtle.write('6', False, "center", ("Times", 50, "normal"))
	return	
def draw_7():
	turtle.write('7', False, "center", ("Times", 50, "normal"))
	return	
def draw_8():
	turtle.write('8', False, "center", ("Times", 50, "normal"))
	return	
def draw_9():
	turtle.write('9', False, "center", ("Times", 50, "normal"))
	return									
##########EO turtle functions ###########

## Drawing the X's and O's##
def Os():
	blue()
	right(45)
	penup()
	forward(30)
	pendown()
	right(90)
	circle(40)
	left(90)
	penup()
	back(30)
	left(45)
	pendown()
	black()
	return

def Xs():
	red()
	right(45)
	penup()
	forward(25)
	pendown()
	forward(91)
	back(45.5)
	left(90)
	forward(45.5)
	back(91)
	forward(45.5)
	right(90)
	back(45.5)
	penup()
	back(25)
	left(45)
	black()
	pendown()
	return
###########EO Drawing X's , O's ##############		

### Function to draw the board ###
def board():

	
	'''Draw '7' on board '''
	forward(50)
	left(90)
	penup()
	forward(20)
	pendown()
	draw_7()
	penup()
	back(20)
	pendown()
	right(90)
	'''Draw '8' on board '''
	forward(100)
	left(90)
	penup()
	forward(20)
	pendown()
	draw_8()
	penup()
	back(20)
	right(90)
	pendown()
	'''Draw '9' on board '''
	forward(100)
	left(90)
	penup()
	forward(20)
	pendown()
	draw_9()
	penup()
	back(20)
	right(90)
	pendown()
	'''Draw '6' on board '''
	forward(50)
	left(90)
	forward(100)
	left(90)
	square()
	forward(50)
	right(90)
	penup()
	forward(20)
	pendown()
	draw_6()
	penup()
	back(20)
	left(90)
	pendown()
	'''Draw '5' on board '''
	forward(100)
	right(90)
	penup()
	forward(20)
	pendown()
	draw_5()
	penup()
	back(20)
	left(90)
	pendown()
	'''Draw '4' on board '''
	forward(100)
	right(90)
	penup()
	forward(20)
	pendown()
	draw_4()
	penup()
	back(20)
	left(90)
	pendown()
	'''Draw '1' on board '''
	forward(50)
	right(90)
	forward(100)
	right(90)
	forward(50)
	left(90)
	penup()
	forward(20)
	pendown()
	draw_1()
	penup()
	back(20)
	right(90)
	pendown()
	'''Draw '2' on board '''
	forward(50)
	left(90)
	square()
	right(90)
	forward(50)
	left(90)
	penup()
	forward(20)
	pendown()
	draw_2()
	penup()
	back(20)
	right(90)
	pendown()
	'''Draw '3' on board '''
	forward(100)
	left(90)
	penup()
	forward(20)
	pendown()
	draw_3()
	penup()
	back(20)
	right(90)
	pendown()
	'''Draw rest of number board '''
	forward(50)
	left(90)
	forward(100)
	left(90)
	forward(100)
	left(90)
	forward(300)
	right(90)
	forward(100)
	right(90)
	forward(300)
	left(90)
	forward(100)
	home()
	penup()
	forward(400)
	pendown()

	''' Draws Play space board '''
	j = 0
	while j < 4 :
		forward(300)
		left(90)
		j += 1

	forward(100)
	left(90)
	forward(300)
	right(90)
	forward(100)
	right(90)
	forward(300)

	left(90)
	forward(100)
	left(90)
	forward(100)
	left(90)
	forward(300)
	right(90)
	forward(100)
	right(90)
	forward(300)
	back(200)
	return
######EO Board function ################

## From space 5 (centre) to all other spots ##
def five_to_1():
	back(100)
	left(90)
	forward(100)
	right(90)
	return

def five_to_2():
	left(90)
	forward(100)
	right(90)
	return

def five_to_3():
	forward(100)
	left(90)
	forward(100)
	right(90)		
	return

def five_to_4():
	back(100)
	return

def five_to_6():
	forward(100)
	return

def five_to_7():
	back(100)
	right(90)
	forward(100)
	left(90)
	return

def five_to_8():
	right(90)
	forward(100)
	left(90)
	return

def five_to_9():
	forward(100)
	right(90)
	forward(100)
	left(90)
	return					
########## End of spot 5 (centre) ############

## From space 1 (top left) to all other spots ##
def one_to_5():
	forward(100)
	right(90)
	forward(100)
	left(90)
	return
########## End of spot 1 (top left) ############


## From space 2 (top centre) to spot 5 (centre) ##
def two_to_5():
	right(90)
	forward(100)
	left(90)
	return
########## End of spot 2 (top centre) ############


## From space 3 (top right) to spot 5 (centre) ##
def three_to_5():
	back(100)
	right(90)
	forward(100)
	left(90)
	return
########## End of spot 3 (top right) ############


## From space 4 (centre left) to spot 5 (centre) ##
def four_to_5():
	forward(100)
	return
########## End of spot 4 (centre left) ############


## From space 6 (centre right) to spot 5 (centre) ##
def six_to_5():
	back(100)
	return
########## End of spot 6 (centre right) ############


## From space 7 (bottom left) to spot 5 (centre) ##
def seven_to_5():
	forward(100)
	left(90)
	forward(100)
	right(90)
	return
########## End of spot 7 (bottom left) ############


## From space 8 (bottom centre) to spot 5 (centre) ##
def eight_to_5():
	left(90)
	forward(100)
	right(90)
	return
########## End of spot 8 (bottom centre) ############


## From space 9 (bottom right) to spot 5 (centre) ##
def nine_to_5():
	back(100)
	left(90)
	forward(100)
	right(90)
	return
########## End of spot 9 (bottom right) ############

def turn(shape):
	if shape == '1':
		Xs()
	else:
		Os()
	return		

##### Function that checks if a spot is taken and draws the appropriate shape ##
def spot_choice(choice,spots,spots_player,player):
	num = 0
	insults = 0
	#loop = 0
	if choice == '1':
		print ("X's turn, "),
	else:
		print ("O's turn, "),
	if player == '2':
		num = (input("choose a spot from 1 to 9. See play space for board numbering \nIf you would like to restart, type 'restart' and hit enter. \n \n If you would like to insult the computer \n type 'help' for a list of insults \n \n Type here:"))
		print ("\n")
	else:
		num = (input("choose a spot from 1 to 9. See play space for board numbering \nIf you would like to restart, type 'restart' and hit enter. \n \n Type here:"))	
	print ("\n")
	if num.lower() == 'help':
		print ("insult 1: 'Bring it noob. I'll give ya memory errors for life!' \n")
		print ("insult 2: 'Your mother is so fat, the recursive function computing her mass causes a stack overflow.' \n")
		print("insult 3:'You're slower than a 1 legged dog on tranquilizers.' \n")
		print ("insult 4: 'You're slower than a herd of snails traveling through peanut butter' \n")
		num = input("Choose a spot from 1 to 9 or type 'insult x' where x is 1,2,3 or 4 \n \n Type here:")
		print ("\n")

	while True:
		if num == '1':
			if spots[0] == 1:
				num = (input("This spot is already taken, choose a different one. \n \n Type here:"))
				print ("\n"*3)
			else:	
				if choice == '1':
					print ("Drawing 'X' on board ")
					print ("\n"*4)
				else:
					print ("Drawing 'O' on board \n")	
					print ("\n"*3)	
				draw(1,choice)
				#loop = 1
				spots[0] = 1
				spots_player[0] = 1
				break

		elif num == '2':
			if spots[1] == 1:
				num = (input("This spot is already taken, choose a different one. \n \n Type here:"))
				print ("\n"*3)
			else:
				if choice == '1':
					print ("Drawing 'X' on board \n")
					print ("\n"*3)
				else:
					print ("Drawing 'O' on board \n")	
					print ("\n"*3)
				draw(2,choice)
				#loop = 1
				spots[1] = 1
				spots_player[1] = 1
				break

		elif num == '3':
			if spots[2] == 1:
				num = (input("This spot is already taken, choose a different one. \n \n Type here:"))
				print ("\n"*3)
			else:
				if choice == '1':
					print ("Drawing 'X' on board \n")
					print ("\n"*3)
				else:
					print ("Drawing 'O' on board \n")
					print ("\n"*3)	
				draw(3,choice)
				spots[2] = 1
				spots_player[2] = 1
				break

		elif num == '4':
			if spots[3] == 1:
				num = (input("This spot is already taken, choose a different one. \n \n Type here:"))
				print ("\n"*3)
			else:
				if choice == '1':
					print ("Drawing 'X' on board \n")
					print ("\n"*3)
				else:
					print ("Drawing 'O' on board \n")	
					print ("\n"*3)
				draw(4,choice)
				spots[3] = 1
				spots_player[3] = 1
				break

		elif num == '5':
			if spots[4] == 1:
				num = (input("This spot is already taken, choose a different one. \n \n Type here:"))
				print ("\n"*3)
			else:
				if choice == '1':
					print ("Drawing 'X' on board \n")
					print ("\n"*3)
				else:
					print ("Drawing 'O' on board \n")	
					print ("\n"*3)
				turn(choice)
				spots[4] = 1
				spots_player[4] = 1
				break	


		elif num == '6':
			if spots[5] == 1:
				num = (input("This spot is already taken, choose a different one. \n \n Type here:"))
				print ("\n"*3)
			else:
				if choice == '1':
					print ("Drawing 'X' on board \n")
					print ("\n"*3)
				else:
					print ("Drawing 'O' on board \n")	
					print ("\n"*3)
				draw(6,choice)
				spots[5] = 1
				spots_player[5] = 1
				break	

		elif num == '7':
			if spots[6] == 1:
				num = (input("This spot is already taken, choose a different one. \n \n Type here:"))
				print ("\n"*3)
			else:
				if choice == '1':
					print ("Drawing 'X' on board \n")
					print ("\n"*3)
				else:
					print ("Drawing 'O' on board \n")	
					print ("\n"*3)
				draw(7,choice)
				spots[6] = 1
				spots_player[6] = 1
				break

		elif num == '8':
			if spots[7] == 1:
				num = (input("This spot is already taken, choose a different one. \n \n Type here:"))
				print ("\n"*3)
			else:
				if choice == '1':
					print ("Drawing 'X' on board \n")
					print ("\n"*3)
				else:
					print ("Drawing 'O' on board \n")	
					print ("\n"*3)
				draw(8,choice)
				spots[7] = 1
				spots_player[7] = 1
				break

		elif num == '9':
			if spots[8] == 1:
				num = (input("This spot is already taken, choose a different one. \n \n Type here:"))
				print ("\n"*3)
			else:
				if choice == '1':
					print ("Drawing 'X' on board \n")
					print ("\n"*3)
				else:
					print ("Drawing 'O' on board \n")	
					print ("\n"*3)
				draw(9,choice)
				spots[8] = 1
				spots_player[8] = 1
				break

		elif num.lower() == 'restart':
				spots[0] = 9
				break

		elif (num.replace(" ","").lower()) == 'insult1':
			if insults < 4:
				print ("Human: 'Bring it noob. I'll give ya memory errors for life!' \n")
			time.sleep(2)
			insults = insulting(insults)
			num = input("Choose a spot from 1 to 9 or type 'insult x' where x is 1,2,3 or 4 \n \n Type here:")


		elif (num.replace(" ","").lower()) == 'insult2':
			if insults < 4:
				print ("Human: 'Your mother is so fat, the recursive function computing her mass causes a stack overflow.' \n")
			time.sleep(2)
			insults = insulting(insults)
			num = input("Choose a spot from 1 to 9 or type 'insult x' where x is 1,2,3 or 4 \n \n Type here:")

		elif (num.replace(" ","").lower()) == 'insult3':
			if insults < 4:
				print("Human:'You're slower than a 1 legged dog on tranquilizers.' \n")
			time.sleep(2)
			insults = insulting(insults)
			num = input("Choose a spot from 1 to 9 or type 'insult x' where x is 1,2,3 or 4 \n \n Type here:")

		elif (num.replace(" ","").lower()) == 'insult4':
			if insults < 4:
				print ("Human: 'You're slower than a herd of snails traveling through peanut butter' \n")
			time.sleep(2)
			insults = insulting(insults)
			num = input("Choose a spot from 1 to 9 or type 'insult x' where x is 1,2,3 or 4 \n \n Type here:")

		elif num.lower() == 'help':
			print ("insult 1: 'Bring it noob. I'll give ya memory errors for life!' \n")
			print ("insult 2: 'Your mother is so fat, the recursive function computing her mass causes a stack overflow.' \n")
			print("insult 3:'You're slower than a 1 legged dog on tranquilizers.' \n")
			print ("insult 4: 'You're slower than a herd of snails traveling through peanut butter' \n")
			num = input("Choose a spot from 1 to 9 or type 'insult x' where x is 1,2,3 or 4 \n \n Type here:")
			print ("\n")	

		else:
			num = input("Invalid input, type a number between 1 and 9. \n \n Type here:")
			print ("\n"*3)

	return			

######### End of Function that checks if spots are taken or not ######

#### Insult Function ##############
def insulting(insults):
	if insults == 0:
		print ("AI: Wow, you are about as intelligent as a floppy disk.. \n")
		time.sleep(2)
		insults = 1
		return insults
	elif insults == 1:
		print ("AI: Hey you hurt my feelings! wait..I am a computer, I have no feelings ;) \n")
		time.sleep(2)
		insults = 2
		return insults
	elif insults == 2:
		print ("AI: you know what? if you touch me again, I'm posting your search history on Facebook..\n")
		time.sleep(2)
		insults = 3
		return insults
	elif insults == 3:		
		print("Now you are really pushing my buttons... >:( \n")
		time.sleep(2)
		insults = 4
		return insults
	else:
		print ("AI: No more insults from you..")
		time.sleep(2)
		return insults
		
############ EO insult function ###########################

##### Function that picks a random open spot ##############
def random_spot(choice,ai_spots,spots_used):
	position = randint(0,8)
	spot_open = 1
	#print (spots_used)
	time.sleep(1)
	while spot_open == 1:
		if spots_used[position] != 1:
			spot_open = 0
			#print ("inside")
			

			if position == 0:
				#print( "one")
				if choice == '1':
					print ("Drawing 'X' on board \n")
					print ("\n"*3)
				else:
					print ("Drawing 'O' on board \n")	
					print ("\n"*3)
				draw(1,choice)
				ai_spots[position] = 1
				spots_used[position] = 1

			elif position == 1:
				#print( "two")
				if choice == '1':
					print ("Drawing 'X' on board \n")
					print ("\n"*3)
				else:
					print ("Drawing 'O' on board \n")	
					print ("\n"*3)
				draw(2,choice)
				ai_spots[position] = 1
				spots_used[position] = 1

			elif position == 2:
				#print( "three")
				if choice == '1':
					print ("Drawing 'X' on board \n")
					print ("\n"*3)
				else:
					print ("Drawing 'O' on board \n")	
					print ("\n"*3)
				draw(3,choice)
				ai_spots[position] = 1
				spots_used[position] = 1

			elif position == 3:
				#print( "four")
				if choice == '1':
					print ("Drawing 'X' on board \n")
					print ("\n"*3)
				else:
					print ("Drawing 'O' on board \n")	
					print ("\n"*3)
				draw(4,choice)
				ai_spots[position] = 1
				spots_used[position] = 1

			elif position == 4:
				#print( "five")
				if choice == '1':
					print ("Drawing 'X' on board \n")
					print ("\n"*3)
				else:
					print ("Drawing 'O' on board \n")	
					print ("\n"*3)
				turn(choice)
				ai_spots[position] = 1
				spots_used[position] = 1

			elif position == 5:
				#print( "six")
				if choice == '1':
					print ("Drawing 'X' on board \n")
					print ("\n"*3)
				else:
					print ("Drawing 'O' on board \n")	
					print ("\n"*3)
				draw(6,choice)
				ai_spots[position] = 1
				spots_used[position] = 1

			elif position == 6:
				#print( "seven")
				if choice == '1':
					print ("Drawing 'X' on board \n")
					print ("\n"*3)
				else:
					print ("Drawing 'O' on board \n")	
					print ("\n"*3)
				draw(7,choice)
				ai_spots[position] = 1
				spots_used[position] = 1

			elif position == 7:
				#print( "eight")
				if choice == '1':
					print ("Drawing 'X' on board \n")
					print ("\n"*3)
				else:
					print ("Drawing 'O' on board \n")	
					print ("\n"*3)
				draw(8,choice)
				ai_spots[position] = 1
				spots_used[position] = 1

			elif position == 8:	
				#print( "nine")
				if choice == '1':
					print ("Drawing 'X' on board \n")
					print ("\n"*3)
				else:
					print ("Drawing 'O' on board \n")	
					print ("\n"*3)
				draw(9,choice)
				ai_spots[position] = 1
				spots_used[position] = 1	

			else:
				print ("Error in random spot function")	

		position = randint(0,8)

	return											

########## EO Random spot function ##########################

#########Checks to see if there is 3-in-a-row #####################
def winner(spots,choice,all_spots):
	if (spots[0] == 1 and spots[1] == 1 and spots[2] == 1) or (spots[3] == 1 and spots[4] == 1 and spots[5] == 1) or (spots[6] == 1 and spots[7] == 1 and spots[8] == 1) or (spots[0] == 1 and spots[3] == 1 and spots[6] == 1) or (spots[1] == 1 and spots[4] == 1 and spots[7] == 1) or (spots[2] == 1 and spots[5] == 1 and spots[8] == 1) or (spots[0] == 1 and spots[4] == 1 and spots[8] == 1) or (spots[2] == 1 and spots[4] == 1 and spots[6] == 1):
		if choice == '1':
			print ("X's win! \n")
			return 1
		else:
			print ("O's win! \n")
			return 1	
	elif all_spots == [1,1,1,1,1,1,1,1,1]:
		print ("It's a Draw.. \n")
		return 2
	else:	
		return 0
############ EO Winner check #####################

#### Function that draws an X or O in correct spot ###
def draw(number,choice):
	if number == 1:
		five_to_1()
		turn(choice)
		one_to_5()

	elif number == 2:
		five_to_2()
		turn(choice)
		two_to_5()

	elif number == 3:
		five_to_3()
		turn(choice)
		three_to_5()

	elif number == 4:
		five_to_4()
		turn(choice)
		four_to_5()

	elif number == 6:
		five_to_6()	
		turn(choice)
		six_to_5()

	elif number == 7:
		five_to_7()
		turn(choice)
		seven_to_5()

	elif number == 8:
		five_to_8()
		turn(choice)
		eight_to_5()

	elif number == 9:
		five_to_9()	
		turn(choice)
		nine_to_5()

	else:
		print ("Error in Draw funtion")	

	return							


######### AI function that determines where to move ######
def AI_moves(choice,ai_spots,human,spots_used):
	if human == [0,0,0,0,0,0,0,0,0] and spots_used[4] != 1:
		if choice == '1':
				print ("Drawing 'X' on board \n")
				print ("\n"*3)
		else:
			print ("Drawing 'O' on board \n")	
			print ("\n"*3)
		print ("\n AI: Ready to lose, human? \n")	
		time.sleep(2)
		turn(choice)
		spots_used[4] = 1
		ai_spots[4] = 1
			
		'''AI goes in space one '''
	elif ((human[1] == 1 and human[2] == 1) or (human[3] == 1 and human[6] == 1) or (human[4] == 1 and human[8] == 1)) and spots_used[0] != 1:
		if choice == '1':
				print ("Drawing 'X' on board \n")
				print ("\n"*3)
		else:
			print ("Drawing 'O' on board \n")	
			print ("\n"*3)
		draw(1,choice)
		print ("\n AI: Ready to lose, human? \n")	
		time.sleep(2)
		spots_used[0] = 1
		ai_spots[0] = 1
			

		'''AI goes in space two '''
	elif ((human[4] == 1 and human[7] == 1) or (human[0] == 1 and human[2] == 1)) and spots_used[1] != 1:
		if choice == '1':
				print ("Drawing 'X' on board \n")
				print ("\n"*3)
		else:
			print ("Drawing 'O' on board \n")	
			print ("\n"*3)
		draw(2,choice)
		print ("\n AI: Ready to lose, human? \n")	
		time.sleep(2)
		spots_used[1] = 1
		ai_spots[1] = 1
			

		'''AI goes in space three '''
	elif ((human[0] == 1 and human[1] == 1) or (human[5] == 1 and human[8] == 1) or (human[4] == 1 and human[6] == 1)) and spots_used[2] != 1:
		if choice == '1':
				print ("Drawing 'X' on board \n")
				print ("\n"*3)
		else:
			print ("Drawing 'O' on board \n")	
			print ("\n"*3)
		draw(3,choice)
		print ("\n AI: Ready to lose, human? \n")	
		time.sleep(2)
		spots_used[2] = 1
		ai_spots[2] = 1
			

		'''AI goes in space four '''
	elif ((human[4] == 1 and human[5] == 1) or (human[0] == 1 and human[6] == 1)) and spots_used[3] != 1:
		if choice == '1':
				print ("Drawing 'X' on board \n")
				print ("\n"*3)
		else:
			print ("Drawing 'O' on board \n")	
			print ("\n"*3)
		draw(4,choice)
		print ("\n AI: Ready to lose, human? \n")	
		time.sleep(2)
		spots_used[3] = 1
		ai_spots[3] = 1
					

		'''AI goes in space five '''
	elif ((human[3] == 1 and human[5] == 1) or (human[1] == 1 and human[7] == 1) or (human[2] == 1 and human[6] == 1) or (human[0] == 1 and human[8] == 1)) and spots_used[4] != 1:
		if choice == '1':
				print ("Drawing 'X' on board \n")
				print ("\n"*3)
		else:
			print ("Drawing 'O' on board \n")	
			print ("\n"*3)
		turn(choice)
		print ("\n AI: Ready to lose, human? \n")	
		time.sleep(2)
		spots_used[4] = 1
		ai_spots[4] = 1
			

		'''AI goes in space six '''
	elif ((human[2] == 1 and human[8] == 1) or (human[3] == 1 and human[4] == 1)) and spots_used[5] != 1:
		if choice == '1':
				print ("Drawing 'X' on board \n")
				print ("\n"*3)
		else:
			print ("Drawing 'O' on board \n")	
			print ("\n"*3)
		draw(6,choice)
		print ("\n AI: Ready to lose, human? \n")	
		time.sleep(2)
		spots_used[5] = 1
		ai_spots[5] = 1
			

		'''AI goes in space seven '''
	elif ((human[0] == 1 and human[3] == 1) or (human[7] == 1 and human[8] == 1) or (human[2] == 1 and human[4] == 1)) and spots_used[6] != 1:
		if choice == '1':
				print ("Drawing 'X' on board \n")
				print ("\n"*3)
		else:
			print ("Drawing 'O' on board \n")	
			print ("\n"*3)
		draw(7,choice)
		print ("\n AI: Ready to lose, human? \n")	
		time.sleep(2)
		spots_used[6] = 1
		ai_spots[6] = 1
			

		'''AI goes in space eight '''
	elif ((human[1] == 1 and human[4] == 1) or (human[6] == 1 and human[8] == 1)) and spots_used[7] != 1:
		if choice == '1':
				print ("Drawing 'X' on board \n")
				print ("\n"*3)
		else:
			print ("Drawing 'O' on board \n")	
			print ("\n"*3)
		draw(8,choice)
		print ("\n AI: Ready to lose, human? \n")	
		time.sleep(2)
		spots_used[7] = 1
		ai_spots[7] = 1
				

		'''AI goes in space nine '''
	elif ((human[0] == 1 and human[4] == 1) or (human[2] == 1 and human[5] == 1) or (human[6] == 1 and human[7] == 1)) and spots_used[8] != 1:
		if choice == '1':
				print ("Drawing 'X' on board \n")
				print ("\n"*3)
		else:
			print ("Drawing 'O' on board \n")	
			print ("\n"*3)
		draw(9,choice)
		print ("\n AI: Ready to lose, human? \n")	
		time.sleep(2)
		spots_used[8] = 1
		ai_spots[8] = 1
			
		# AI goes for 3 in a row at spot 1 #	
	elif ((ai_spots[1] == 1 and ai_spots[2] == 1) or (ai_spots[3] == 1 and ai_spots[6] == 1) or (ai_spots[4] == 1 and ai_spots[8] == 1)) and spots_used[0] != 1:
		if choice == '1':
				print ("Drawing 'X' on board \n")
				print ("\n"*3)
		else:
			print ("Drawing 'O' on board \n")	
			print ("\n"*3)
		draw(1,choice)
		print ("\n AI: I win 101010101010..(laughing in binary) \n")	
		time.sleep(2)
		spots_used[0] = 1
		ai_spots[0] = 1

	# AI goes for 3 in a row at spot 2 #	
	elif ((ai_spots[4] == 1 and ai_spots[7] == 1) or (ai_spots[0] == 1 and ai_spots[2] == 1)) and spots_used[1] != 1:
		if choice == '1':
				print ("Drawing 'X' on board \n")
				print ("\n"*3)
		else:
			print ("Drawing 'O' on board \n")	
			print ("\n"*3)
		draw(2,choice)
		print ("\n AI: I win 101010101010..(laughing in binary) \n")
		time.sleep(2)
		spots_used[1] = 1
		ai_spots[1] = 1

	# AI goes for 3 in a row at spot 3 #	
	elif ((ai_spots[0] == 1 and ai_spots[1] == 1) or (ai_spots[5] == 1 and ai_spots[8] == 1) or (ai_spots[4] == 1 and ai_spots[6] == 1)) and spots_used[2] != 1:
		if choice == '1':
				print ("Drawing 'X' on board \n")
				print ("\n"*3)
		else:
			print ("Drawing 'O' on board \n")	
			print ("\n"*3)
		draw(3,choice)
		print ("\n AI: I win 101010101010..(laughing in binary) \n")
		time.sleep(2)
		spots_used[2] = 1
		ai_spots[2] = 1

	# AI goes for 3 in a row at spot 4 #	
	elif ((ai_spots[4] == 1 and ai_spots[5] == 1) or (ai_spots[0] == 1 and ai_spots[6] == 1)) and spots_used[3] != 1:
		if choice == '1':
				print ("Drawing 'X' on board \n")
				print ("\n"*3)
		else:
			print ("Drawing 'O' on board \n")	
			print ("\n"*3)
		draw(4,choice)
		print ("\n AI: I win 101010101010..(laughing in binary) \n")
		time.sleep(2)
		spots_used[3] = 1
		ai_spots[3] = 1

	# AI goes for 3 in a row at spot 5 #	
	elif ((ai_spots[3] == 1 and ai_spots[5] == 1) or (ai_spots[1] == 1 and ai_spots[7] == 1) or (ai_spots[2] == 1 and ai_spots[6] == 1) or (ai_spots[0] == 1 and ai_spots[8] == 1)) and spots_used[4] != 1:
		if choice == '1':
				print ("Drawing 'X' on board \n")
				print ("\n"*3)
		else:
			print ("Drawing 'O' on board \n")	
			print ("\n"*3)
		turn(choice)
		print ("\n AI: I win 101010101010..(laughing in binary) \n")
		time.sleep(2)
		spots_used[4] = 1
		ai_spots[4] = 1

	# AI goes for 3 in a row at spot 6 #	
	elif ((ai_spots[2] == 1 and ai_spots[8] == 1) or (ai_spots[3] == 1 and ai_spots[4] == 1)) and spots_used[5] != 1:
		if choice == '1':
				print ("Drawing 'X' on board \n")
				print ("\n"*3)
		else:
			print ("Drawing 'O' on board \n")	
			print ("\n"*3)
		draw(6,choice)
		print ("\n AI: I win 101010101010..(laughing in binary) \n")
		time.sleep(2)
		spots_used[5] = 1
		ai_spots[5] = 1

	# AI goes for 3 in a row at spot 7 #	
	elif ((ai_spots[0] == 1 and ai_spots[3] == 1) or (ai_spots[7] == 1 and ai_spots[8] == 1) or (ai_spots[2] == 1 and ai_spots[4] == 1)) and spots_used[6] != 1:
		if choice == '1':
				print ("Drawing 'X' on board \n")
				print ("\n"*3)
		else:
			print ("Drawing 'O' on board \n")	
			print ("\n"*3)
		draw(7,choice)
		print ("\n AI: I win 101010101010..(laughing in binary) \n")
		time.sleep(2)
		spots_used[6] = 1
		ai_spots[6] = 1

	# AI goes for 3 in a row at spot 8 #	
	elif ((ai_spots[1] == 1 and ai_spots[4] == 1) or (ai_spots[6] == 1 and ai_spots[8] == 1)) and spots_used[7] != 1:
		if choice == '1':
				print ("Drawing 'X' on board \n")
				print ("\n"*3)
		else:
			print ("Drawing 'O' on board \n")	
			print ("\n"*3)
		draw(8,choice)
		print ("\n AI: I win 101010101010..(laughing in binary) \n")
		time.sleep(2)
		spots_used[7] = 1
		ai_spots[7] = 1

	# AI goes for 3 in a row at spot 9 #	
	elif ((ai_spots[0] == 1 and ai_spots[4] == 1) or (ai_spots[2] == 1 and ai_spots[5] == 1) or (ai_spots[6] == 1 and ai_spots[7] == 1)) and spots_used[8] != 1:
		if choice == '1':
				print ("Drawing 'X' on board \n")
				print ("\n"*3)
		else:
			print ("Drawing 'O' on board \n")	
			print ("\n"*3)
		draw(9,choice)
		print ("\n AI: I win 101010101010..(laughing in binary) \n")
		time.sleep(2)
		spots_used[8] = 1
		ai_spots[8] = 1								


	else:
		print ("Finding spot..")
		time.sleep(1)
		random_spot(choice,ai_spots,spots_used)
			

	return
########## EO AI function boiiii ##################
def main():

	game_won = 0
	choice = 0
	AI_choice = 0
	player = 0
	computer = 6
	insults = 0
	spots_taken = [0,0,0,0,0,0,0,0,0]
	spots_O = [0,0,0,0,0,0,0,0,0]
	spots_X = [0,0,0,0,0,0,0,0,0]

	print ("Drawing play space...")
	board()
	print ("\n"*100)

	print ("Welcome to Tic Tac Toe! \n \n \n \n \n")
	print ("NOTE: you must hit enter after you type in your choice.")

	while player != '1' and player != '2':
		player = input("If you'd like to be play with a friend, enter '1', enter '2' to verse a computer \n \n Type here: ")
		
	
	while choice != '1' and choice != '2':
		print ("NOTE: you must hit enter after you type in your choice. \n \n")
		choice = (input("If you'd like to be X's, enter '1', enter '2' for O's \n \n Type here: "))
		print ("\n")
	print ("\n"*100)

	print ("NOTE: you must hit enter after you type in your choice. \n \n")

	if player == '2':
		print ("Drawing randomly to see who goes first.. \n \n")
		time.sleep(2)
		computer = randint(0,1)
		if computer == 1:
			print ("Computer goes first.. \n")
			time.sleep(1.5)
		elif computer == 0:
			print ( "AI: Make your move, Human. \n")	
			time.sleep(1.5)
		else:
			print ("\n")
	else:
		print ("Drawing randomly to see who goes first.. \n \n")
		time.sleep(2)
		choice = randint(1,2)
		if choice == 1:
			choice = '1'
			print ("X's go first. \n \n")
			time.sleep(1.5)
		else:
			choice = '2'
			print ("O's go first. \n \n")
			time.sleep(1.5)


	if choice == '1':
		AI_choice = '2'
	else:
		AI_choice = '1'	

	while game_won == 0:
		''' if statement for playing against another human '''
		if player == '1':	
			if choice == '1':
				spot_choice(choice,spots_taken,spots_X,player)
				if spots_taken[0] == 9:
					break
				game_won = winner(spots_X,choice,spots_taken)
				choice = '2'
				#print ("%s \n"%spots_X )

			elif choice == '2':
				spot_choice(choice,spots_taken,spots_O,player)
				if spots_taken[0] == 9:
					break
				game_won = winner(spots_O,choice,spots_taken)
				choice = '1'
				#print ("%s \n"%spots_O)

			else:
				print ("Error 1")

			''' Else statement for playing against an AI '''
		else:		
			if choice == '1':
				AI_choice = '2'
			else:
				AI_choice = '1'

			if AI_choice == '1' and computer == 1:
			
				## Code for AI goes here ##
				#print ("Line 980")
				print ("AI calculating best move.. \n")
				#print (spots_X,spots_O)
				time.sleep(3)
				AI_moves(AI_choice,spots_X,spots_O,spots_taken)
				#print ("Line 984")
				time.sleep(3)
				game_won = winner(spots_X,AI_choice,spots_taken)
				if game_won == 1:
					#print("\nAI Won the game with choice = 1\n")
					print ("\n AI: I win 101010101010..(laughing in binary) \n")
				computer = 0
				#choice = '2'
			elif choice == '1' and computer == 0:
				#print (player)
				spot_choice(choice,spots_taken,spots_X,player)
				if spots_taken[0] == 9:
					break
				game_won = winner(spots_X,choice,spots_taken)
				#choice = '2'
				computer = 1
			
			elif AI_choice == '2' and computer == 1:
				## Code for AI goes here ##
				#print ("Line 989")
				print ("AI calculating best move..\n")
				#print (spots_X,spots_O)
				time.sleep(3)
				AI_moves(AI_choice,spots_O,spots_X,spots_taken)
				#print ("Line 992")
				#time.sleep(3)
				game_won = winner(spots_O,AI_choice,spots_taken)
				if game_won == 1:
					#print("\nAI Won the game with choice = 2\n")
					print ("\n AI: I win 101010101010..(laughing in binary) \n")
				computer = 0
				#choice = '1'
			elif choice == '2' and computer == 0:	
				#print (player)
				spot_choice(choice,spots_taken,spots_O,player)
				if spots_taken[0] == 9:
					break
				game_won = winner(spots_O,choice,spots_taken)
				#choice = '1'
				computer = 1
			else:
				print ("Error 2")					


	return spots_taken[0]

while True:
	end_phrase = main()
	if end_phrase == 9:
		print ("Restarting game..\n \n")
		time.sleep(5)
	else:	
		print ("Game Over! wait 10 seconds to play again \n")
		time.sleep(9)
	home()
	clear()

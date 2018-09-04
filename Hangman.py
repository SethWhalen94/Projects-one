''' HangMan '''
#-------------------#
''' Source Code owned by Seth Whalen @smwhalen94 '''
#---------------------------------#
import turtle as turtle
#turtle.speed(0)
#Global variable definitions
letters = ["A","B","C",'D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
count = 0
guess = ""
word = ""
guesses = 0
number = 0
true2 = True
print_word = []
############# EO definitions ##############

####Letter guessing function####
def guess_word(guesses):
	guess = ""
	true = True
	while true:
		if guesses < 6:
			print_phrase(print_word)
			print ("\n")
			print ("You have %d limbs left" %(6-guesses))
			inputs = (input("Enter your guess:"))
			if inputs.isdigit() or inputs == "" or len(inputs) != 1 or " " in inputs or inputs.isalpha() == False :
				print ("\n" * 100)
				print ("Please enter a single letter")
			else:
				guess = inputs
				true = False	

	return guess	
################ EOFunc guess_word #################

#function that prints out the current standing of letters in the word/phrase
def print_phrase(words):
	i = 0
	while i < len(words):
		print (words[i]),
		i+=1
	return	
################# EOFunc print_phrase ##################

#function that rotates drawing cursor 180 degrees
def one_8():
	turtle.right(180)
	return
############# EOFunc one_8 ##################

#Function that draws a circle, useless since 'turtle.circle()' does the same thing
def circle():
	for i in range(360):
		turtle.forward(.6)
		turtle.right(1)
	return
############ EOFunc circle##############

### Drawing the Hanger
print ("Loading...")
turtle.penup()
turtle.backward(200)
turtle.right(90)
turtle.forward(200)
turtle.left(90)
turtle.pendown()
turtle.forward(200)
turtle.backward(100)
turtle.left(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(50)
turtle.left(90)
print ("\n" * 100)
####### EO drawing hanger ##########
##Asking for player 1's word/phrase of choice###
while true2:
	word = input("Player 1, Enter a word or phrase for Player 2 to guess:")
	if word.isdigit()  or word == "" or (word.isalpha() or len(word) > 5) == False:
		print ("\n" * 100)
		print ("Please enter letters only")
	else:
		true2 = False
############ EO word/phrase Input ################

### Creating empty list to hold Correct guessed letters and list version of "word/phrase" entered ###
print ("\n" * 100)
word = word.upper()
print_word = ["__"]*(len(word))
word3 = list(word)
if " " in word:
	word2 = list(word.upper())
	word2.remove(" ")
	word2 = str(word2)
else:
	word2 = list(word)
###### EO Lists ##############


##### Main Part of code, checks whether letter guesses are correct or duplicates. Prints results ##
##### and print a list of letters that have not been guessed ######################################
while count < 6:
	letter = guess_word(count)
	i = 0
	letter = letter.upper()

	while i < len(word3):
		if word3[i] == letter:
  		    print_word[i] = letter

		elif word3[i] == " ":
			print_word[i] = " "
		i+=1

	number = 0

	if letter not in letters:
		print ("\n" * 100)
		print_phrase(print_word)
		print ("\n")
		print ("You already guessed the letter %s \n" %letter)
		print ("Letters you haven't guessed %s \n" %letters)

	elif letter in word2:
		print ("\n" * 100)
		#print_phrase(print_word)
		#print ("\n")
		print ("Good guess. the letter %s is in the word \n" %letter.upper())
		letter = letter.upper()
		letters.remove(letter)
		print ("Letters you haven't guessed %s \n" %letters)


	for i in letters:
		for j in word2:
			if j == i:
				number =+ 1	

	if number == 0:
		while i < len(word):
			if word3[i] == letter:
  			    print_word[i] = letter
			i+=1
		print ("\n" * 100)
		print (" Congratulations! You won! the word/phrase is "),
		print_phrase(print_word)
		print ("\n")
		break

	if letter not in word2:

		if letter not in letters:
			print ("\n")

		else:
			letter = letter.upper()
			letters.remove(letter)
			print ("\n" * 100)
			print ("The letter %s is not in the word" % letter)
			print ("Letters you haven't guessed %s \n" %letters)
			count += 1

			'''Drawing the head'''
			if count == 1:
				print ("Drawing head...")
				turtle.right(180)
				turtle.circle(40)
				turtle.left(90)
				turtle.penup()
				turtle.forward(73)
				turtle.pendown()
				print ("\n" * 10)

			'''Drawing the body'''
			if count == 2:
				turtle.forward(100)

			'''Drawing right leg'''
			if count == 3:
				turtle.left(45)
				turtle.forward(50)
				turtle.backward(50)

			'''Drawing left leg'''
			if count == 4:
				turtle.right(90)
				turtle.forward(50)
				turtle.backward(50)
				turtle.right(135)
				turtle.forward(65)
				one_8()


			'''Drawing the right arm'''
			if count == 5:
				turtle.left(45)
				turtle.forward(35)
				turtle.backward(35)
				turtle.right(90)


'''Drawing the left arm'''
if count == 6 and number != 0:
	turtle.forward(35)
	turtle.backward(35)
	print ("\n" * 100)
	print ( " You lost :("),
	print ("The word/phrase was"),
	print (word)


	################## END OF PROGRAM ###########################
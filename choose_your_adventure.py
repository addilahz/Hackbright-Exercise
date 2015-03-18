#choose your adventure

def intro ():
	#print introductions - going in a castle
	print "Going inside the castle to find treasure. You stand in front of two doors. Please choose and proceeds at your own risk"
	#decide - choose a door A B
	print "Door A, Door B or Door C" 
	#users need to enter A or B in the terminal
	door = raw_input()
	door = door.upper()
	# #whichever door the users choose, it will open
	if door == "NO":
	   print "Toodles!"
	if door == "A" :
		doorA ()
	if door == "B":
		doorB()
	if door == "C":
 		doorC()


 

def doorA ():
	print "Hooray! Your found the treasure!"
def doorB ():
	print "Oh no, its's the dragon! The dragon eat you! Game Over!"
def doorC():
	print "Congratulations, you found a secret door! You get Easter Eggs as a treat. Enjoy!"
	print "would you like to continue to play and choose Door A, Door B or No?"
	door = raw_input()
	door = door.upper()
	if door == "NO":
	   print "Toodles!"
	if door == "A":
		doorA()
	if door == "B":
		doorB()
	if door == "C":
 		doorC()
intro()
 
























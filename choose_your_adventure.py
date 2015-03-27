#choose your adventure

def intro ():
	#print introductions - going in a castle
	print "Going inside the castle to find treasure. You stand in front of two doors. Please choose and proceeds at your own risk"
	#decide - choose a door A B
	print "Door A, Door B or Door C" 
	#users need to enter A or B in the terminal
	door = raw_input()
	#regardless what user enter (e.g. lowercase) convert letter to uppercase letter
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
	print "You are standing in front of two door again. Please choose Door D or E. Be very sure with your choice!"
	door = raw_input()
	door = door.upper()
	if door == "D":
		doorD()
	if door == "E":
		doorE()
	



def doorC ():
	print "You get Easter Eggs as a treat. Enjoy!"
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
 	
 	
 	

def doorD () :
	print " You found a stairs and next to it, there's a door. Do you want to climb the stairs or open Door A?"
 	door = raw_input()
	door = door.upper()
	if door == "A":
		doorA()
	if door == "STAIRS":
		stairs()
	
	


def doorE ():
	print "Oh no, you just open the wrong door and fell into the hole! Sorry.. Game Over!"


def stairs ():
	print " uh oh, it's block by the wall. You have no choice but to turn around"




intro()
 
























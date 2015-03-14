#choose your adventure
def doorA ():
	print "Hooray! Your found the treasure!"
def doorB ():
	print "Oh no, its's the dragon! The dragon eat you! Game Over!"
def doorC():
	print "Congratulations, you found a secret door! You get Easter Eggs as a treat. Enjoy!"
	print "would you like to continue to play and choose Door A, Door B or No?"
	door = raw_input()
	if door == "No":
	   print "Toodles!"
	if door == "A":
		doorA()
	if door == "B":
		doorB()













#print introductions - going in a castle
print "Going inside the castle to find treasure. You stand in front of two doors. Please choose and proceeds at your own risk"
#decide - choose a door A B
print "Door A or Door B" 
#users need to enter A or B in the terminal
door = raw_input()
#whichever door the users choose, it will open
if door == "A" :
	doorA ()
if door == "B":
	doorB()
if door == "C":
	doorC()
#door B - find a dragon. users burned! game over 




















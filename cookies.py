# *** Needs to be some association between the date and the number of cookies sold***
# Open the file
cookie_file = open ("PT-Intro-To-Programming/week03/lists/cookies_sold.txt")
# Read it
	#To find the number of cookies sold
cookies_sold = cookie_file.readlines()	
# Close the file
cookie_file.close()
# Prompt the user to input two dates
dates = raw_input("Pick two dates:")
dates = dates.split(",")
date1 = int(dates [0])
date2 = int(dates[1])
# Compare the two dates
	# If date1 sold more cookies than the date2,
		#print more cookies were sold on date 1
if int(cookies_sold[date1-1] > int (cookies_sold[date2-1]):
			#print "more cookies were sold on date 1"
	print "More cookies were sold on date1"
	# If date2 sold more cookies than the date 1,
			#print "more cookies were sold on date 2"
	# else 


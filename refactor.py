my_numbers = [8,3,46,1,2,3]

for i in range (0,len(my_numbers)):
	if my_numbers[i] % 2==0:
		print "the number %i is divisible by 2" % my_numbers[i]
	else:
		print "the number %i is not divisible by 2" % my_numbers[i]
	multiplied_by_2 = my_numbers[i] * 2
	print "The number %i multipled by 2 is %i." % (my_numbers[i], multiplied_by_2)


my_numbers = [8,3,46,1,2,3]

def chub (a,b):
	total = a + b
	print "The sum of %i and %i is %i." % (a, b, total)

chub(my_numbers[0],my_numbers[1])
chub(my_numbers[1],my_numbers[2])
chub(my_numbers[0],my_numbers[2])




#sum_of_first_two_numbers = my_numbers[0] + my_numbers[1]
#print "The sum of %i and %i is %i." % (my_numbers[0], my_numbers[1], sum_of_first_two_numbers)

#sum_of_last_two_numbers = my_numbers[1] + my_numbers[2]
#print "The sum of %i and %i is %i." % (my_numbers[1], my_numbers[2], sum_of_last_two_numbers)

#sum_of_first_and_last_numbers = my_numbers[0] + my_numbers[2]
#print "The sum of %i and %i is %i." % (my_numbers[0], my_numbers[2], sum_of_first_and_last_numbers)
		



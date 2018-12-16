from random import randint

# Randomly generates a number from 0-21 (22 projects)
# Returns number to find that project's data
# Appends number to list so that it is not reused
# Once list is full, restart with empty list
def Randomize(count_list):
	rand_int = randint(0,21)
	if (len(count_list)==22):
			count_list = []
	loop_failsafe = 0
	while (rand_int in count_list):
		if (loop_failsafe == 2):
			break
		rand_int+=1
		if (rand_int == 22):
			rand_int = 0
			loop_failsafe += 1
	count_list.append(rand_int)
	return count_list, rand_int

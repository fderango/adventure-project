rooms = [{"name":"entranceway", "msg":"","egg":True,"basket":False},
         {""}}]
def msg(room):
	if room['msg'] == '': #There is no custom message
		return 'You have entered the ' + room['name']
	else:
		return room['msg']

def get_choice(room,dir):
	if dir == 'N':
		choice = 0
	elif dir == 'E':
		choice = 1
	elif dir == 'S':
		choice = 2
	elif dir == 'W':
		choice = 3
	else:
		return -1

	if room['directions'][choice] == 0:
		return 4

	else:
		return choice

def statusupdate(bunny):
	print("You are in the ", location, ".")
	if basket == True:
		print("The basket is in this room! Little Johnny is sleeping right next to it so drop your eggs and get out fast!")
	else:


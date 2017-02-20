rooms = [{"name":"entranceway", "msg":"","egg":True,"basket":False,'directions':[2,4,0,0]},
         {""}}]
bunny = {"location":0,"basket":False,"eggs":0}
gameover = False
def msg(room):
	if room['msg'] == '': #There is no custom message
		return 'You have entered the ' + room['name']
	else:
		return room['msg']

def get_choice(room,dir):
	if dir="HELP":
		help()
		return room
	elif dir == 'N':
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
		print("You cannot go in that direction!")
		return room
	else:
		return room['directions'][choice]



def main():
	while(not gameover):
		userinput = input("Pick a direction. Type 'HELP' for help.")
		new_room = get_choice(bunny["location"], userinput)
		if new_room == -1:
			print("invalid input")
		else:
			bunny["location"] = room
			if room["basket"]:
				print("You got the basket")
				bunny["basket"] = True
				room["basket"] = False

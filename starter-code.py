

rooms = [{"name":"entranceway", "msg":"","egg":True,"basket":False},
         {"name":"hallway", "msg":"", "egg":True, "basket":False},
         {"name":"kitchen","msg":"", "egg":False, "basket":False},
         {"name":"diningroom", "msg":"", "egg":False, "basket":True},
         {"name":"livingroom", "msg":"", "egg":True, "basket":False}]

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

def statusupdate(bunny):
	msg(bunny["location"])
	if not bunny["basket"]:
		print("You do not have the basket")
	else:
		print("You have the basket! Now you can collect eggs")
		eggmessage = "You have ", bunny['eggs'], "egg(s) in your basket."
		print(eggmessage)

	# if basket == True:
	# 	print("The basket is in this room! Little Johnny is sleeping right next to it so drop your eggs and get out fast!")
	#

def main():
	while(not gameover):
		userinput = input("Pick a direction. Type 'HELP' for help.")
		new_room = get_choice(bunny["location"], userinput)
		if new_room == -1:
			print("Invalid input, try again")
		else:
			bunny["location"] = room
			if room["basket"]:
				print("You got the basket")
				bunny["basket"] = True
				room["basket"] = False
			if room["egg"]:
				print("There is an egg in this room! You picked it up")
				bunny["eggs"] += 1
				room["egg"] = False
		if bunny["eggs"] == 3:
			gameover = True

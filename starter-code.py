
def msg(room):
	if room['msg'] == '': #There is no custom message
		return 'You have entered the ' + room['name']
	else:
		return room['msg']


def get_choice(room,dir):
	if dir=="HELP":
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

	if room['directions'][choice] == -1:
		print("You cannot go in that direction!")
		return -1
	else:
		return room['directions'][choice]

def statusupdate(bunny):
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
	rooms = [{"name":"entranceway", "msg":"","egg":True,"basket":False,"directions":[2,4,-1,-1]},
	         {"name":"hallway", "msg":"", "egg":True, "basket":False,"directions":[-1,2,-1,-1]},
	         {"name":"kitchen","msg":"", "egg":False, "basket":False, "directions":[-1,3,0,1]},
	         {"name":"diningroom", "msg":"", "egg":False, "basket":True, "directions":[-1,-1,4,2]},
	         {"name":"livingroom", "msg":"", "egg":True, "basket":False, "directions":[3,-1,-1,0]}]

	bunny = {"location":0,"basket":False,"eggs":0}
	gameover = False
	while(not gameover):
		userinput = input("Pick a direction. Type 'HELP' for help.")
		new_room = get_choice(rooms[bunny["location"]], userinput)
		if new_room == -1:
			print("Invalid input, try again")
		else:
			bunny["location"] = new_room
			if rooms[new_room]["basket"]:
				print("You got the basket")
				bunny["basket"] = True
				rooms[new_room]["basket"] = False
			if rooms[new_room]["egg"]:
				print("There is an egg in this room! You picked it up")
				bunny["eggs"] += 1
				rooms[new_room]["egg"] = False
		if bunny["eggs"] == 3:
			print("you win")
			gameover = True

main()

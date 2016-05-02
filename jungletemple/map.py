import random




class Room(object):
	def __init__(self, name, description, help):
		self.name = name
		self.description = description
		self.help = help
		self.paths = {}
	
	def go(self, direction):
	    direction = direction.lower()
	    return self.paths.get(direction)
            
		
	def add_paths(self, paths):
		self.paths.update(paths)
		
#Death gets its own class, because there are so many instances of Death in the game. 
class Death(Room):
    def __init__(self, description):
        self.description = description
        self.paths = {}
        self.name = "Death"
        self.help = "Better luck next time!"

class Ravine(Room):
	def __init__(self, name, description, help):
		self.name = name
		self.description = description
		self.help = help
		self.paths = {}
		#generates a random integer between 1 and 3
		self.num = random.randint(1,3)
	#The method that works is chosen randomly. Hence, each choice can be either "good" or "bad".
	def go(self, direction):
	    if direction == "swing" and self.num == 1:
	        return self.paths.get("goodswing")
	    elif direction == "swing" and self.num != 1:
	    	return self.paths.get("badswing")
	    elif direction == "jump" and self.num == 2:
	        return self.paths.get("goodjump")
	    elif direction == "jump" and self.num != 2:
	        return self.paths.get("badjump")
	    elif direction == "climb" and self.num == 3:
	        return self.paths.get("goodclimb")
	    elif direction == "climb" and self.num != 3:
	        return self.paths.get("badclimb")
	    else:
	    	return self.paths.get("other")

confusion = Room("Say what?", """What you typed made no sense. Try again.""", "If you don't know what to type, read the 'Help' section.")

levers = Room("Entrance", """You enter the temple to find your path blocked by a wall. 
There are two recesses with levers hidden inside. Do you pull the left or the right one?""", "Type left or right to make a choice.")

ravine = Ravine("Ravine", """You pull the lever and a secret door opens up. You walk through the door and enter a dark pathway. 
After a few steps the path gives way to a wide ravine. How are you going to cross it?""", "You can try to jump across, swing from a vine, or climb along the wall.")

skeletons = Room("Skeletons", """You make it to the other side, where you fall on your face. 
You open your eyes, and face a grinning skull lying on the floor. There are skeletons with arrows in them strewn across the floor in front of you.
Do you sneak across, trying to avoid booby traps, or run across as fast as you can?""", "Your choices are sneak or run.")


doors = Room("Doors", """You tread carefully, avoiding a series of trick tiles on the floor. 
After maneuvering through the traps, you arrive at a wall with two doors. Do you walk through the left one or the right one?""", "Your choices are left or right.")

treasure = Room("Treasure Chamber", """Finally you arrive at your destination: the hidden treasure. 
There is a large chest filled with gold and diamonds and a solid gold idol in the shape of a Python. Which part of the treasure do you take?""", "Your choices are to pick up the whole chest, scoop some gold into your bag, or to take the Python statue.")

victory = Room("You win!", "You scoop some gold into your bag and quickly climb out of the temple, back to daylight and safety.", "Play again to try different outcomes!")
generic_death = Room("Dead", "You made the wrong choice and died", "You can play again.")

death1 = Death("""As you pull the lever, the stone around you begins to creak,
 as huge metal spikes shoot out of the walls and harpoon you.""")
death2 = Death("""You barely miss the next side, and try to cling to the rock, but your fingers find nothing to grab. 
You disappear into the depths.""")
death3 = Death("""You make it halfway across, but then the ledge you're holding onto breaks off, 
sending you careening into the void.""")
death4 = Death("""You push open the door and walk through. It slams shut behind you, and the floor gives way to a trap door, sending you falling onto a rocky bottom far below""")
death5 = Death("""You step onto a hidden tile and are killed by a poison arrow. Come on, that one was obvious.""")
death6 = Death("""As you lift up the chest, it activates a booby trap, sending a huge rock falling on top of you from the ceiling. Not even your styling brown fedora and your whip can protect you.""")
death7 = Death("""As you wrap your hand around the idol, a hidden poison spike penetrates the skin of your palm, sending a lethal dose of poison into your bloodstream.""")
death8 = Death("""The vine rips and you plummet into the pit.""")
death9 = Death("""You die of natural causes.""")
levers.add_paths({
"left":ravine, 
"right": death1
})
ravine.add_paths({
"goodswing": skeletons,
"badswing": death8,
"goodjump": skeletons,
"badjump": death2,
"goodclimb": skeletons,
"badclimb": death3,
"other": death9
})

skeletons.add_paths({
"sneak": doors,
"run": death5
})
doors.add_paths({
"left":treasure,
"right": death4
})

treasure.add_paths({
"chest": death6,
"scoop": victory,
"statue": death7
})


START = levers





import os





heroesSW = ['Luke Skywalker', 'Yoda', 'Han Solo', 'R2D2', 'C3PO', 'Chewbacca', 'Leia'] # I am setting the value for heroes
villainsSW=['Darth Vader','The Emperor', 'Jabba the Hut', ] # I am setting the value for Villains
heroesTN = ['Leonardo', 'Michelangelo', 'Donatello', 'Rapheal', 'Casey Jones', 'April', 'Master Splinter']
villainsTN = ['Shredder', 'Rock Steady', 'Bee Bop',]
global chosenlist

def Heropicker(list1,list2): #this is the definition, Heropicker, that is using heroesSW array and heroesTN array
	herolist = [] #this herolist is empty so that the user can input his/her choices, and it'll show up in the herolist
	
	for iter in range(len(list1)): #this is utilizing two functions: iter, and range. iter gives the numerical range of the range of list1
	
		print list1[iter] +"  <->  "+ list2[iter] #this prints list1 and list2 side by side, giving the user a choice between a <-> b
		
		uchoice	= raw_input("Make your hero selection here:") #this is where the user will be asked to make his/her selection 
		
		herolist.append(uchoice) #here, python is appeneding the users choice into the herolist 
		
	return herolist # after all the choices are made, this will return the herolist 
		

def Villainpicker(list1,list2): #this is the definition: Villainpicker, that is using heroesSW array and heroesTN array
	villainlist = []
	for iter in range(len(list1)):
		print list1[iter] +" <-> "+ list2[iter]
		uchoice = raw_input("Make your villain selection here:")
		villainlist.append(uchoice)
	return  villainlist
	
debug = raw_input("1")
herolist = Heropicker(heroesSW,heroesTN) 	
debug = raw_input("2")
print chosenlist #I am assigning the value of Heropicker to the variable chosenlist, this will display all the user's choices on one line 
	
debug = raw_input("3")
villainlist = Villainpicker(villainsSW, villainsTN)
print chosenlist 

debug = raw_input("4")
path = os.path.dirname(os.path.abspath(__file__))
debug = raw_input("5")
index = open(os.path.join(path, 'TURTLE1.txt'), 'r').read()
debug = raw_input("6")
entryStyle = open(os.path.join(path, 'TURTLE1.txt'), 'r').read()
debug = raw_input("7")
index = index.format(herolist[0], herolist[1], herolist[2], herolist[3], herolist[4], herolist[5], herolist[6], villainlist[0], villainlist[1], villainlist[2])
print index
debug = raw_input("8")

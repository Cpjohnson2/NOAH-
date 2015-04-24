from sys import argv
import os
import choice 





heroesSW = ['Luke Skywalker', 'Yoda', 'Han Solo', 'R2D2', 'C3PO', 'Chewbacca', 'Leia'] # I am setting the data structure for heroes
villainsSW=['Darth Vader','The Emperor', 'Jabba the Hut', ] # I am setting the data structure for Villains
heroesTN = ['Leonardo', 'Michelangelo', 'Donatello', 'Rapheal', 'Casey Jones', 'April', 'Master Splinter']
villainsTN = ['Shredder', 'Rock Steady', 'Bee Bop',]
storyTMNT = ['TURTLE1.txt', 'TURTLE2.txt']
storySW = 	['SW1.txt', 'SW2.txt']

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

	
		
		
def storyselector(path):
	star= os.listdir(path)
	for i in range(len(star)):
		print str(i + 1) + ") " + star[i]
	userchoice = int(raw_input("which story would you like?")) - 1 
	chosenpath = os.path.join(path, star[userchoice])
	chosenstory= os.path.userchoice.txt() #SOMETHING MUST GO HERE 
	
def stories(chosenpath):
	f = open(os.path.join(storiespath, star[i]), 'r').read()
	lines = f.readLines()
	return lines 
	f.close(os.path.join(storiespath, star[i]))
print stories 


def main():
	stories(sys.argv[1])
print main 
herolist = Heropicker(heroesTN, heroesSW)
	

  
	

villainlist = Villainpicker(villainsSW, villainsTN)





path = os.path.dirname(os.path.abspath(__file__))
storiespath = (os.path.join(path, 'STORIES')) 
 
storyselector(storiespath)


entryStyle = open(os.path.join(storiespath, chosenstory), 'r').read()




index = entryStyle.format(herolist[0], herolist[1], herolist[2], herolist[3], herolist[4], herolist[5], herolist[6], villainlist[0], villainlist[1], villainlist[2])
print index



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
	return chosenpath 
	
	
	
def stories(chosenpath):
	f = open(os.path.join(storiespath, star[i]), 'r').read()
	lines = f.readLines()
	return lines 
	f.close(os.path.join(storiespath, star[i]))
print stories 


# this is to parse the stories into a 100 word format, story represents the entry style of heroes and villains and the text files 
def comicstrip(story, maxwords):  
	#I want to parse 100 words or so of the txt file that has been chosen 
	allofthewords = story.split(" ")  # this represents every time a space is after a word in the text 
	counter = 0 # this is the counter that is set at zero, so it starts from the beginning of the story. 
	words = [" "]  #this develops a list 
	for  word in allofthewords:    #for the space in the length of the stories is 100,
		counter += 1
		words.append(word)
		if counter == maxwords:
			counter = 0
			print "\n" * 200
			# I want to add 100 words
			print  " ".join(words) 
			
			words = ["word"]
			raw_input("Press enter to continue") 
			
	
	

def main():
	stories(sys.argv[1])

herolist = Heropicker(heroesTN, heroesSW)

villainlist = Villainpicker(villainsSW, villainsTN)

path = os.path.dirname(os.path.abspath(__file__))

storiespath = (os.path.join(path, 'STORIES')) 
 
chosenstory = storyselector(storiespath)

entryStyle = open(os.path.join(storiespath, chosenstory), 'r').read()


story = entryStyle.format(herolist[0], herolist[1], herolist[2], herolist[3], herolist[4], herolist[5], herolist[6], villainlist[0], villainlist[1], villainlist[2])
comicstrip(story, 200)

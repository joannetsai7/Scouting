# scouting.py
#using pygame

# imports
import pygame
import time

# prompting
firstname = input("First Name: ")
lastname = input("Last Name: ")
match = input("Match #: ")
team = input("Team #: ")
color = input("Color: ")

# initialize pygame and initalize font
pygame.init()
pygame.font.init()

# Set screen
SCREEN_WIDTH = 1250
SCREEN_HEIGHT = 580

pygame.display.set_caption("Scouting")

# Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
GRAY = (112,138,144)

# load field image and scale to correct size
field = pygame.image.load("Strongholdfield.png")
field = pygame.transform.scale(field,(1250, 480)) #scaling to screen size

# Category A
portcullis = pygame.image.load("Portcullis.png")
portcullis = pygame.transform.scale(portcullis, (300,300))
chevaldefrise = pygame.image.load("ChevalDeFrise.png")
chevaldefrise = pygame.transform.scale(chevaldefrise, (300,300))

# Category B
moat = pygame.image.load("Moat.png")
moat = pygame.transform.scale(moat, (300,300))
ramparts = pygame.image.load("Ramparts.png")
ramparts = pygame.transform.scale(ramparts, (300,300))

# Category C
sallyport = pygame.image.load("SallyPort.png")
sallyport = pygame.transform.scale(sallyport, (300,300))
drawbridge = pygame.image.load("Drawbridge.png")
drawbridge = pygame.transform.scale(drawbridge, (300,300))

# Category D
rockwall = pygame.image.load("RockWall.png")
rockwall = pygame.transform.scale(rockwall, (300,300))
roughterrain = pygame.image.load("RoughTerrain.png")
roughterrain = pygame.transform.scale(roughterrain, (300,300))

# Low Bar
lowbar = pygame.image.load("LowBar.png")
lowbar = pygame.transform.scale(lowbar,(65,58))

# create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# create font
myfont = pygame.font.SysFont("monospace", 30, True, False)

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# stages of match
setup = True
auto = False
telop = False

# setup obstacle conditionals
obstacleclick = True
choosingA = False
choosingB = False
choosingC = False
choosingD = False
Achosen = False
Bchosen = False
Cchosen = False
Dchosen = False

# auto conditionals
start = True
crossreach = False

#auto radio buttons
class Cross_Reach():

	def ask(self):
		question = myfont.render("Did the robot cross or reach the obstacle?", 1, BLACK)
		# normal
		cross = myfont.render("Cross", 1, GRAY)
		reach = myfont.render("Reach", 1, GRAY)
		cancel = myfont.render("Cancel", 1, GRAY)
		# hover
		crossH = myfont.render("Cross", 1, BLACK)
		reachH = myfont.render("Reach", 1, BLACK)
		cancelH = myfont.render("Cancel", 1, BLACK)

		screen.blit(question, (300, 50))
		screen.blit(cross, (575, 300))
		screen.blit(reach, (575, 350))
		screen.blit(cancel, (575, 400))

		xpos, ypos = pygame.mouse.get_pos()
		if xpos > 525 and xpos < 675:
			if ypos > 275 and ypos < 325:
				screen.blit(crossH, (575, 300))
			elif ypos > 325 and ypos < 375:
				screen.blit(reachH, (575, 350))
			elif ypos > 375 and ypos < 425:
				screen.blit(cancelH, (575, 400))
		
		if event.type == pygame.MOUSEBUTTONDOWN:
			x, y = pygame.mouse.get_pos()
			if x > 525 and x < 675:
				if ypos > 275 and ypos < 325:
					time.sleep(.3)
					cr = "cross"
					return False, cr
				elif y > 325 and y < 375:
					time.sleep(.3)
					cr = "reach"
					return False, cr
				elif y > 375 and y < 425:
					time.sleep(.3)
					return ("", False)

while setup:# setup loop
	# set label's words and color
	label = myfont.render("Select an obstacle", 1, BLACK)
	part = myfont.render("Set Up", 1 , BLACK)

	screen.fill(WHITE)# Background color
	
	screen.blit(field, (0, 100))# display screen
	
	screen.blit(lowbar, (440, 469))# display lowbar
	
	if Achosen:# display chosen obstacle A
		screen.blit(chosenA, (440, 406))
	
	if Bchosen:# display chosen obstacle B
		screen.blit(chosenB, (440, 345))

	if Cchosen:# display chosen obstacle C
		screen.blit(chosenC, (440, 280))
	
	if Dchosen:# display chosen obstacle D
		screen.blit(chosenD, (440, 220))

	screen.blit(part, (575, 0))# display part of game
	
	if Achosen and Bchosen and Cchosen and Dchosen:# Switching modes if setup is done to auto
		setup = False
		auto = True
		print("Auto")

	for event in pygame.event.get():# if quit
		if event.type == pygame.QUIT:
			setup = False
	
	if obstacleclick: # choosing which obstacles to set
		if event.type == pygame.MOUSEBUTTONDOWN:
			x,y = pygame.mouse.get_pos()
			print (str(x) + ", " + str(y))
			if x > 440 and x < 505:
				if y > 405 and y < 470: # 405 - 470, obstacle 2
					choosingA = True 
					obstacleclick = False
					time.sleep(.3) # delay so click doesn't register as multiple clicks
				elif y > 345 and y < 405: # 325 - 405, obstacle 3
					choosingB = True
					obstacleclick = False
					time.sleep(.3)
				elif y > 285 and y < 345: # 285 - 345, obstacle 4
					choosingC = True
					obstacleclick = False
					time.sleep(.3)
				elif y > 220 and y < 285: # 220 - 285, obstacle 5
					choosingD = True
					obstacleclick = False
					time.sleep(.3)

	else: # choosing which type of obstacles
		if choosingA:
			screen.blit(portcullis, (300,200))
			screen.blit(chevaldefrise, (650, 200))
			screen.blit(label, (475, 50))
			if event.type == pygame.MOUSEBUTTONDOWN:
				xcoor, ycoor = pygame.mouse.get_pos()
				print (str(xcoor) + ", " + str(ycoor))
				if ycoor > 200 and ycoor < 500:
					if xcoor > 300 and xcoor < 600:
						Achosen = True
						choosingA = False
						obstacleclick = True
						chosenA = pygame.transform.scale(portcullis, (65,62))
						time.sleep(.3)
					elif xcoor > 650 and xcoor < 950:
						Achosen = True
						choosingA = False
						obstacleclick = True
						chosenA = pygame.transform.scale(chevaldefrise, (65,62))
						time.sleep(.3)
		elif choosingB:
			screen.blit(moat, (300, 200))
			screen.blit(ramparts, (650, 200))
			screen.blit(label, (475, 50))
			if event.type == pygame.MOUSEBUTTONDOWN:
				xcoor, ycoor = pygame.mouse.get_pos()
				print (str(xcoor) + ", " + str(ycoor))
				if ycoor > 200 and ycoor < 500:
					if xcoor > 300 and xcoor < 600:
						Bchosen = True
						choosingB = False
						obstacleclick = True
						chosenB = pygame.transform.scale(moat, (65,62))
						time.sleep(.3)
					elif xcoor > 650 and xcoor < 950:
						Bchosen = True
						choosingB = False
						obstacleclick = True
						chosenB = pygame.transform.scale(ramparts, (65,62))
						time.sleep(.3)
		elif choosingC:
			screen.blit(sallyport, (300, 200))
			screen.blit(drawbridge, (650, 200))
			screen.blit(label, (475, 50))
			if event.type == pygame.MOUSEBUTTONDOWN:
				xcoor, ycoor = pygame.mouse.get_pos()
				print (str(xcoor) + ", " + str(ycoor))
				if ycoor > 200 and ycoor < 500:
					if xcoor > 300 and xcoor < 600:
						Cchosen = True
						choosingC = False
						obstacleclick = True
						chosenC = pygame.transform.scale(sallyport, (65,65))
						time.sleep(.3)
					elif xcoor > 650 and xcoor < 950:
						Cchosen = True
						choosingC = False
						obstacleclick = True
						chosenC = pygame.transform.scale(drawbridge, (65,65))
						time.sleep(.3)
		elif choosingD:
			screen.blit(rockwall, (300, 200))
			screen.blit(roughterrain, (650, 200))
			screen.blit(label, (475, 50))
			if event.type == pygame.MOUSEBUTTONDOWN:
				xcoor, ycoor = pygame.mouse.get_pos()
				print (str(xcoor) + ", " + str(ycoor))
				if ycoor > 200 and ycoor < 500:
					if xcoor > 300 and xcoor < 600:
						Dchosen = True
						choosingD = False
						obstacleclick = True
						chosenD = pygame.transform.scale(rockwall, (65,65))
						time.sleep(.3)
					elif xcoor > 650 and xcoor < 950:
						Dchosen = True
						choosingD = False
						obstacleclick = True
						chosenD = pygame.transform.scale(roughterrain, (65,65))
						time.sleep(.3)

	pygame.display.flip()

while auto:# auto loop

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			auto = False

	# set label's words and color
	part = myfont.render("Auto", 1, BLACK)
	label = myfont.render("Click on the starting position", 1, BLACK)
	pos1 = myfont.render("1", 1, BLACK)
	pos2 = myfont.render("2", 1, BLACK)
	pos3 = myfont.render("3", 1, BLACK)
	pos4 = myfont.render("4", 1, BLACK)
	pos5 = myfont.render("5", 1, BLACK)
	pos6 = myfont.render("6", 1, BLACK)

	screen.fill(WHITE)
	screen.blit(field, (0, 100))
	screen.blit(lowbar, (440, 469))
	screen.blit(chosenA, (440, 406))
	screen.blit(chosenB, (440, 345))
	screen.blit(chosenC, (440, 280))
	screen.blit(chosenD, (440, 220))
	screen.blit(part, (600, 0))

	if start:
		#Labeling starting position
		screen.blit(label, (400, 50))
		screen.blit(pos1, (585, 240))
		screen.blit(pos2, (585, 300))
		screen.blit(pos3, (585, 360))
		screen.blit(pos4, (585, 420))
		screen.blit(pos5, (585, 485))
		screen.blit(pos6, (185, 485))

		if event.type == pygame.MOUSEBUTTONDOWN:
			x,y = pygame.mouse.get_pos()
			print (str(x) + ", " + str(y))
			if x > 570 and x < 620:
				if y > 230 and y < 280:
					startingpos = 1
					print(startingpos)
					start = False
					time.sleep(.3)
				elif y > 290 and y < 340:
					startingpos = 2
					print(startingpos)
					start = False
					time.sleep(.3)
				elif y > 350 and y < 400:
					startingpos = 3
					print(startingpos)
					start = False
					time.sleep(.3)
				elif y > 410 and y < 460:
					startingpos = 4
					print(startingpos)
					start = False
					time.sleep(.3)
				elif y > 475 and y < 525:
					startingpos = 5
					print(startingpos)
					start = False
					time.sleep(.3)
			elif x > 170 and x < 220:
				if y > 475 and y < 525:
					startingpos = 6
					print(startingpos)
					start = False
					time.sleep(.3)

	else:
		if event.type == pygame.MOUSEBUTTONDOWN:
			xcoor,ycoor = pygame.mouse.get_pos()
			print (str(x) + ", " + str(y))
			if xcoor > 440 and xcoor < 505:
				if ycoor > 470 and ycoor < 525: # 470 - 525, obstacle 1 (low bar)
					crobstacle = "Low Bar"
					crossreach = True
					time.sleep(.3)
				elif ycoor > 405 and ycoor < 470: # 405 - 470, obstacle 2
					crobstacle = "Obstacle 2"
					crossreach = True
					time.sleep(.3) # delay so click doesn't register as multiple clicks
				elif ycoor > 345 and ycoor < 405: # 325 - 405, obstacle 3
					crobstacle = "Obstacle 3"
					crossreach = True
					time.sleep(.3)
				elif ycoor > 285 and ycoor < 345: # 285 - 345, obstacle 4
					crobstacle = "Obstacle 4"
					crossreach = True
					time.sleep(.3)
				elif ycoor > 220 and ycoor < 285: # 220 - 285, obstacle 5
					crobstacle = "Obstacle 5"
					crossreach = True
					time.sleep(.3)

	if crossreach:
		c_r = Cross_Reach()
		if y > 470 and y < 525:
			crossreach, crlb = c_r.ask()
			print(crlb)
		elif ycoor > 405 and ycoor < 470:
			crossreach, cra = c_r.ask()
			print(cra)
		elif ycoor > 345 and ycoor < 405:
			crossreach, crb = c_r.ask()
			print(crb)
		elif ycoor > 285 and ycoor < 345: 
			crossreach, crc = c_r.ask()
			print(crc)
		elif ycoor > 220 and ycoor < 285:
			crossreach, crd = c_r.ask()
			print(crd)

	pygame.display.flip()

while telop: #telop loop

	screen.fill(WHITE)# Background color
	screen.blit(field, (0, 100))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			telop = False
	
	if event.type == pygame.MOUSEBUTTONDOWN:
			x,y = pygame.mouse.get_pos()
			print (str(x) + ", " + str(y))

	pygame.display.flip()

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
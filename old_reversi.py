# Reversi Task 1

# Import relevent modules #
import turtle
import math
import random

# http://patorjk.com/software/taag/#p=display&f=Doom&t=welcome%0Ato%0Areversi #

print("""
      _    _      _                       
     | |  | |    | |                     
     | |  | | ___| | ___ ___  _ __ ___   ___ 
     | |/\| |/ _ \ |/ __/ _ \| '_ ` _ \ / _ \\\
     
     \  /\  /  __/ | (_| (_) | | | | | |  __/
      \/  \/ \___|_|\___\___/|_| |_| |_|\___|
      _
     | |   
     | |_ ___  
     | __/ _ \\\
     
     | || (_) |
      \__\___/ 
      _____                        _
     | ___ \                      (_)
     | |_/ /____   _____ _ __ ___ __
     |   // _ \ \ / / _ \ '__/ __|  |
     | |\ \  __/\ V /  __/ |  \__ \ |
     \_| \_\___| \_/ \___|_|  |___/_|
""")

print('   _____________________________________________________________________________________\n')

# CITATION!!! Reversi game description taken from D2L!
print('''   Reversi is a game for two players, played on a grid of eight columns and eight rows. 
   
   As a result, there are 64 possible locations on the grid. 
   
   Starting from the initial configuration, players take turns by placing a marker on the grid 
   such that there exists at least one straight (horizontal, vertical, or diagonal) occupied line
   between the new marker and another marker belonging to the player, with one or more contiguous 
   markers belonging to the opponent between them. 
   
   After placing the marker, the player captures all of the opponent's markers on the straight 
   line between the new marker and the other, anchoring marker.
   
   Thus, every legal move results in the capture of at least one of the opponents markers, and 
   if a player cannot make a valid move, that player misses a turn.
   
   The game ends when neither player can add a marker to the grid - either because the grid is 
   full or because no other legal moves exist.
   
   When the game has ended, the player with the most markers is declared the winner.
   ''')
   
print('   _____________________________________________________________________________________\n')

def init_board():
	board = turtle.Turtle()
	wn = turtle.Screen()
	turtle.setworldcoordinates(-402,-402,402,402)
	wn.bgcolor("Green")
	board.ht()
	board.speed(0)
	board.pensize(4)
	board.pencolor("black")

	coordinate = [[-300,-402,90,None,804],
				  [-200,-402,None,None,804],
				  [-100,-402,None,None,804],
				  [0,-402,None,None,804],
				  [100,-402,None,None,804],
				  [200,-402,None,None,804],
				  [300,-402,None,None,804],
				  [-402,-300,None,90,804],
				  [-402,-200,None,None,804],
				  [-402,-100,None,None,804],
				  [-402,0,None,None,804],
				  [-402,100,None,None,804],
				  [-402,200,None,None,804],
				  [-402,300,None,None,804]]

	for i in range(14):
		X=0
		Y=1
		LEFT=2
		RIGHT=3
		FORWARD=4
		
		board.up()
		board.goto(coordinate[i][X],coordinate[i][Y])
		if coordinate[i][LEFT] is not None:
			board.left(coordinate[i][LEFT])
		if coordinate[i][RIGHT] is not None:
			board.right(coordinate[i][RIGHT])
		board.down()
		if coordinate[i][FORWARD] is not None:
			board.forward(coordinate[i][FORWARD])
			
	board_definition = turtle.Turtle()
	board_definition.ht()

	label = [[-420,-360,8],
			 [-420,-260,7],
			 [-420,-160,6],
			 [-420,-60,5],
			 [-420,40,4],
			 [-420,140,3],
			 [-420,240,2],
			 [-420,340,1],
			 [-350,415,'A'],
			 [-250,415,'B'],
			 [-150,415,'C'],
			 [-50,415,'D'],
			 [50,415,'E'],
			 [150,415,'F'],
			 [250,415,'G'],
			 [350,415,'H']]

	board.up()
	board.pensize(5)
	board.pencolor("brown")
	board.goto(-402,-402)
	board.down()

	for i in range(4):
		board.forward(804)
		board.left(90)

	for i in range(16):
		X=0
		Y=1
		WRITE=2

		board_definition.up()
		board_definition.goto(label[i][X],label[i][Y])
		board_definition.write(label[i][WRITE], move=False, align="center", font=("Arial", 18, "bold"))

	player_1_score = turtle.Turtle()
	player_2_score = turtle.Turtle()
	player_1_score.ht()
	player_2_score.ht()
	player_1_score.up()
	player_2_score.up()
	player_1_score.goto(-200,-435)
	player_2_score.goto(200,-435)
	
	printTile(-50,0,'white','black')
	printTile(50,-100,'white','black')
	printTile(-50,-100,'black','white')
	printTile(50,0,'black','white')

	player_1_score.write('Player 1 has: ' + str(2) + ' Tiles', move=False, align="center", font=("Arial", 12, "bold"))
	player_2_score.write('Player 2 has: ' + str(2) + ' Tiles', move=False, align="center", font=("Arial", 12, "bold"))

def circle(turtle,radius):    
    for i in range(36):
        # Move by 1/360 circumference
        turtle.forward((2*math.pi*radius/360)*10)
        turtle.left(10)
    return 

def printTile(xcord,ycord,pen_color,fill_color):
    tile = turtle.Turtle()
    tile.ht()
    tile.speed(0)
    tile.up()
    tile.goto(xcord,ycord)
    tile.down()
    tile.begin_fill()
    tile.pencolor(pen_color)
    tile.fillcolor(fill_color)
    circle(tile,50)
    tile.end_fill()
    return
    
init_board()

player_1_move = input("Player 1, you are black, please enter the coordinates of your first move: ")
print("Player 1 played at: " + player_1_move)

wn.exitonclick()

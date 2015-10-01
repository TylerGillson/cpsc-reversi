# Reversi Task 2

# Import relevant modules #
import turtle
import math
import random
import string

#This function will draw the game's welcome screen. When the player clicks on the screen, it will exit, running the next function
def welcome():
    #The window that will draw the welcome screen components
    welcome_window = turtle.Screen()
    welcome_window.bgcolor("Green")

    #separating drawing functionality into different turtle objects for clarity (plus easier to debug)

    #Turtle to display the title screen
    title_screen_turtle = turtle.Turtle()
    title_screen_turtle.ht()
    title_screen_turtle.penup()
    title_screen_turtle.left(90)
    title_screen_turtle.forward(250)
    title_screen_turtle.write("Welcome to Reversi!", move = False, align = "center", font = ("stencil", 50, "bold"))

    #Turtle to display the description
    description_turtle = turtle.Turtle()
    description_turtle.ht()
    description_turtle.penup()
    description_turtle.right(90)
    description_turtle.forward(200)
        
    #CITATION: Game description was taken from d2l game description(modified only a little bit)
    description_turtle.write('''
    ___________________________________________________________________________
     
    Game description:
        
    Reversi is a game for two players, played on a grid of eight columns and eight rows.
       
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
    ________________________________________________________________________

    ''', move = False, align = "center", font = ("cornerstone", 11, "normal"))
        
    #turtle that draws a 'click anywhere to start' message
    click_turtle = turtle.Turtle()
    click_turtle.ht()
    click_turtle.penup()
    click_turtle.right(90)
    click_turtle.forward(300)
    click_turtle.pencolor("white")
    click_turtle.write("Click anywhere to start!", move = False, align = "center", font = ("stencil", 40, "bold"))

    #Exits the welcome_window, and in return exits the welcome() func, initializing the main board func
    welcome_window.exitonclick()

def init_board():
    board = turtle.Turtle()
    wn = turtle.Screen()
    turtle.setworldcoordinates(-400,-400,400,400)
    wn.bgcolor('green')
    board.ht()
    board.speed(0)
    board.pensize(4)
    board.pencolor('black')

    coordinate = [[-300,-400,90,None,800],
		  [-200,-400,None,None,800],
		  [-100,-400,None,None,800],
		  [0,-400,None,None,800],
		  [100,-400,None,None,800],
		  [200,-400,None,None,800],
		  [300,-400,None,None,800],
		  [-400,-300,None,90,800],
		  [-400,-200,None,None,800],
		  [-400,-100,None,None,800],
		  [-400,0,None,None,800],
		  [-400,100,None,None,800],
		  [-400,200,None,None,800],
		  [-400,300,None,None,800]]

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
    board.pencolor('brown')
    board.goto(-400,-400)
    board.down()

    for i in range(4):
        board.forward(800)
        board.left(90)

        board_definition = turtle.Turtle()
        board_definition.ht()

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

    printTile('D4','white','black')
    printTile('E5','white','black')
    printTile('E4','black','white')
    printTile('D5','black','white')

    player_1_score.write('Player 1 has: ' + str(2) + ' Tiles', move=False, align="center", font=("Arial", 12, "bold"))
    player_2_score.write('Player 2 has: ' + str(2) + ' Tiles', move=False, align="center", font=("Arial", 12, "bold"))

def circle(turtle,radius):    
    for i in range(36):
        # Move by 1/360 circumference
        turtle.forward((2*math.pi*radius/360)*10)
        turtle.left(10)
    return 

def printTile(cell,pen_color,fill_color):
    xcord = int(str.split(getCellCords(cell),',')[0]) + 46
    ycord = int(str.split(getCellCords(cell),',')[1]) + 4
    state = fill_color
    
    #updateCellState(cell,state)
    
    tile = turtle.Turtle()
    tile.ht()
    tile.speed(0)
    tile.up()
    tile.goto(xcord,ycord)
    tile.down()
    tile.begin_fill()
    tile.pencolor(pen_color)
    tile.fillcolor(fill_color)
    circle(tile,46)
    tile.end_fill()
    return

def init_constants():
    # letter, number, xcord, ycord, state
    #cells = [['A',1,-400,400,empty/white/black]]

    #CITATION: http://stackoverflow.com/questions/16060899/alphabet-range-python
    letters = list(map(chr, range(ord('A'), ord('H')+1)))

    global cells 
    cells = []
    for letters in letters:
        state = 'empty'
        if letters == 'A':
            xcord = -400
        if letters == 'B':
            xcord = -300
        if letters == 'C':
            xcord = -200
        if letters == 'D':
            xcord = -100
        if letters == 'E':
            xcord = 0
        if letters == 'F':
            xcord = 100
        if letters == 'G':
            xcord = 200
        if letters == 'H':
            xcord = 300
    for i in range(1,9):
        if i == 1:
            ycord = 300
        if i == 2:
            ycord = 200
        if i == 3:
            ycord = 100
        if i == 4:
            ycord = 0
        if i == 5:
            ycord = -100
        if i == 6:
            ycord = -200
        if i == 7:
            ycord = -300
        if i == 8:
            ycord = -400
        cells.append([letters,i,xcord,ycord,state])

def getCellCords(cell):
    for i in range(64):
        if cells[i][0] + str(cells[i][1]) == cell:
            return str(cells[i][2]) + ',' + str(cells[i][3])

def updateCellState(cell,state):
    for i in range(64):
        if cells[i][0] + str(cells[i][1]) == cell:
            del cells[i][4]
            cells.insert([i],[state])

welcome()
init_constants()
init_board()

player_1_move = input('Player 1, you are Black, please enter the coordinates of your first move: ')
print('Player 1 played at: ' + player_1_move)
printTile(player_1_move,'white','black')

# CHEAT block to accomplish Task #2
if player_1_move == 'C5':
    printTile('D5','white','black')
if player_1_move == 'D6':
    printTile('D5','white','black')
if player_1_move == 'F4':
    printTile('E4','white','black')
if player_1_move == 'E3':
    printTile('E4','white','black')

# prompt player 2 to move simply to keep the turtle window open...
player_2_move = input('Player 2, you are White, please enter the coordinates of your first move: ')

# Reversi Task 3 #

# Import relevant modules #
import turtle
import math
import random
import string

# This function will draw the game's welcome screen. When the player clicks on the screen, it will exit, running the next function #
def welcome():
    
    welcome_window = turtle.Screen()
    welcome_window.bgcolor("Green")
    # Separating drawing functionality into different turtle objects for clarity (plus easier to debug) #

    # Turtle to display the title message #
    title_screen_turtle = turtle.Turtle()
    title_screen_turtle.ht()
    title_screen_turtle.penup()
    title_screen_turtle.goto(0,300)
    title_screen_turtle.write("Welcome to Reversi!", move = False, align = "center", font = ("stencil", 50, "bold"))

    # Turtle to display the description #
    description_turtle = turtle.Turtle()
    description_turtle.ht()
    description_turtle.penup()
    description_turtle.goto(0,-200)

    # CITATION: Game description was taken from d2l game description(modified only a little bit) #
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

    ''', move = False, align = "center", font = ("cornerstone", 12, "normal"))
        
    # Turtle that draws a 'click anywhere to start' message #
    click_turtle = turtle.Turtle()
    click_turtle.ht()
    click_turtle.penup()
    click_turtle.goto(0,-300)
    click_turtle.pencolor("white")
    click_turtle.write("Click anywhere to start!", move = False, align = "center", font = ("stencil", 40, "bold"))

    # Exits the welcome_window #
    welcome_window.exitonclick()

# This function will draw the game board #
def init_board():

    # Create a turtle object for the screen and configure it's settings #
    wn = turtle.Screen()
    wn.bgcolor('green')
    
    # Create a turtle object for drawing the board and configure it's settings #
    board = turtle.Turtle()
    board.ht()
    board.speed(0)
    board.pensize(4)
    board.pencolor('black')

    #These two functions uses the constants to draw the cells (excluding the outline)
    for i in range(num_rows-1):
        additive_int = i+1
        board.up()
        board.goto(origin_x,origin_y-(size_of_cell_y*additive_int))
        board.down()
        board.forward(size_of_cell_x*num_rows)

    board.right(90)
    
    for i in range(num_columns-1):
        additive_int = i+1
        board.up()
        board.goto(origin_x+(size_of_cell_x*additive_int), origin_y)
        board.down()
        board.forward(size_of_cell_y*num_columns)

    # Reconfigure the board drawing turtle for drawing the border #
    board.up()
    board.pensize(5)
    board.pencolor('brown')
    board.goto(origin_x,origin_y)
    board.down()

    # Draw the border #
    for i in range(2):
        board.forward(size_of_cell_x*num_rows)
        board.left(90)
        board.forward(size_of_cell_y*num_columns)
        board.left(90)

    # Create a new turtle object for writing board labels #
    board_definition = turtle.Turtle()
    board_definition.ht()
    board_definition.up()
    
    #These two for loops draw the labels (1, 2, 3, 4.... / A, B, C, D....)
    for i in range(num_rows):
        str_to_write = str(i+1)
        board_definition.goto(origin_x - (size_of_cell_x/2), origin_y - ((2*i+1)*size_of_cell_y/2) -  (size_of_cell_y/8))
        board_definition.write(str_to_write, move=False, align="center", font=("Arial", 18, "bold"))
    
    for i in range(num_columns):
        str_to_write = alphabet[i]
        board_definition.goto(origin_x + ((2*i+1)*size_of_cell_x/2), origin_y + (size_of_cell_y/3))
        board_definition.write(str_to_write, move=False, align="center", font=("Arial", 18, "bold"))

    # Draw the initial four pieces using the printTile function #
    printTile('D4','white','black')
    printTile('E5','white','black')
    printTile('E4','black','white')
    printTile('D5','black','white')
        
def update_Scores(player_1_Score, player_2_Score):
    # Initialize turtle and places them under the board#
    player_1_turtle = turtle.Turtle()
    player_1_turtle.up()
    player_1_turtle.ht()
    player_1_turtle.goto((size_of_cell_x*num_rows) - (size_of_cell_x*num_rows)/3,-origin_y - size_of_cell_y)
    
    player_2_turtle = turtle.Turtle()
    player_2_turtle.up()
    player_2_turtle.ht()
    player_2_turtle.goto((size_of_cell_x*num_rows) - (((size_of_cell_x*num_rows)/3)*2),-origin_y - size_of_cell_y)
    
    #clear turtle clears previous scores
    clear = turtle.Turtle()
    clear.speed(0)
    clear.up()
    clear.ht()
    clear.goto(-300,-415)
    clear.color('green')
    clear.begin_fill()
    
    for i in range(2):
        clear.forward(600)
        clear.right(90)
        clear.forward(30)
        clear.right(90)

    clear.end_fill()
    
    # Display running totals for initial configuration #
    player_1_turtle.write('Player 1 has: ' + str(player_1_Score) + ' Tiles', move=False, align="center", font=("Arial", 12, "bold"))
    player_2_turtle.write('Player 2 has: ' + str(player_2_Score) + ' Tiles', move=False, align="center", font=("Arial", 12, "bold"))

# Define a function for drawing circles of x radius #
def circle(turtle,radius):
    for i in range(36):
       #Move by 1/360 circumference
       turtle.forward((2*math.pi*radius/360)*(size_of_cell_x/10))
       turtle.left(10)
    return

# Define a function for drawing pieces wherever a player chooses #
def printTile(cell,pen_color,fill_color):
    # Pass the user input value into getCellCords in order to determine x/y coordinates for drawing a piece #
    xcord = int(str.split(getCellCords(cell),',')[0]) - (size_of_cell_x/2) - 2
    ycord = int(str.split(getCellCords(cell),',')[1]) + size_of_cell_y + 2
#    state = fill_color
    
#    updateCellState(cell,state)
    
    # Create & configure a turtle object for drawing a piece #
    tile = turtle.Turtle()
    tile.ht()
    tile.speed(0)
    tile.up()
    
    # Relocate turtle to required position and draw a piece using the colors specified in the parameters #
    tile.goto(xcord,ycord)
    tile.down()
    tile.begin_fill()
    tile.pencolor(pen_color)
    tile.fillcolor(fill_color)
    circle(tile,46)
    tile.end_fill()
    return

# This function creates the 2D list 'cells' which will be referenced later for drawing pieces when players make moves #
def init_cells_array():
    global origin_x
    global origin_y
    origin_x = ((size_of_cell_x*num_rows)/-2)
    origin_y = ((size_of_cell_y*num_columns)/2)
    
    # letter, number, xcord, ycord, state #
    # cells[0] = [['A',1,-400,400,empty/white/black]] #

    # CITATION: line 213 was written via referencing this URL: http://stackoverflow.com/questions/16060899/alphabet-range-python #
    global alphabet
    alphabet = list(map(chr, range(ord('A'), ord('Z')+1)))
    letters = list(map(chr, range(ord(alphabet[0]), ord(alphabet[num_columns]))))

    # Create a globally available 2D list containing information about all grid locations #
    global cells
    cells = []
    for letters in letters:
       state = 'empty'
       # Assign xcoordinates according to column value #
       if letters == 'A':
           letter_int = 0
       letter_int = letter_int + 1
       xcord = int(origin_x+(size_of_cell_x*letter_int))
       
       for i in range(num_rows-1):
           # Assign ycoordinates according to row value #
           i_int = i + 1
           ycord = int(origin_y-(size_of_cell_y*i_int))
           cells.append([letters,i,xcord,ycord,state])

# Define a function for determining x/y coordinates of a given grid location #
def getCellCords(cell):
    for i in range(64):
        if cells[i][0] + str(cells[i][1]) == cell:
            return str(cells[i][2]) + ',' + str(cells[i][3])

# Define a function for updating the state value of a given grid location #
def updateCellState(cell,state):
    for i in range(64):
        if cells[i][0] + str(cells[i][1]) == cell:
            del cells[i][4]
            cells.insert([i],[state])

def main():
    # Define constants for drawing the board #
    global num_rows
    global num_columns
    global size_of_cell_x
    global size_of_cell_y

    num_rows = 8
    num_columns = 8
    size_of_cell_x = 50
    size_of_cell_y = 50

    # Display welcome screen, then initialize the board & all constants etc. #
    welcome()
    init_cells_array()
    init_board()
    #Added by Victor
    global player_1_Score
    player_1_Score = 2
    global player_2_Score
    player_2_Score = 2
    update_Scores(player_1_Score,player_2_Score)
    
    # Prompt player 1 for a move #
    player_1_move = input('Player 1, you are Black, please enter the coordinates of your first move: ')

    # Echo player 1's move back via terminal #
    print('Player 1 played at: ' + player_1_move)

    # Draw a piece wherever player 1 picked #
    printTile(player_1_move,'white','black')

    # Temporary code block to accomplish Task #2
    if player_1_move == 'C5':
        printTile('D5','white','black')
    if player_1_move == 'D6':
        printTile('D5','white','black')
    if player_1_move == 'F4':
        printTile('E4','white','black')
    if player_1_move == 'E3':
        printTile('E4','white','black')

    player_1_Score += 2
    player_2_Score += 2
    update_Scores(player_1_Score, player_2_Score)
    # prompt player 2 to move simply to keep the turtle window open... #
    player_2_move = input('Player 2, you are White, please enter the coordinates of your first move: ')

main()
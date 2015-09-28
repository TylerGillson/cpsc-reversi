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

board = turtle.Turtle()
wn = turtle.Screen()
turtle.setworldcoordinates(-402,-402,402,402)
wn.bgcolor("Green")
board.ht()
board.speed(0)
board.pensize(4)
board.pencolor("black")

for i in range(14):
    if i == 0:
        board.up()
        board.goto(-300,-402)
        board.left(90)
        board.down()
        board.forward(804)
    if i == 1:
        board.up()
        board.goto(-200,-402)
        board.down()
        board.forward(804)
    if i == 2:
        board.up()
        board.goto(-100,-402)
        board.down()
        board.forward(804)
    if i == 3:
        board.up()
        board.goto(-0,-402)
        board.down()
        board.forward(804)
    if i == 4:
        board.up()
        board.goto(100,-402)
        board.down()
        board.forward(804)
    if i == 5:
        board.up()
        board.goto(200,-402)
        board.down()
        board.forward(804)
    if i == 6:
        board.up()
        board.goto(300,-402)
        board.down()
        board.forward(804)
    if i == 7:
        board.up()
        board.goto(-402,-300)
        board.right(90)
        board.down()
        board.forward(804)
    if i == 8:
        board.up()
        board.goto(-402,-200)
        board.down()
        board.forward(804)
    if i == 9:
        board.up()
        board.goto(-402,-100)
        board.down()
        board.forward(804)
    if i == 10:
        board.up()
        board.goto(-402,0)
        board.down()
        board.forward(804)
    if i == 11:
        board.up()
        board.goto(-402,100)
        board.down()
        board.forward(804)
    if i == 12:
        board.up()
        board.goto(-402,200)
        board.down()
        board.forward(804)
    if i == 13:
        board.up()
        board.goto(-402,300)
        board.down()
        board.forward(804)
        

board.up()
board.pensize(5)
board.pencolor("brown")
board.goto(-402,-402)
board.down()

for i in range(4):
    board.forward(804)
    board.left(90)

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
    
printTile(-50,0,'white','black')
printTile(50,-100,'white','black')
printTile(-50,-100,'black','white')
printTile(50,0,'black','white')

player_1_move = input("Player 1, you are black, please enter the coordinates of your first move: ")
print("Player 1 played at: " + player_1_move)

wn.exitonclick()
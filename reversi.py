# Reversi Task 1
# Alejandro, dogsTyler, and Victor

# Display ASCII Art welcome screen
# CITATION!!! ASCII Art taken from: "http://patorjk.com/software/taag/#p=display&h=0&v=0&f=Doom&t=Welcome%0Ato%0AReversi"
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

print("   _______________________________________________________________________________________________\n")

# Display brief introduction to Reversi
# CITATION!!! Reversi game description taken from D2L!
print('''   Game Description:

     Reversi is a game for two players, identified here as X's and O's.

     Reversi is played on a grid of eight (8) columns and eight (8) rows.

     As a result, there are 64 possible locations on the grid. 

     Each player starts the game with two markers on the grid in the initial configuration depicted below.
     Starting from the initial configuration players take turns by placing a marker on the grid such that there
     exists at least one straight (horizontal, vertical, or diagonal) occupied line between the new marker and 
     another marker belonging to the player, with one or more contiguous markers belonging to the opponent between them.
     After placing the marker, the player captures all of the opponent's markers on the straight line between the 
     new marker and the other, anchoring marker. Thus, every legal move results in the capture of at least one of the 
     opponents markers, and if a player cannot make a valid move, that player misses a turn.

     The game ends when neither player can add a marker to the grid - either because the grid is full or because 
     no other legal moves exist. When the game has ended, the player with the most markers is declared the winner.
''')

print("   _______________________________________________________________________________________________\n")

# Display game board in starting configuration
print("""            |_A_|_B_|_C_|_D_|_F_|_G_|_H_|_I_|
          1 |___|___|___|___|___|___|___|___|
          2 |___|___|___|___|___|___|___|___|
          3 |___|___|___|___|___|___|___|___|
          4 |___|___|___|_X_|_O_|___|___|___|
          5 |___|___|___|_O_|_X_|___|___|___|
          6 |___|___|___|___|___|___|___|___|
          7 |___|___|___|___|___|___|___|___|
          8 |___|___|___|___|___|___|___|___|
          
          """)

# Prompt player 1 for a move, then echo the move player 1 chooses back to the screen
player_1_move = input("Player 1, you are X's, please enter the coordinates of your first move: ")
print("Player 1 played at: " + player_1_move)

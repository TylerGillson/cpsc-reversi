    global cells
    cells = []
    for letters in letters:
       state = 'empty'
       # Assign xcoordinates according to column value #
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
           # Assign ycoordinates according to row value #
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
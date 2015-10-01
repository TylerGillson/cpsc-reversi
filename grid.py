# http://stackoverflow.com/questions/7001144/range-over-character-in-python

def char_range(c1,c2):
    """Generates the characters from `c1` to `c2`, inclusive."""
    for c in range(ord(c1), ord(c2)+1):
        character = chr(c)
        return(character)

for i in range(8):
	print(char_range('A','H') + 'A')


#for i in range(64):
	

#for letter in range(1,9):

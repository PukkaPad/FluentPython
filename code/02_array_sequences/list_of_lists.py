# Building lists of lists
board = [['_'] * 3 for i in range(3)] 
print(board)
board[1][2] = 'X'
print(board)
print('###')

# wrong way of doing the above:
board = [['_'] * 3] * 3
print(board)
board[1][2] = 'O' # all rows are aliases referring to the same object
print(board)

row=['_']*3 
board = []
for i in range(3):
	board.append(row)

# correct way
board = []
for i in range(3):
	row = ['_'] * 3 # each iteration builds a new row
	board.append(row)
print(board)
board[2][0] = 'X'
print(board)








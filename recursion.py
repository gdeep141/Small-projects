"""
"""Solve a maze using recursive backtracking
"""

string = """\
#################
#       ###    ##
# #### #### ## ##
# ####      ## ##
# ############ ##
# *  ## #       #
####      #### ##
#################
"""
# get height and width of maze
height = 0
width = 0

for i in string:
	if i == "\n":
		break
	else:
		width += 1

for j in string:
	if j == "\n":
		height += 1

# create maze
maze = []
for i in range(height):
	row = []
	for j in range(width):
		col = ' '
		row.append(col)
	maze.append(row)

# set values in maze to string
row = 0
col = 0
for i in string:
	if i == '\n':
		row += 1
		col = 0
	else:
		maze[row][col] = i
		col += 1

# solve maze
def solve(row, col):
	maze[row][col] = '.'

	# check values surrounding current location
	for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
		if maze[row + i][col + j] == '*':
			print("solution found")						
			print_maze()
			input("Continue?")

		elif maze[row + i][col + j] == ' ':
			solve(row + i, col + j)	
			maze[row + i][col + j] = ' '
      
	return False

def print_maze():
	for row in maze:
		for col in row:
			print(col, end = '')
		print()

solve(1, 1)
print("No more solutions found")

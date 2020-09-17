
#Testing Board (not important)
board =[5,3,0,0,7,0,0,0,0,
	 	6,0,0,1,9,5,0,0,0,
		0,9,8,0,0,0,0,6,0,
		8,0,0,0,6,0,0,0,3,
		4,0,0,8,0,3,0,0,1,
		7,0,0,0,2,0,0,0,6,
		0,6,0,0,0,0,2,8,0,
		0,0,0,4,1,9,0,0,5,
		0,0,0,0,8,0,0,7,9]

solve = [1,2,3,4,5,6,7,8,9] # List of Solutions (not important)

def BoardReset(): # Reset Board in Shell
	board =[5,3,0,0,7,0,0,0,0,
		 	6,0,0,1,9,5,0,0,0,
			0,9,8,0,0,0,0,6,0,
			8,0,0,0,6,0,0,0,3,
			4,0,0,8,0,3,0,0,1,
			7,0,0,0,2,0,0,0,6,
			0,6,0,0,0,0,2,8,0,
			0,0,0,4,1,9,0,0,5,
			0,0,0,0,8,0,0,7,9]
	return board


def ThreeXThreeCheck(y): #Getting Indeces for 3x3 parts
	x=int(y/9)
	if (x == 0 or x == 3 or x == 6):
		if y%3 == 0:
			sub = [y,y+1,y+2,y+9,y+10,y+11,y+18,y+19,y+20]
		elif y%3 == 1:
			sub = [y-1,y,y+1,y+8,y+9,y+10,y+17,y+18,y+19]
		elif y%3 == 2:
			sub = [y-2,y-1,y,y+7,y+8,y+9,y+16,y+17,y+18]
	elif (x == 1 or x == 4 or x == 7):
		if y%3 == 0:
			sub = [y,y+1,y+2,y+9,y+10,y+11,y-9,y-8,y-7]
		elif y%3 == 1:
			sub = [y-1,y,y+1,y+8,y+9,y+10,y-10,y-9,y-8]
		elif y%3 == 2:
			sub = [y-2,y-1,y,y+7,y+8,y+9,y-11,y-10,y-9]
	elif (x == 2 or x == 5 or x == 8):
		if y%3 == 0:
			sub = [y,y+1,y+2,y-9,y-8,y-7,y-18,y-17,y-16]
		elif y%3 == 1:
			sub = [y-1,y,y+1,y-10,y-9,y-8,y-19,y-18,y-17]
		elif y%3 == 2:
			sub = [y-2,y-1,y,y-11,y-10,y-9,y-20,y-19,y-18]
	return sub

def Check3x3(y): #Checking Indeces for 3x3 parts (Not Important)
	x=int(y/9)
	if (x == 0 or x == 3 or x == 6):
		if y%3 == 0:
			sub = [y,y+1,y+2,y+9,y+10,y+11,y+18,y+19,y+20]
			print("1")
		elif y%3 == 1:
			sub = [y-1,y,y+1,y+8,y+9,y+10,y+17,y+18,y+19]
			print("2")
		elif y%3 == 2:
			sub = [y-2,y-1,y,y+7,y+8,y+9,y+16,y+17,y+18]
			print("3")
	elif (x == 1 or x == 4 or x == 7):
		if y%3 == 0:
			sub = [y,y+1,y+2,y+9,y+10,y+11,y-9,y-8,y-7]
			print("4")
		elif y%3 == 1:
			sub = [y-1,y,y+1,y+8,y+9,y+10,y-10,y-9,y-8]
			print("yuh")
		elif y%3 == 2:
			sub = [y-2,y-1,y,y+7,y+8,y+9,y-11,y-10,y-9]
			print("6")
	elif (x == 2 or x == 5 or x == 8):
		if y%3 == 0:
			sub = [y,y+1,y+2,y-9,y-8,y-7,y-18,y-17,y-16]
			print("7")
		elif y%3 == 1:
			sub = [y-1,y,y+1,y-10,y-9,y-8,y-19,y-18,y-17]
			print("8")
		elif y%3 == 2:
			sub = [y-2,y-1,y,y-11,y-10,y-9,y-20,y-19,y-18]
			print("9")

	return sub

def ThreeXThree(ind,num): #Getting Numbers of 3x3 parts
	new = []
	for i in range(9):
		new.append(num[ind[i]])
	return new

def Row(y,num): #Getting Row Numbers
	x=int(y/9)
	row = num[9*x:9*x+9]
	return row

def Column(y,num): #Getting Column Numbers
	x=y%9
	column = num[x:80:9]
	return column

def PrintBoardOriginal(): #Printing Board in order without Text Design (not important)
	n=1
	x=1
	for i in range(0,9):
		print(board[n-1:9*x])
		n=9+n
		x=1+x

def PrintBoard(board): #Printing Board with Text Design
	n=0
	for j in range(3):
		print("---------------------")
		for i in range(3):
			print(board[0+n],board[1+n],board[2+n],"|",board[3+n],board[4+n],board[5+n],"|",board[6+n],board[7+n],board[8+n],sep=" ")
			n = n+9
	print("---------------------")

def Solving(board): #Solving Board
	solve = [1,2,3,4,5,6,7,8,9]
	print(" ")
	print("    Suduko Solver")
	print(" ")
	PrintBoard(board)
	print(" ")
	print(" ")
	print(" ")
	counter = -1
	blanks = []
	used = []
	original = []
	n = 0
	while 0 in board:
		y = board.index(0)
		for i in range(9):
			if ((solve[i] not in Row(y,board)) and (solve[i] not in Column(y,board)) and (solve[i] not in ThreeXThree(ThreeXThreeCheck(y),board))):
				board[y] = solve[i]
				blanks.append(y)
				used.append(solve[i])
				original.append(solve[i])
				counter = counter + 1
				n=n+1
				break
		if (board[y] == 0): #Backtracking Part
			while True:
				y = blanks[counter]
				z = used[counter]
				for i in range(z,9):
					if ((solve[i] not in Row(y,board)) and (solve[i] not in Column(y,board)) and (solve[i] not in ThreeXThree(ThreeXThreeCheck(y),board)) and (solve[i] != used[counter])):
						board[y] = solve[i]
						used[counter] = board[y]
						break
				if (original[counter] == board[y]):
					counter = counter - 1
					blanks.pop()
					used.pop()
					original.pop()
					board[y] = 0
				else:
					original[counter] = used[counter]
					break
	PrintBoard(board)

def Initialize(c): # MAIN FUNCTION
	board = []
	#c = input("Press 1 to use Testing Board or 2 to input another: ")
	if c == 2:
		board = []
		for i in range(81):
			num = int(input())
			board.append(num)
	elif c == 1:
		board = [5,3,0,0,7,0,0,0,0,
				 	6,0,0,1,9,5,0,0,0,
					0,9,8,0,0,0,0,6,0,
					8,0,0,0,6,0,0,0,3,
					4,0,0,8,0,3,0,0,1,
					7,0,0,0,2,0,0,0,6,
					0,6,0,0,0,0,2,8,0,
					0,0,0,4,1,9,0,0,5,
					0,0,0,0,8,0,0,7,9]
	return board

def Main():
	print("Welcome to Sudoko Solver")
	print("Press 1 to use test board or Press 2 to input own board")
	board = Initialize(int(input()))
	Solving(board)
Main()

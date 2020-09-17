import pygame
from SudokuSolver import Row, Column,ThreeXThreeCheck,ThreeXThree

pygame.init()

surface = pygame.display.set_mode((631,631))
background = pygame.image.load('Board.png').convert()
font = pygame.font.Font('freesansbold.ttf',32)
choices = font.render("Press 1 for test Board or 2 for own input", True, (255,255,255))
start = font.render("Press spacebar to solve", True, (255,255,255))
board = [0,0,0,0,0,0,0,0,0,
		 0,0,0,0,0,0,0,0,0,
		 0,0,0,0,0,0,0,0,0,
		 0,0,0,0,0,0,0,0,0,
		 0,0,0,0,0,0,0,0,0,
		 0,0,0,0,0,0,0,0,0,
		 0,0,0,0,0,0,0,0,0,
		 0,0,0,0,0,0,0,0,0,
		 0,0,0,0,0,0,0,0,0]
#board = Initialize(int(input()))

running = True

def PrintingBoard(board):
	n=0
	y=25
	for j in range(9):
		x=30
		for i in range(9*n,9*n+9):
			if board[i] != 0:
				numbers = font.render(str(board[i]), True, (255,255,255))
				surface.blit(numbers, (x,y))
			x += 70
		n += 1
		y += 70

def Searching(r):	
	y = 0
	q = int(r/9)
	for g in range(q+1):
		w=0
		if (r-9)>=0:
			t=8
		else:
			t=r
		for l in range(t+1):
			pygame.draw.rect(surface, (255,0,0),(9,9+y,63.5+w,63.5))
			w += 69
		r -= 9	
		y += 69

def NewSearching(index):
	x = index*67
	pygame.draw.rect(surface, (255,0,0),(9+x,9,63.1,63.5))


def BacktrackingGUI(r,e):
	q=int(r/9)
	p=int(e/9)
	sy=9+69*q
	h=q-p
	for i in range(h+1):
		sx=9+69*(r%9)+63.5
		q=int(r/9)
		p=int(e/9)
		w=0
		if r==e:
			z=1
		elif p == q:
			z = r - e
		else:
			z = r - 9*q+1
		for j in range(z):
			pygame.draw.rect(surface,(0,0,0),(sx,9+69*q,-63.5+w,63.5))
			w-=69
		r-=z

#def Update():


def GUISolver():
	solve = [1,2,3,4,5,6,7,8,9]
	counter = -1
	blanks = []
	used = []
	original = []
	n = 0
	temp = 0
	while 0 in board:
		for i in range(81):
			Searching(i)
			PrintingBoard(board)
			pygame.display.update()
			if board[i] == 0:
				y = i
				break

		for i in range(9):
			PrintingBoard(board)
			pygame.display.update()
			if ((solve[i] not in Row(y,board)) and (solve[i] not in Column(y,board)) and (solve[i] not in ThreeXThree(ThreeXThreeCheck(y),board))):
				board[y] = solve[i]
				blanks.append(y)
				used.append(solve[i])
				original.append(solve[i])
				counter = counter + 1
				n=n+1
				PrintingBoard(board)
				pygame.display.update()
				break
		if (board[y] == 0): #Backtracking Part
			while True:
				g = blanks[counter]
				BacktrackingGUI(y,g)
				PrintingBoard(board)
				pygame.display.update()
				y = blanks[counter]
				z = used[counter]
				for i in range(z,9):
					if ((solve[i] not in Row(y,board)) and (solve[i] not in Column(y,board)) and (solve[i] not in ThreeXThree(ThreeXThreeCheck(y),board)) and (solve[i] != used[counter])):
						board[y] = solve[i]
						used[counter] = board[y]
						break
						PrintingBoard(board)
						pygame.display.update()
				if (original[counter] == board[y]):
					counter = counter - 1
					blanks.pop()
					used.pop()
					original.pop()
					board[y] = 0
				else:
					original[counter] = used[counter]
					break
		pygame.display.update()
		PrintingBoard(board)
	PrintingBoard(board)
clock = pygame.time.Clock()


def InitializeGUI():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_1:
				board = [5,3,0,0,7,0,0,0,0,
					 	6,0,0,1,9,5,0,0,0,
						0,9,8,0,0,0,0,6,0,
						8,0,0,0,6,0,0,0,3,
						4,0,0,8,0,3,0,0,1,
						7,0,0,0,2,0,0,0,6,
						0,6,0,0,0,0,2,8,0,
						0,0,0,4,1,9,0,0,5,
						0,0,0,0,8,0,0,7,9]
			if event.key == pygame.K_2:
				for i in range(81):
					for event in pygame.event.get():
						if event.type == pygame.KEYDOWN:
							print("nigga)")
							
surface.blit(choices,(0,316))
while running:
	clock.tick(120)
	pygame.display.update()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_1:
				board = [5,3,0,0,7,0,0,0,0,
					 	6,0,0,1,9,5,0,0,0,
						0,9,8,0,0,0,0,6,0,
						8,0,0,0,6,0,0,0,3,
						4,0,0,8,0,3,0,0,1,
						7,0,0,0,2,0,0,0,6,
						0,6,0,0,0,0,2,8,0,
						0,0,0,4,1,9,0,0,5,
						0,0,0,0,8,0,0,7,9]
				surface.blit(background,(0,0))
				PrintingBoard(board)
				pygame.display.update()
			if event.key == pygame.K_2:
				pygame.draw.rect(surface,(0,0,0),(0,0,631,631))
				surface.blit(background,(0,0))
				n=0
				while n!=81:
					pygame.draw.rect(surface,(0,0,0),(0,0,631,631))
					surface.blit(background,(0,0))
					PrintingBoard(board)
					pygame.display.update()
					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							n=81
						if event.type == pygame.KEYDOWN:
							board[n] = int(event.unicode)
							n+=1
			if event.key == pygame.K_SPACE:
				GUISolver()
				surface.blit(background,(0,0))
				PrintingBoard(board)
				pygame.display.update()


				


	#print(event)




	#PrintingBoard(board)
	#GUISolver()
	#Searching(36)
	#NewSearching(0)
	#NewSearching(1)
	#pygame.draw.rect(surface, (0,0,255),(561,9+138,63.5,63.5))
	#BacktrackingGUI(81,17)
	#pygame.draw.rect(surface,(0,255,0),(260,260,-63.5,63.5))
	#pygame.display.update()
	#surface.blit(background,(0,0))
	#PrintingBoard(board)
	#PrintingBoard(board)
	pygame.display.update()

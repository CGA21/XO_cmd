board = ["1","2","3",
		 "4","5","6",
		 "7","8","9"]

def play_game():
	winner="continue"
	current_player=choice()
	display_board()
	while(winner=="continue"):
		ask_input(current_player)
		display_board()
		winner=check_winner(current_player)
		if(winner!="continue"):
			break
		current_player=flip_player(current_player)
	if(winner=="win"):
		print("		"+current_player + " won!!")
	else:
		print("it's a tie!!")
	return

def choice():
	current_player=input("choose X or O to start with: ")
	if(current_player=='X' or current_player=='O'):
		print("you chose "+current_player+"!!\n let's start the game")
	else:
		choice()
	return current_player

def display_board():
	print("		"+board[0]+"|"+board[1]+"|"+board[2])
	print("		"+board[3]+"|"+board[4]+"|"+board[5])
	print("		"+board[6]+"|"+board[7]+"|"+board[8])
	return

def ask_input(current_player):
	print("		"+current_player+"\'s turn!")
	ask=input("select a place to enter your value(1-9): ")
	ask=int(ask)-1
	if(ask>=0 and ask<=8 and board[ask]!="X" and board[ask]!="O"):
		board[ask]=current_player
	else:
		print("illegal entry \n try again!!")
		ask_input(current_player)
	return

def flip_player(current_player):
	if(current_player=='X'):
		current_player="O"
	else:
		current_player="X"
	return current_player;

def check_winner(current_player):
	if(check_rows(current_player) or check_column(current_player) or check_diagonal(current_player)):
		return "win"
	elif((board[0]=="X" or board[0]=="O") and
		 (board[1]=="X" or board[1]=="O") and
		 (board[2]=="X" or board[2]=="O") and
		 (board[3]=="X" or board[3]=="O") and
		 (board[4]=="X" or board[4]=="O") and
		 (board[5]=="X" or board[5]=="O") and
		 (board[6]=="X" or board[6]=="O") and
		 (board[7]=="X" or board[7]=="O") and
		 (board[8]=="X" or board[8]=="O")):
		return "tie"
	else:
		return "continue"

def check_rows(current_player):
	if(board[0]==current_player and board[1]==current_player and board[2]==current_player):
		return 1
	elif(board[3]==current_player and board[4]==current_player and board[5]==current_player):
		return 1
	elif(board[6]==current_player and board[7]==current_player and board[8]==current_player):
		return true
	else:
		return 0

def check_column(current_player):
	if(board[0]==current_player and board[3]==current_player and board[6]==current_player):
		return 1
	elif(board[1]==current_player and board[4]==current_player and board[7]==current_player):
		return true
	elif(board[2]==current_player and board[5]==current_player and board[8]==current_player):
		return 1
	else:
		return 0

def check_diagonal(current_player):
	if(board[0]==current_player and board[4]==current_player and board[8]==current_player):
		return 1
	elif(board[2]==current_player and board[4]==current_player and board[6]==current_player):
		return 1
	else:
		return 0

play_game()
print("Rock...")
print("Paper...")
print("Scissors...")

player1 = input("Player 1, make your move: ")
player2 = input("Player 2, make your move: ")

if player1 == "Rock" and player2 == "Scissors": 
	print("Player 1 wins!")
elif player1 == "Rock" and player2 == "Paper":
	print("Player 2 wins!")	
elif player1 == "Paper" and player2 == "Rock": 
	print("Player 1 wins!")
elif player1 == "Paper" and	player2 == "Scissors":
	print("Player 2 wins!")
elif player1 == "Scissors" and player2 == "Rock":
	print("Player 2 wins!")
elif player1 == "Scissors" and player2 == "Paper":
	print("Player 1 wins!")
elif player1 == player2: 
	print("It's a tie!")
else: 
	print("Oops, not a valid input")	
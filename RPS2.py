#A Shorter solution to Rock, Paper, Scissors Game. Lumped Else statments 
p1 = input("Player 1: rock, paper, or scissors ")
p2 = input("Player 2: rock, paper, or scissors ")
     
if p1 == p2:
    print("Draw")
elif p1 == "rock" and p2 == "scissors":
    print("p1 wins")
elif p1 == "paper" and p2 == "rock":
    print("p1 wins")
elif p1 == "scissors" and p2 == "paper":
    print("p1 wins")
else:
    print("p2 wins")

#Rather than typing every scenario, we can list out all the scenarios where p1 wins and add a else statement to cover all the instances where p2 would win

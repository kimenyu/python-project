import random

mychoices = ['rock', 'paper', 'scissors']
user_wins = 0
computer_wins = 0

for i in range(3):
    computer = random.choice(mychoices)
    userinput = input('Enter your input: ')
    
    #Case when rock is input
    def rockinput():
        if userinput == 'rock' and computer == 'rock':
            return (f'You pick {userinput} and computer picks {computer},  You drew')
        elif userinput == 'rock' and computer == 'paper':
            return (f"You pick {userinput} and computer picks {computer}, Computer wins")
        elif userinput == 'rock' and computer == 'scissors':
            return (f"You pick {userinput} and computer picks {computer}, You win")
    
    #Case when scissors is input
    def scissorsinput():
        if userinput == 'scissors' and computer == 'rock':
            return (f"You pick {userinput} and computer picks {computer}, Computer wins")
        elif userinput == 'scissors' and computer == 'scissors':
            return (f"You pick {userinput} and computer picks {computer} , You draw")
        elif userinput == 'scissors' and computer == 'paper':
            return (f"You pick {userinput} and computer picks {computer}, You win")
    
    #Case when input is paper is input
    def paperinput():
        if userinput == 'paper' and computer == 'paper':
            return (f"You pick {userinput} and computer picks {computer}, You draw")
        elif userinput == 'paper' and computer == 'rock':
            return (f"You pick {userinput} and computer picks {computer}, You win")
        elif userinput == 'paper' and computer == 'scissors':
            return (f"You pick {userinput} and computer picks {computer}, Computer wins")
    
    result1 = rockinput()
    if result1 is not None:
        print(result1)
        if 'You win' in result1:
            user_wins += 1
        elif 'Computer wins' in result1:
            computer_wins += 1
    
    result2 = scissorsinput()
    if result2 is not None:
        print(result2)
        if 'You win' in result2:
            user_wins += 1
        elif 'Computer wins' in result2:
            computer_wins += 1
    
    result3 = paperinput()
    if result3 is not None:
        print(result3)
        if 'You win' in result3:
            user_wins += 1
        elif 'Computer wins' in result3:
            computer_wins += 1

if user_wins > computer_wins:
    print("Congratulations! You won the game.")
elif computer_wins > user_wins:
    print("Sorry, the computer won the game.")
else:
    print("The game ended in a tie.")

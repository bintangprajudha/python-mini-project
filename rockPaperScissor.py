import random

def play():
    print("Lets play! What's your choise?")
    user = input("(r) for rock, (p) for paper, (s) for scissor: ")
    computer = random.choice(['r', 'p', 's'])

    print(f'You choice {user}')
    print(f'Computer choice {computer}')

    if user == computer:
        return "It\'s a tie"
    
    if is_win(user, computer):
        return 'You won!'
    
    return 'You lost!'

def is_win(player, opponent):
    if ((player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r')): 
        return True
    
print(play())
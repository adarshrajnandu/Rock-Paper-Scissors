import random
import colorama
from colorama import Fore,Style

opt = ['rock', 'paper', 'scissors']

print('How many times you want to play?')
times = int(input())

n = []  # to count the player wins
m = []  # to count the computer wins

for _ in range(times):
    i = random.randint(0,2)
    comp = opt[i]
    
    print('Enter your choice: (rock,paper,scissors)')
    user = input().lower()
    
    if user == comp:
        print(Fore.BLUE + " That's a tie")
        n.append(0)
        m.append(0)
    elif user == 'rock':
        if comp =='scissors':
            print(Fore.GREEN + ' Congrats ', user,' smashed ', comp)
            n.append(1)
        else:
            print(Fore.RED + ' Sorry ', comp, ' covered ', user)
            m.append(1)
    elif user == 'paper':
        if comp == 'rock':
            print(Fore.GREEN + ' Congrats ', user,' covered ', comp)
            n.append(1)
        else:
            print(Fore.RED + ' Sorry ', comp, ' cuts ', user)
            m.append(1)
    elif user == 'scissors':
        if comp == 'paper':
            print(Fore.GREEN + ' Congrats ', user, ' cuts ', comp)
            n.append(1)
        else:
            print(Fore.RED + ' Sorry ', comp, ' covered ', user)
            m.append(1)
    else:
        print(" You've not entered a valid choice!, please enter either rock, paper or scissors")


user_wins = sum(n)        
comp_wins = sum(m)
print(Fore.GREEN + 'You have won ', user_wins, 'times')
print(Fore.RED + 'Computer has won', comp_wins , 'times')
if comp_wins == user_wins:
    print(Fore.BLUE + "That's a tie")
elif comp_wins > user_wins:
    print(Fore.RED + 'Sorry computer has won this time')
else:
    print(Fore.GREEN + 'Congrats, you have won the game !!!')

print(Style.RESET_ALL)

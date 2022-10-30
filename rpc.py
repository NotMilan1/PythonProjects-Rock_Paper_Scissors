#Made by Milan#4574 on discord.
import random
choices = ['Rock', 'Paper', 'Scissors']

pWins = 0   #Amount of player Wins
aiWins = 0  #Amount of AI Wins

c = None    #Player Choice
aiC = None  #AI Choice

def Choose():
    global pWins; global aiWins; global c; global aiC; global canPlay
    #print(str(c) + " " + str(aiC) + "\n")
    if c == 'Rock' and aiC == 'Paper':
        aiWins += 1
        print(c + " > " + aiC)
        canPlay = False
    elif c == 'Rock' and aiC == 'Scissors':
        pWins += 1
        print(c + " < " + aiC)
        canPlay = False
    if c == 'Paper' and aiC == 'Rock':
        pWins += 1
        print(c + " < " + aiC)
        canPlay = False
    elif c == 'Paper' and aiC == 'Scissors':
        aiWins += 1
        print(c + " > " + aiC)
        canPlay = False
    if c == 'Scissors' and aiC == 'Rock':
        aiWins += 1
        print(c + " > " + aiC)
        canPlay = False
    elif c == 'Scissors' and aiC == 'Paper':
        pWins += 1
        print(c + " < " + aiC)
        canPlay = False

def pChoose():
    global c
    print('\nOptions:\n1: Rock\n2: Paper\n3: Scissors\n')
    c = choices[(int(input('Choose your option: '))-1)]
    AIChoose()

def AIChoose():
    global aiC; global c
    aiC = choices[random.choice(range(0, 2))]
    if c == aiC:
        return AIChoose()
    print('\nAIs Choice: ' + aiC)
    Choose()

canPlay = True
canGo = True
while True:
    if canPlay == False:
        print('\nPlayer Wins: ' + str(pWins) + "\nAI Wins: " + str(aiWins))
        ch = str.lower(input('Do you want to Play Again?\n\nYes or No?: '))
        if ch == "yes":
            canPlay = True
            canGo = True
        elif ch == "no":
            quit()
    if canGo:
        pChoose()
        canGo = False
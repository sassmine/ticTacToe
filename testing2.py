from random import *
from time import *
#Noughts and Crosses
#Only works in Python 3

def PrintBoard(Places): #Prints the Board, mirrors a laptop's keypad
    print('',Places[6],'|',Places[7],'|',Places[8],'')
    print('---|---|---')
    print('',Places[3],'|',Places[4],'|',Places[5],'')
    print('---|---|---')
    print('',Places[0],'|',Places[1],'|',Places[2],'')
    print()#empty line at the bottom to make room for further prompts

from random import *
from time import *
#Noughts and Crosses
#Only works in Python 3

def PrintBoard(Places): #Prints the Board, mirrors a laptop's keypad
    print('',Places[6],'|',Places[7],'|',Places[8],'')
    print('---|---|---')
    print('',Places[3],'|',Places[4],'|',Places[5],'')
    print('---|---|---')
    print('',Places[0],'|',Places[1],'|',Places[2],'')
    print()#empty line at the bottom to make room for further prompts


def VerifyPosition(Places, Type):#Verifys and asks for your selection
    Valid = False
    print(Type+"'s Go...")#O's Go... / X's Go...
    while not Valid:
        Position = input("Please type where you wish to place: ")
        while Position.isdigit() == False or int(Position) > 9 or int(Position) <= 0:#Ensures the player does not type an incorrect location to place in
            Position = input("Please type a valid integer between 1 and 9: ")
        Position = int(Position)
        if Places[Position-1] == 'X' or Places[Position-1] == 'O':#9 on the keypad would refer to index 8, as starts from 0 but keypad starts at 1
            Valid = False
            print("That is an invalid square, please try again ")
        else:
            Valid = True
    Places[Position-1] = Type#lists start at 0, inputs start at 1
    #the board is layed out identical to a Computer's Key-Pad, hence starting at 1 and not 0, requiring -1 to the positional index


def PlayRoundSingle(Places, Type, GameType):
    GameWon = False
    while not GameWon:#loops until someone wins
        if GameType in ["S","M"]:
            Move(Places, Type)
            GameWon,WinningType = CheckWin(Places, Type)
            Type = ChangeType(Type)
        if GameType != "M" and GameWon == False:# If Single Player and the Game has not been Won...
            print(Type+"'s Go...")#Computers Go!
            sleep(1)
            Places = GetComputersChoice(Places, Type)
            GameWon,WinningType = CheckWin(Places, Type)
            Type = ChangeType(Type)
    return WinningType, GameWon

def GetComputersChoice(Places, Type):
    EmptySpaces = []
    for i in range(0,9):#goes through all spaces on the board...
        if Places[i] == ' ': #Finds empty spaces...
            EmptySpaces.append(i) # Adds them to a list for future reference
    Places = ComputerMove(Places, EmptySpaces, Type)
    PrintBoard(Places) # Prints the Board
    return Places

def ComputerMove(Places,EmptySpaces, Type):
    Change = False
    OriginalType = Type # prevents placing down the opponent's piece when checking for a BLOCK
    for i in range(0,2):#Checks each space twice, FIRST to see if there is a winning move, THEN to check if they can block the opponent
        for i in range(0,len(EmptySpaces)):#check the space to see FIRST if two friendly pieces are in line for a win, THEN check if you can block an opponent, IF NEITHER, radomise
            if not Change: # If no change has happened (prevents re-checking after a space has been found
                Position, Change = CheckComputerWin(Places, EmptySpaces[i], Type) # checks to see whether the computer can cause a three-in-a-row... or prevent one
            if Change:    # If there is a change...
                Places[Position] = OriginalType # Fills in the space
                return Places # prevents unneccesarily checking more spaces
        Type = ChangeType(Type) #switches the type, to see if any draws are available AFTER checking for wins
    Places[choice(EmptySpaces)] = OriginalType # If no places were found to have a effect, randomize the location...
    return Places

def CheckComputerWin(Places, SpaceToCheck, Type):
    if (SpaceToCheck in [6,3,0] and Places[SpaceToCheck + 1] == Type and Places[SpaceToCheck + 2] == Type) or (#Left Side Checks     |
        SpaceToCheck in [7,4,1] and Places[SpaceToCheck + 1] == Type and Places[SpaceToCheck - 1] == Type) or (#Central Column check | Horizontal Checks
        SpaceToCheck in [8,5,2] and Places[SpaceToCheck - 1] == Type and Places[SpaceToCheck - 2] == Type) or (#Right Side Check     |
        SpaceToCheck in [6,7,8] and Places[SpaceToCheck - 3] == Type and Places[SpaceToCheck - 6] == Type) or (#Top Row Check     |
        SpaceToCheck in [5,4,3] and Places[SpaceToCheck - 3] == Type and Places[SpaceToCheck + 3] == Type) or (#Middle Row Check  | Vertical Checks
        SpaceToCheck in [2,1,0] and Places[SpaceToCheck + 3] == Type and Places[SpaceToCheck + 6] == Type) or (#Bottom Row Check  |
        SpaceToCheck == 0 and Places[SpaceToCheck + 4] == Type and Places[SpaceToCheck + 8] == Type) or ( #Bottom Left  |
        SpaceToCheck == 2 and Places[SpaceToCheck + 2] == Type and Places[SpaceToCheck + 4] == Type) or ( #Bottom Right | Diagonal
        SpaceToCheck == 6 and Places[SpaceToCheck - 2] == Type and Places[SpaceToCheck - 4] == Type) or ( #Top Left     | Checks
        SpaceToCheck == 8 and Places[SpaceToCheck - 4] == Type and Places[SpaceToCheck - 8] == Type) or ( #Top Right    |
        SpaceToCheck == 4 and ((Places[SpaceToCheck + 2] == Type and Places[SpaceToCheck - 2] == Type) or ( # Centre Piece, | Top-Left to Bottom-Right  | Diagonal
            Places[SpaceToCheck + 4] == Type and Places[SpaceToCheck - 4] == Type))):                       # Centre Piece, | Top-Right to Bottom-Left  | Checks
        return SpaceToCheck, True # Yes, The position Places[SpaceToCheck] would not win or block an opponent
    return 0, False    # No, The position Places[SpaceToCheck] would not win or block an opponent



def ChangeType(Type):#Switches the players turns after their go
    if Type == 'X':
        Type = 'O'
    else:
        Type = 'X'
    return Type


def Move(Places, Type):
    VerifyPosition(Places, Type)#asks for your square,verifies, then moves
    PrintBoard(Places)#shows the board


def CheckWin(Places,Type):
    GameWon = False
    if ((Places[0]== Type) and (Places[1] == Type) and (Places[2] == Type)) or (
        (Places[3]== Type) and (Places[4] == Type) and (Places[5] == Type)) or (
        (Places[6]== Type) and (Places[7] == Type) and (Places[8] == Type)) or (
        #Row Check^^^^^^^
        (Places[0]== Type) and (Places[3] == Type) and (Places[6] == Type)) or (
        (Places[1]== Type) and (Places[4] == Type) and (Places[7] == Type)) or (
        (Places[2]== Type) and (Places[5] == Type) and (Places[8] == Type)) or (
        #Column Check^^^^
        (Places[0]== Type) and (Places[4] == Type) and (Places[8] == Type)) or (
        (Places[2]== Type) and (Places[4] == Type) and (Places[6] == Type)):
        #Diagonal Check^^
      #  Type = 'X'
        GameWon = True
    if GameWon != True:#if no one wins (potentially on the last go...)
        DrawCheck = 0
        for i in range(0,9):#checks the number of spaces left in the board out of 9 squares, 0-8
            if Places[i] == ' ':
                DrawCheck = DrawCheck + 1
        if DrawCheck == 0:#if there are no squares...
            GameWon = 'Draw'

    return GameWon, Type#returns True, False or 'Draw' and Type (who won, NONE if else)


def Start():
        GameType = "Computer v Computer"
    if GameType in ["S","M"]:
        Places = ['1','2','3',#for the initial board - to show the player which key relates to which position
                  '4','5','6',
                  '7','8','9']#flipped as Key-Pads are flipped
        print("This is how the Board is layed Out (Key-Pad use recommended)")
        PrintBoard(Places)
    Places = [' ',' ',' ',
              ' ',' ',' ',
              ' ',' ',' ']
    if GameType not in["S","M"]:
        PrintBoard(Places)
        sleep(1)
    Type = choice(['X','O'])#more effective than randint
    WinningType, GameWon = PlayRoundSingle(Places, Type, GameType)
#waiting for game to end...
    if GameWon == True:#if you win...
        print(WinningType, "Wins!")
    else:#if you draw... (will not get to this stage is GameWon is False, as will stay in the loop
        print("Draw!")



#starts here...
PlayAgain = 'yes'
while PlayAgain in ["Yes","yes","y","Y"]:
    Start()
    PlayAgain = input("Do You want to play again? Y/es or N/o: ")
    print()

#quit()
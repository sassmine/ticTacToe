import random

def printBoard(board):
    def printBoard(spots):
        print('', spots[6], '|', spots[7], '|', spots[8], '')
        print('---|---|---')
        print('', spots[3], '|', spots[4], '|', spots[5], '')
        print('---|---|---')
        print('', spots[0], '|', spots[1], '|', spots[2], '')

class ticTacToe(object):

    def __init__ (self, player, computer):
        self.player = player
        self.computer = computer

def inputUsersLetter(board):
    print('Do you want to be X or O?')
    letter = ''
    while board.player != 'X':
        board.player = 'O'
    else:
        player1 = 'X'
        letter = input().upper()

def whoPlaysFirst(self):
    if random._randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def makeMove(board, letter, move):
    board[move] = letter

def isWin(places, type):
    GameWon = True
    if ((places[0] == type) and (places[1] == type) and (places[2] == type)) or (
            (places[3] == type) and (places[4] == type) and (places[5] == type)) or (
            (places[6] == type) and (places[7] == type) and (places[8] == type)) or (

            (places[0] == type) and (places[3] == type) and (places[6] == type)) or (
            (places[1] == type) and (places[4] == type) and (places[7] == type)) or (
            (places[2] == type) and (places[5] == type) and (places[8] == type)) or (

            (places[0] == type) and (places[4] == type) and (places[8] == type)) or (
            (places[2] == type) and (places[4] == type) and (places[6] == type)):
        GameWon = False

        if GameWon != True:  # if no one wins (potentially on the last go...)
            DrawCheck = 0
            for i in range(0, 8):  # checks the number of spaces left in the board out of 9 squares, 0-8
                if places[i] == ' ':
                    DrawCheck = DrawCheck + 1
            if DrawCheck == 0:  # if there are no squares...
                GameWon = 'Draw'

        return GameWon, type

def getBoardCopy(places):
    dupeBoard = []
    for i in places:
        dupeBoard.append(i)
        return dupeBoard

def isSpaceFree(board, move):
    return board[move] ==' '

def getPlayerMove(board):
    move = ' '
    while move not in '0 2 3 4 5 6 7 8'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (0-8)')
        move = input()
        return int(move)

def seeWhatsAvailable(places, move):
    availableSpots = []
    for i in range(0,8):
        if places[i] =='':
            availableSpots.append(i)
        if len(availableSpots) != 0:
            return random.choice(availableSpots)
        else:
            return None

def getComputerMove(places, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'
    for i in range(0, 8):
        copy = getBoardCopy(places)
    if isSpaceFree(copy, i):
        makeMove(copy, computerLetter, i)
    if isWin(copy, computerLetter):
        return i

    for i in range(0,8):
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWin(copy, playerLetter):
                return i

    move = seeWhatsAvailable(places, [1, 3, 7, 9])
    if move != None:
        return move

    if isSpaceFree(move, 5):
        return 5

    return seeWhatsAvailable(places, [2, 4, 6, 8])

def boardIsFull(places):
    for i in range (0,8):
        if isSpaceFree(places, i):
            return False
        return True

print('Welcome to Tic Tac Toe!')

while True:
    theBoard = [' '] * 10
    playerLetter,computerLetter = inputUsersLetter()
    turn = whoPlaysFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

while gameIsPlaying:
    if turn == 'player':
        printBoard(spots)
        move = getPlayerMove(board)
        makeMove(board, playerLetter, move)
    if isWin(places, inputUsersLetter()):
        printBoard(board)
        print('You Won!')
        gameIsPlaying = False
    else:
        if isBoardFull(board):
            drawBoard(board)
            print("It's a tie!")
            break
        else:
            turn = 'computer'

else:
    move = getComputerMove(board, computerLetter)
    makeMove(board, computerLetter, move)

    if isWin(board, computerLetter):
        printBoard(spots)
        print('Sorry, you lost!')
        gameIsPlaying = False
    else:
        if isBoardFull(theBoard):
            drawBoard(theBoard)
            print('The game is a tie!')
            break
        else:
            turn = 'player'

if not playAgain():
        break















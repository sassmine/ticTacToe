from random import *
import itertools

def PrintBoard(spots):
    print('', spots[6], '|', spots[7], '|', spots[8], '')
    print('---|---|---')
    print('', spots[3], '|', spots[4], '|', spots[5], '')
    print('---|---|---')
    print('', spots[0], '|', spots[1], '|', spots[2], '')

board = [0, 1, 2, 3, 4, 5, 6, 7, 8]


class ticTacToe(object):

    def __init__ (self, player1, computer):
        self.player1 = player1
        self.computer = computer

    def whoGoesFirst(self):

        if random.randint(0, 1) == 0:

            return 'computer'

        else:

            return 'player1'


    def CheckWin(Places, Type):
        GameWon = False
        if ((Places[0] == Type) and (Places[1] == Type) and (Places[2] == Type)) or (
                (Places[3] == Type) and (Places[4] == Type) and (Places[5] == Type)) or (
                (Places[6] == Type) and (Places[7] == Type) and (Places[8] == Type)) or (

                (Places[0] == Type) and (Places[3] == Type) and (Places[6] == Type)) or (
                (Places[1] == Type) and (Places[4] == Type) and (Places[7] == Type)) or (
                (Places[2] == Type) and (Places[5] == Type) and (Places[8] == Type)) or (

                (Places[0] == Type) and (Places[4] == Type) and (Places[8] == Type)) or (
                (Places[2] == Type) and (Places[4] == Type) and (Places[6] == Type)):

            GameWon = True
        if GameWon != True:  # if no one wins (potentially on the last go...)
            DrawCheck = 0
            for i in range(0, 9):  # checks the number of spaces left in the board out of 9 squares, 0-8
                if Places[i] == ' ':
                    DrawCheck = DrawCheck + 1
            if DrawCheck == 0:  # if there are no squares...
                GameWon = 'Draw'

        return GameWon, Type

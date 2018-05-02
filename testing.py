
board = [0, 1, 2,
         3, 4, 5,
         6, 7, 8]
def show():
    print('', spots[6], '|', spots[7], '|', spots[8], '')
    print('---|---|---')
    print('', spots[3], '|', spots[4], '|', spots[5], '')
    print('---|---|---')
    print('', spots[0], '|', spots[1], '|', spots[2], '')

    while True:
        input = input("Select a spot:")
        input=int(input)

        if board(input) != 'x' and board [input] != 'o':
            board[input] = 'x'
        else:
            print("spot is taken")
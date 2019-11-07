# CMPT 120 - Intro To Programming
# Lab 7 - Lists, Functions, and Error Handling
# Author: Enrique Pesantez
# Created: 10-24-2019

symbol = ['', 'x', 'o']

def printRow(row):
    sq = '|'
    for sqaure in row:
        sq = sq + symbol[sqaure] + '  |'
    print(sq)

def printBoard(board):
    print('+-------+') # print the top border
    for row in board: # for each row in the board...
        printRow(row) # print the row
        print('+--------+')# print the next border

def markBoard(board, row, col, player):
    #check to see whether the desired square is blank
    if board[row][col] == 0:
        #if so, set it to player number
        board[row][col] = player



def getPlayerMove(player):
    print("\nPlayer {0}:\n".format(str(player)))
    row = int(input("Enter row number: "))
    col = int(input("Enter column number:"))
    print()
    return row , col


def hasBlanks(board):
    # for each row in the board..
    for row in range(len(board)):
        # for each sqaure in the row...
        for col in range(len(board[row])):
            # Check whether the square is blank
            if board[row][col] == 0:
                # if so, return True
                return True
            else:
                return False

def main():
    board = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]] # TODO replace this with a three by three matrix of zeros
    player = 1
    while hasBlanks(board):
        printBoard(board)
        row, col = getPlayerMove(player)
        markBoard(board, row, col, player)
        player = player % 2 + 1 # switch player for next turn


main()

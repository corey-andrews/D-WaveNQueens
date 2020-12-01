from PIL import Image

SQUARE_DIM = 100
DARK_STRING  = "#7D8796"
LIGHT_STRING = "#E8EBEF"
DARK_TUPLE   = (125,135,150)
LIGHT_TUPLE  = (232,235,239)

# Flow control
def drawNQueensSolution(dimension, queens):
    board = drawBoard(dimension)
    board = placeQueens(board, dimension, queens)

    board.save("Solution.png")
    board.show()
    board.close()

# puts all the queens onto the board on the appropriate
# squares
def placeQueens(board, dimension, queens):
    queenImg = Image.open("Queen.png")
    # for each queen, calculate it's row and column then 
    # draw it
    for queen in queens:
        row = (queen-1)//dimension
        col = (queen-1) %dimension
        board = drawQueen(board, queenImg, row, col)
    queenImg.close()
    return board

# Draws the empty board
def drawBoard(dimension):
    boardDimension = dimension * SQUARE_DIM
    # Create our image and precolor it dark
    board = Image.new(
        "RGB",
        (boardDimension,boardDimension),
        DARK_STRING
    )

    # Rows can be paired off into one that starts with light
    # colored squares then one that starts with dark unless
    # a light colored square row ends the board (odd dimensions) 
    # Because we started with the board dark, we must add the
    # light squares
    for row in range(1, dimension + 1, 2):
        for col in range(1, dimension + 1, 2):
            board.paste(LIGHT_TUPLE, getSquare(row,   col))
        if(row+1 <= dimension):
            for col in range(2, dimension + 1, 2):
                board.paste(LIGHT_TUPLE, getSquare(row+1, col))
        
    return board

# Puts the queen image on the board on a given square
def drawQueen(board, queen, row, col):
    board.paste(
        queen, 
        (SQUARE_DIM*(col),SQUARE_DIM*(row))
    )
    return board

# gets a 4 dimensional tuple of the dimensions of a square
# on a chess board in terms of pixels
# We want to index from 0 here so we subtract 1 for top and
# left
def getSquare(row, col):
    return (
        SQUARE_DIM*(col-1), SQUARE_DIM*(row-1),
        SQUARE_DIM*( col ), SQUARE_DIM*( row )
    )


sudoku_board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7],
]

def solve(board):

    if not find_empty_cell(board):
        return True
    else:
        row, col = find_empty_cell(board)

    for i in range(1,10):
        if valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

        board[row][col] = 0

    return False


def valid(board, num, pos):

    # Check row
    for row in range(len(board[0])):
        if board[pos[0]][row] == num and pos[1] != row:
            return False
        
    # Check column
    for col in range(len(board[0])):
        if board[col][pos[1]] == num and pos[0] != col:
            return False
        
    # Check box
    grid_x = (pos[1] // 3) * 3
    grid_y = (pos[0] // 3) * 3

    for i in range(grid_y, grid_y + 3):
        for j in range(grid_x, grid_x + 3):
            if board[i][j] == num and (i, j) != pos:
                return False
            
    return True
    
 

def print_board(board):

    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) +" ", end="")

def find_empty_cell(board):
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
            
    return None

print_board(sudoku_board)

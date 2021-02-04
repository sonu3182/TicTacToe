


    def printBoard():
        # "board" is a list of 10 strings representing the board (ignore index 0)
        print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
        print('-----------')
        print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
        print('-----------')
        print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
 
    def main():
        #Main game loop
        print("Welcome to Tic Tac Toe, to win complete a straight line of your letter (Diagonal, Horizontal, Vertical). The board has positions 1-9 starting at the top left.")
        printBoard()
    

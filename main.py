''' 3by3 grid '''
global board
board = [[" "," "," "],[" "," "," "],[" "," "," "]] 
player="X"

''' prints the board  '''
def printBoard(board): 
      for line in board:
        print(line)
        
''' takes user input and replace blank space  ''' 
def user_input():
    global player
    x=int(input("Player " + player + ", What is the X coordinate?"))
    y=int(input("What is the Y coordinate?"))
    
    while board[y][x] != " ":
        print("You must choose an empty spot:")
        x=int(input("Player " + player + ", What is the X coordinate?"))
        y=int(input("What is the Y coordinate?"))
    
    if player=="X":
        board[y][x]= "X"
        ''' now switch players '''
        player="O" 
    else:
        board[y][x]= "O"
        player="X"
        
''' if a player wins '''
def ifwin():
  
   #row 
    for x in range(len(board)):
        win = True
    for y in range(len(board)):
        if board[x][y] != player:
            win = False 
            break 
    if win: 
       return  True 

    return False 

    
    
    
    
''' calls the input function '''     
def tictac():
    printBoard(board)
    user_input()

def main():
    gamewon = False
    while gamewon== False:
      printBoard(board)
      user_input()
      gamewon=ifwin()
    print("GAMEOVER!!")
    printBoard(board)
  
        
        
        
main() 

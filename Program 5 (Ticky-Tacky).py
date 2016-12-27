#Ticky-Tacky.py
#by Margaret He, Fall Quarter 2013, ECS 10


#Assign global constants
X = "X"
O = "O"
EMPTY = ""
TIE = "TIE"
NUM_SQUARES = 16
import random

def display_instruct():
    """Display game instructions."""  
    print (
    """
    Welcome to the greatest intellectual challenge of all time: Ticky-Tacky.  
    This will be a showdown between your human brain and my silicon processor.  

    Play goes as follows:

step 1:    Player X calls out a number from 1 to 18.
step 2:    Player O calls out a number from 1 to 18 that player O has not called out before.
step 3:    Player O adds that number to the last number called out by 
           X, and if that square is on the board and unmarked, that square is marked O.
step 4:    Player X calls out a number from 1 to 18 that player X has not called out before.
step 5:    Player X adds that number to the last number called out by 
           O, and if that square is on the board and unmarked, that square is marked X.
step 6:    Repeat from step 2. 

Play ends when either X or O has four in a row, or a column, or a diagonal, 
and is declared a winner; or when no more moves are possible by either player.

Here is an example:
12 |  5 | 7| 2
---------------
14 | 11 | 3| 8
---------------
4  | 13 | 9| 30 
---------------
24 | 16 |31| 21

X: calls out 1, O: calls out 3 (to make 4), X: 8 (11), O: 4 (12), X: 3 (7), O: 6 (9). At the point the board looks like:

 O |  5 | X | 2
----------------
14 |  X | O | 8
----------------
 O | 13 | O | 30
----------------
24 | 16 |31| 21 \n
   
Below is the board we will be playing on:""")

#Make the 4 x 4 Board
random_board = []
def Make_Board(random_board):
    while len(random_board) != 16: #Holds the numbers assigned to the squares
        number = random.randrange(2, 32)
        if number not in random_board: #Add the new numbers into random board
            random_board.append(number)

    for i in range(NUM_SQUARES):        
        print (random_board[i], end = "")

        if (i + 1 < NUM_SQUARES):
            if(((i+1) % 4 ) == 0):
               print("\n----------")
            else:
               print("|", end ="")
    print("\n")               
    return random_board

#Determine whether human or computer goes first.
def pieces():
    go_first = input("Do you require the first move? (y/n): ")
    response = go_first.lower()
    
    if response == "y":
        print("\nThen take the first move. You will need it.")
        human = X
        computer = O

    elif response == "n":
        print("\nYour bravery will be your undoing...I will go first.")
        computer = X
        human = O

    else:
        print("Your input is invalid")
    return computer, human

#Creates new game board
def new_board():
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board


#Check if human move is legal
humlegal = ""
def h_legal_move(human_move, random_board):
    humlegal = None
    if (human_move >= 1) and (human_move <= 18):
        a = True
    else:
        a = False
    if (human_move + computer_list[-1] in random_board):
        b = True
    else:
        b = False
    if (human_move not in human_list) and (human_move not in computer_list): #Check to make sure this move 
        c = True                                                                # has not been used yet
    else:
        c = False 
    if (a == b == c == True):
        humlegal = True
    else:
        humlegal = False
    return humlegal


#Check if computer move is legal
comlegal = ""
def c_legal_move(computer_move, random_board):
    comlegal = None
    if (computer_move + human_list[-1] in random_board):
        d = True
    else:
        d = False
    if (computer_move not in computer_list) and (computer_move not in human_list): #Check to make sure this move 
        e = True                                                                      # has not been used yet
    else:
        e = False
    if (d == e == True):
        comlegal = True
    else:
        comlegal = False
    return comlegal

       
#Swtich Turns
def next_turn(turn):
    if turn == X:
        return O
    else:
        return X

#Determine the game winner
def winner_board(board, humlegal, comlegal):
    row = 0
    for row in range(4):      #Check for Horizontal Winner
        if (board[row*4] == board[row*4 + 1] == board[row*4 + 2] == board[row*4 + 3] != EMPTY):
            winner = board[row*4]
            return winner
    column = 0   
    for column in range(4):   #Check for Vertical Winner
        if (board[column] == board[column + 4] == board[column + 8] == board[column + 12] != EMPTY):
            winner = board[column]
            return winner
    diag_1 = 0
    for diag_1 in range(1): #Check for Diagonal Winner \ 
        if (board[diag_1] == board[diag_1+5] == board[diag_1 + 10] == board[diag_1 + 15] != EMPTY):
            winner = board[diag_1]
            return winner
    diag_2 = 3
    for diag_2 in range(1): #Check for Diagonal Winner /
        if (board[diag_2] == board[diag_2 + 3] == board[diag_2 + 6] == board[diag_2 + 9] != EMPTY):
            winner = board[diag_2]
            return winner

    if EMPTY not in board:       #If there are no empty spots left, game ends with a TIE
        the_winner = TIE 
        return the_winner
    if humlegal == comlegal == False:  #If both human and computer can no longer place legal move
        the_winner = TIE
        return the_winner

#Main Program
display_instruct()
Make_Board(random_board)
print("Prepare yourself, human. The ultimate battle is about to begin. \n")
computer, human = pieces()
turn = X
board = new_board()

#Keep track of the numbers human and computer call out
human_list = []
computer_list = []

#Human's first turn
if (turn == human):
    human_move = eval(input("Please input a new number between 1 to 18 (inclusive): "))
    if (human_move >= 1) and (human_move <= 18):
        print("Human: I choose number", human_move)
        human_list.append(human_move)
    else:
        print("Foolish human, you picked an invalid number")

#Computer's first turn
import random         
if (turn == computer):
    comp_move = random.randrange(1, 19)
    print("Computer: I choose number", comp_move)
    computer_list.append(comp_move)
turn = next_turn(turn)
        
#Human's consecutive turns
while not winner_board(board, humlegal, comlegal):
    if (turn == human):
        human_move = eval(input("Please input a new number between 1 to 18 (inclusive): "))
        humlegal = h_legal_move(human_move, random_board)
            
        if (humlegal == True):
            board_move = human_move + computer_list[-1]
            print("Human: I choose number", human_move)
            print("My move", human_move, "+ your last move", computer_list[-1], "is", board_move)
            human_list.append(human_move)
            print("I will take space", board_move)
                
            for i in range(16):
                if random_board[i] == board_move:
                    position = i
            board[position] = human
            random_board[position] = human
            human_list.append(human_move)

        elif (humlegal == False):
            print("Computer: Oh foolish human, that's an illegal move. Thanks for giving me an extra turn!")
            turn = next_turn(turn)
                
                 
                    
#Display new board
        for i in range(NUM_SQUARES):
            print(random_board[i], end = " ")
            if (i + 1 < NUM_SQUARES):
                if ((i+1) % 4 == 0):
                    print("\n---------")
                else:
                    print("|", end="")
        print("\n")
        

#Computer's consecutive turns
    if turn == computer:
        import random
        computer_move =random.randrange(1, 19)
        comlegal = c_legal_move(computer_move, random_board)
            
#If computer chooses an illegal move continue to generate moves
#until it picks an accurate one (given 5 chances total)
        i = 0
        while (comlegal == False) and (i <= 20):
            computer_move = random.randrange(1, 19)
            comlegal = c_legal_move(computer_move, random_board)
            i += 1
            
        if (comlegal == True):
                board_move = computer_move + human_list[-1]
                print("Computer: I choose number", computer_move)
                computer_list.append(computer_move)
                print("My move", computer_move, "+ your last move", human_list[-1], "is", board_move)
                print("I will take space", board_move)

                for i in range(16):
                    if (random_board[i] == board_move):
                        position = i
                board[position] = computer
                random_board[position] = computer
                computer_list.append(computer_move)

        for i in range(NUM_SQUARES):
            print(random_board[i], end = " ")
            if (i + 1 < NUM_SQUARES):
                if ((i+1) % 4 == 0):
                    print("\n---------")
                else:
                    print("|", end="")
        print("\n")               
                         
    turn = next_turn(turn)
                
#Congratulate the winner!    
def congrat_winner(the_winner, computer, human):
    if (the_winner != TIE):
        print(the_winner, "won!\n" )
    else:
        print("It's a tie! \n")

    if (the_winner == computer):
        print("As predicted I am triumphant once again. \n" \
            "Proof that computers are superior to humans in all regards.")
        
    elif the_winner == human:
        print ("No, no!  It cannot be!  Somehow you tricked me, human. \n" \
              "But never again!  I, the computer, so swears it!")

    elif the_winner == TIE:
        print ("You were most lucky, human, and somehow managed to tie me.  \n" \
              "Celebrate today... for this is the best you will ever achieve.") 
         
the_winner = winner_board(random_board, humlegal, comlegal)
congrat_winner(the_winner, computer, human)

    
    
  





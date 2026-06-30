def again_function():
    again = input(f"Rematch? \n")
    if again.lower()=="yes":
        print("Starting again")
        return True
    elif again.lower()=="no":
        print("Then perish! ")
        return False
    else:
        print("Say that again? ")
        again_function()
    
def wining_condition(table, player):
    for i in table:
        if i[0]==player and i[1]==player and i[2]==player:
            print(f"Player {player} wins a match")
            display_board(table)
            return True
    
    for i in (range(0, (len(table)))):
        if table[0][i]==player and table[1][i]==player and table[2][i]==player:
            print(f"Player {player} wins a match")
            display_board(table)
            return True

    if table[0][0]==player and table[1][1]==player and table[2][2]==player:
        print(f"Player {player} wins a match")
        display_board(table)
        return True

    if table[0][2]==player and table[1][1]==player and table[2][0]==player:
        print(f"Player {player} wins a match")
        display_board(table)
        return True
    
    return False

def display_board(table):
    for i in range(0,3):
        print(table[i])

    

again = True
while again == True:

    win = False
    board = ["-","-","-"],["-","-","-"],["-","-","-"]
    turn = 1

    while not win:
        if turn % 2 == 1:
            player = "X"
        else:
            player = "O"

        
        display_board(board)
        
        move = input(f"Players {player} turn. Insert two numbers to select a row and a column example: [ 1 2 ] :")
        row, column = move.split(" ")

        if int(row) not in range(0,2) or int(column) not in range(0,2):
            print("You reached beyond the border")
            continue
        elif board[int(row)-1][int(column)-1] != "-":
            print("This bracket is ocupied try again")
            continue
        else:
            board[int(row)-1][int(column)-1] = player

        win = wining_condition(board, player)
        turn+=1

    again = again_function()


    


    

    



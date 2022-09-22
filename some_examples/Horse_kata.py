'''Aleksieiev Valentyn
19/07/2022
There is a horse on the figured board, determine whether the horse can get to a given cell in 2 moves.
'''


RULES_1 = 'ABCDEFGH'
RULES_2 = '87654321'
new_game_rules = '''Let's play my chess-game. ©2022 Aleksieiev Valentyn.
Write down where your horse is and the cell where he wants to go in 2 moves.
The program will calculate the possibility or absence of such options.
Input only in this format: lowercase "a1" or uppercase "A1".
==============  NEW GAME HAS JUST STARTED!  ==============
The playing field has been formed\n'''


def can_capture_horse(x1,y1, x2,y2, count=1):
    h_next = ((-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1))
    answer = (False, '00', count)
    for x, y in h_next:
        if 0<=x1+x<8 and 0<=y1+y<8:
            if x1 + x == x2 and y1 + y ==y2:
                answer = (True, RULES_1[x1]+RULES_2[y1], count)
                break
            elif count==1 and can_capture_horse(x1+x, y1+y, x2, y2, count+1)[0]:
                    answer = (True, RULES_1[x1+x]+RULES_2[y1+y], count+1)
                    break        
    return answer
                
def board_init():
    board = [0]*8
    for i in range(8):
        board[i] = [' ']*8
        for j in range(8):
            board[i][j] = ['o','x'][(i+j)%2]
    return board

def print_board(board, hcell='A0', c_new='A0'):
    print('\033[41m\033[37m',end='')
    [print(ch, end=' ') for ch in ' ' + RULES_1]
    print('\033[0m')
    [print(f'\033[41m\033[37m{8-i}\033[0m', *line, f'\033[41m\033[37m{8-i}\033[0m') for i, line in enumerate(board)]
    print('\033[41m\033[37m',end='')
    [print(ch, end=' ') for ch in ' ' + RULES_1]
    print('\033[0m')

def check_cell(cell):
    
    return len(cell)==2 and cell[0] in RULES_1 and cell[1] in RULES_2

def input_cell(mes):
    cell = input(mes).upper()
    while not(check_cell(cell)):
        print('You input wrong cell, please repeat')
        cell = input(mes).upper()
    return cell

print(new_game_rules)  #print greeting message
my_board = board_init()  # init new board 
print_board(my_board)  #print new board

horse = input_cell('Input horse cell like "a1" or "A1" or "00" to exit: ')
while horse!='00':
    cell_new = input_cell('Input cell "N" to calculate: ')
    if horse != cell_new:
        x1, y1 = RULES_1.index(horse[0]), RULES_2.index(horse[1])
        my_board[y1][x1] = 'H'
        x2, y2 = RULES_1.index(cell_new[0]), RULES_2.index(cell_new[1])
        my_board[y2][x2] = 'N'
        print(f'Add Horse {horse}="H" and new cell to calc {cell_new}="N"')
        print_board(my_board)  #print board with horse and new_cell
        answer = can_capture_horse(x1, y1, x2, y2) #calc steps and ability to get to the new cell
        # answer = (True, 'D', '3', 0)
        if answer[0]:
            if answer[2]>1:
                print(f'\033[1mYes we can move to cell {cell_new} from cell {horse}->{answer[1]}->{cell_new} we need only {answer[2]} steps.\033[0m')
            else:
                print(f'\033[1mYes we can move to cell {cell_new} we need only {answer[2]} step.\033[0m')
        else:
            print(f"\033[1mNo, we can't get your horse to cell {cell_new} in 2 steps\033[0m")
    else:
        print(f'\033[1mYour Horse alredy in cell {horse}:)\033[0m')
    if input('Press enter to generate new game! or 0 to exit ')=='0': break
    print('\n\n'+new_game_rules)
    my_board = board_init()  # init new board 
    print_board(my_board)  #print new board
    horse = input_cell('Input horse cell like "a1" or "A1" or "00" to exit: ')
print('Have a nice day!')

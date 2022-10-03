'''Aleksieiev Valentyn
15/07/2021
In chess, queens can move any number of sqaueres horizontally, vertically or diagonally.
Given the location of your queen and your opponents' queen, determine whethere or not
you're able to capture your opponents' queen. Your location and your opponents' location
are the first and second elements of the list, respectively.
['A1', 'H8'] -> True
['A1', 'C2'] -> False
['G3', 'E5'] -> True
'''

def can_capture(lst):
    rules = 'ABCDEFGH'
    x1, y1 = rules.index(lst[0][0])+1, int(lst[0][1])
    x2, y2 = rules.index(lst[1][0])+1, int(lst[1][1])
    if 1<=max(x1, x2, y1, y2)<=8 and 1<=min(x1, x2, y1, y2)<=8:
        if x1==x2 or y1==y2 or abs(x2-x1)==abs(y2-y1):
            return True
        else:
            return False
    else:
        return None
    

my_queen = input('Input your queen position or 00 to exit: ')

while my_queen!='00':
    if not my_queen:
        my_queen = input('Input your queen position or 00 to exit: ')
        if my_queen == '00': break
    op_queen = input("Input your opponents' position: ")
    ans = can_capture([my_queen.upper(), op_queen.upper()])
    if ans:
        print("Yes! Your queen can capture your opponents' queen.")
    elif ans==False:
        print("No! Your queen can't capture your opponents' queen.")
    else:
        print("Your input error position of the queens")
        
    my_queen, op_queen = '', ''
    

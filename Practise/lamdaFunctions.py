'''
1 2 3
0 5 4
8 7 6
'''
from cgitb import small


Current_state = [[1,2,3], [0,5,4], [8,7,6]]

GOAL_STATE = [[1,2,3], [4,5,6], [7,8,0]]

Open_List = []
Closed_List = []

def print_board(board):
    for i in board:
        print('-'*11)
        for j in i:
            print(j, '|', end=' ')
        print()

def getPos(value):
    for i, j in enumerate(Current_state):
        if j.count(value) > 0:
            return i, j.index(value)

def getMoves(currpos):
    moves = []
    if currpos[0]+1 < 3:
        moves.append((currpos[0]+1, currpos[1]))
    if currpos[0]-1 >= 0:
        moves.append((currpos[0]-1, currpos[1]))
    if currpos[1]+1 < 3:
        moves.append((currpos[0], currpos[1]+1))
    if currpos[1]-1 >=0:
        moves.append((currpos[0], currpos[1]-1))
    return moves

def check_if_current_pos_is_correct(pos):
    if GOAL_STATE[pos[0]][pos[1]] == Current_state[pos[0]][pos[1]]:
        return True
    else:
        return False


def count_wrong_tile(node, height):
    count = 0
    for i,j in enumerate(node):
        for m,n in enumerate(j):
            if n != GOAL_STATE[i][m]:
                count += 1
    return count+height

def expand_node(node):
    currPos = getPos(0)
    possibleMoves = getMoves(currPos)
    expanded_nodes = []
    temp_state = node
    for i in possibleMoves:
        if check_if_current_pos_is_correct(i):
            continue
        temp_state[currPos[0]][currPos[1]] = temp_state[i[0]][i[1]]
        temp_state[i[0]][i[1]] = 0
        if temp_state not in Closed_List:
            expanded_nodes.append(temp_state)
    return expanded_nodes

if __name__=='__main__':
    final_node = []
    height = 0
    print_board(Current_state)
    while final_node != GOAL_STATE:
        height += 1
        nodes = expand_node(Current_state) 
        if GOAL_STATE in nodes:
            print_board(GOAL_STATE)
            break
        else:
            heuristic_value = []
            for i in nodes:
                heuristic_value.append(count_wrong_tile(i, height))


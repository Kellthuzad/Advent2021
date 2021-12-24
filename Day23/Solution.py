from itertools import permutations
from copy import deepcopy

def main():
    filehandle = open("./Day23/input.txt")
    lines = []

    for line in filehandle:
        lines.append(line.strip())

    roomMap = mapRoom(lines)
    # state = {(0, 0): '.', (1, 0): 'B', (3, 0): 'C', (5, 0): '.', (7, 0): 'A', (9, 0): '.', (10, 0): '.', (2, -1): '.', (4, -1): '.', (6, -1): '.', (8, -1): 'D', (2, -2): 'A', (4, -2): 'B', (6, -2): 'C', (8,-2): 'D'}
    # canMove('C', 6, (3,0), state)
    print(dfs(roomMap, 0))

def mapRoom(lines):
    map = {}

    for i in range(11):
        if i in [2,4,6,8]:
            continue
        map[(i,0)] = '.'

    xPos= 2
    for char in lines[2]:
        if char != '#':
            map[(xPos,-1)] = char
            xPos += 2
    
    xPos= 2
    for char in lines[3]:
        if char != '#':
            map[(xPos,-2)] = char
            xPos += 2
    
    
    
    return map

def canMove(piece, destination, location, state):
    if location[1] == 0:
        return canMoveIn(piece, destination, location, state)
    elif location[1] == -2 and state[(location[0], -1)] != '.':
        return False
    elif state[(location[0] -1, 0)] != '.' and state[(location[0] + 1, 0)] != '.' :
        return False
    return True 
        

            
def canMoveIn(piece, destination, location, state):
    rightOfDestination = location[0] > destination
    start = 0
    end = 0
    if rightOfDestination:
        start = destination
        end = location[0]
    else:
        start = location[0] + 1
        end = destination
    
    for i in range(start, end, 1):
            if i in [2,4,6,8]:
                continue
            if state[(i,0)] != '.':
                return False
    if state[(destination, -1)] != '.':
        return False
    if state[(destination, -2)] == piece or state[(destination, -2)] == '.':
        return True

bestScore = 1e9
def dfs(state, score):
    global bestScore
    destinationMap = {'A':2, 'B':4, 'C':6, 'D':8}
    if winningState(destinationMap, state):
        return score
    for k,v in state.items():
        #dont move empty space
        if v == '.':
            continue
        #dont move correct ones
        elif (k[0] == destinationMap[v] and k[1] == -2) or (k[0] == destinationMap[v] and state[(k[0],-2)] == v):
            continue

        if canMove(v, destinationMap[v], k, state):
            allMoves = moves(v, destinationMap[v], k, state)
            for move in allMoves:
                newState = deepcopy(state)
                newState[k] = '.'
                newState[move] = v
                newScore = score + energyUsage(k, move, v)
                if newScore < bestScore:
                    bestScore = min(bestScore, dfs(newState, newScore))
    
    return bestScore

def moves(piece, destination, location, state):
    allMoves = []
    
    if location[1] == 0:
        #already verified that we can move in, so if the bottom is occupied, that means its the correct one.
        if state[(destination, -2)] != '.':
            return [(destination, -1)]
        else:
            return [(destination, -2)]
    
    else:
        allMoves.extend(allLeftMoves(piece, destination, location, state))
        allMoves.extend(allRightMoves(piece, destination, location, state))
        return allMoves

def allLeftMoves(piece, destination, location, state):
    moves = []
    for i in range(location[0], 0, -1):
        if i in [2,4,6,8]:
            continue
        if state[(i,0)] != '.':
            return moves
        else:
            moves.append((i,0))
    return moves

def allRightMoves(piece, destination, location, state):
    moves = []
    for i in range(location[0], 11, 1):
        if i in [2,4,6,8]:
            continue
        if state[(i,0)] != '.':
            return moves
        else:
            moves.append((i,0))
    return moves
    
def energyUsage(start, finish, variant):
    multMap = {'A':1,'B':10,'C':100,'D':1000}

    total = abs(finish[0] - start[0])
    total += abs(finish[1] - start[1])

    total *= multMap[variant]

    return total

def winningState(destinations, state):
    for k,v in state.items():
        if v != '.' and k[0] != destinations[v]:
            return False
    
    return True

    
main()

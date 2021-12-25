
def main():
    filehandle = open("./Day25/input.txt")
    lines = []

    for line in filehandle:
        lines.append(line.strip())
    rows, columns, eastHerd, southHerd = parse(lines)
    
    steps = walk(eastHerd, southHerd, rows, columns)

    print(steps)

def walk(eastHerd, southHerd, rows, columns):
    moves = True
    i = 0
    while moves:
        eastMoves = moveEast(eastHerd, southHerd, rows, columns)
        southMoves = moveSouth(eastHerd, southHerd, rows, columns)

        if eastMoves or southMoves:
            moves = True
        else:
            moves = False
        i += 1
    
    return i

def moveEast(eastHerd, southHerd, rows, columns):
    newMoveList = []
    for r,c in eastHerd:
        if c+1 == columns:
            newSpot = (r,0)
        else:
            newSpot = (r,c+1)
        if newSpot in eastHerd or newSpot in southHerd:
            continue
        else:
            newMoveList.append((r,c))

    for r,c in newMoveList:
        eastHerd.remove((r,c))
        if c+1 == columns:
            eastHerd.add((r, 0))
        else:
            eastHerd.add((r,c+1))

    if len(newMoveList) > 0:
        return True
    return False

def moveSouth(eastHerd, southHerd, rows, columns):
    newMoveList = []
    for r,c in southHerd:
        if r+1 == rows:
            newSpot = (0,c)
        else:
            newSpot = (r+1,c)
        if newSpot in eastHerd or newSpot in southHerd:
            continue
        else:
            newMoveList.append((r,c))

    for r,c in newMoveList:
        southHerd.remove((r,c))
        if r+1 == rows:
            southHerd.add((0, c))
        else:
            southHerd.add((r+1,c))

    if len(newMoveList) > 0:
        return True
    return False
        

def parse(lines):
    rows = len(lines)
    columns = len(lines[0])
    eastHerd = set()
    southHerd = set()

    for r in range(rows):
        for c in range(columns):
            if lines[r][c] == '>':
                eastHerd.add((r,c))
            elif lines[r][c] == 'v':
                southHerd.add((r,c))


    return rows, columns, eastHerd, southHerd



main()
        
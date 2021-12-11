def main():
    filehandle = open("./Day09/input.txt")
    lines = []

    for line in filehandle:
        lines.append(line.strip())
    topomap = parse(lines)
    #print(findLowPoint(topomap))
    basinFinder(topomap)
        

def parse(lines):
    topomap = []
    for line in lines:
        row = []
        for char in line:
            row.append(int(char))
        topomap.append(row)
    return topomap

def findLowPoint(topomap):
    totalRisk = 0
    for y in range(len(topomap)):
        for x in range(len(topomap[0])):
            totalRisk += checkAndReturnRisk(topomap,x,y)

    return totalRisk
            
def checkAndReturnRisk(topomap, x, y):
    val = topomap[y][x]
    xVals = []
    yVals = []
    if x == 0:
        xVals = [1,0]
    elif x == len(topomap[0]) - 1:
        xVals = [-1,0]
    else:
        xVals = [-1,0,1]

    if y == 0:
        yVals = [1,0]
    elif y == len(topomap) - 1:
        yVals = [-1,0]
    else:
        yVals = [-1,0,1]

    for dX in xVals:
        for dY in yVals:
            if (dY != 0 and dX != 0) or (dY == 0 and dX == 0):
                continue
            if val >= topomap[y + dY][x + dX]:
                return 0

    return val + 1

def basinFinder(topomap):
    visited = set()
    topThree = []
    for y in range(len(topomap)):
        for x in range(len(topomap[0])):
            if (y,x) in visited:
               continue
            elif topomap[y][x] == 9:
                visited.add((y,x))
            else:
                size = determineBasinSize(topomap, visited, x, y)
                topThree = adjustTopThree(topThree, size)
    total = 1
    for i in topThree:
        total *= i
    print(total)
                
def determineBasinSize(topomap, visited, x, y):
    size = 1
    toVisit = [(y,x)]
    while len(toVisit) > 0:
        (y,x) = toVisit.pop(0)
        visited.add((y,x))    
        for dY in [-1,0,1]:
            for dX in [-1,0,1]:
                if not (0 <= y + dY < len(topomap)) or not (0 <= x + dX < len(topomap[0])) or (dX != 0 and dY != 0):
                    continue
                if (y + dY, x + dX) in visited or (y + dY, x + dX) in toVisit:
                    continue
                elif topomap[y + dY][x + dX] == 9:
                    visited.add((y + dY, x + dX))
                else:
                    toVisit.append((y + dY, x + dX))
                    size += 1
        

    return size

def adjustTopThree(topThree, newSize):
    

    topThree.append(newSize)

    if len(topThree) < 3:
        return topThree

    topThree = sorted(topThree, reverse=True)

    return topThree[0:3]




main()
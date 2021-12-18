from copy import deepcopy

topLevelWorkingLine = None

def main():
    global topLevelWorkingLine
    filehandle = open("./Day18/input.txt")
    lines = []

    for line in filehandle:
        lines.append(parse(line.strip(), 1)[1])
    
    findCombinations(lines)
    #current = addAllNums(lines)
    #current = [[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]
    # magnitude = findMag(current[0], current[1])

    # print(magnitude)

def findMag(left, right):
    lVal = 0
    rVal = 0
    if type(left) is list:
        lVal = findMag(left[0], left[1])
    else:
        lVal = left
    
    if type(right) is list:
        rVal = findMag(right[0], right[1])
    else:
        rVal = right

    return lVal * 3 + rVal * 2
    
def findCombinations(lines):
    maxMag = 0
    for i in range(len(lines)):
        for j in range(len(lines)):
            if i == j:
                continue
            newList = [deepcopy(lines[i]),deepcopy(lines[j])]
            reduceNum(newList)
            currentMag = findMag(newList[0], newList[1])
            maxMag = max(maxMag, currentMag)


    print(f'maxMag:{maxMag}')

            
    

def parse(line, index):
    currentList = []

    while index < len(line):
        if line[index] == ']':
            return index + 1, currentList
        elif line[index] == '[':
            index, newList = parse(line, index + 1)
            currentList.append(newList)
        elif line[index] != ',':
            currentList.append(int(line[index]))
            index += 1
        else:
            index += 1
    
    return index, currentList

def addAllNums(lines):
    workingLines = deepcopy(lines)
    current = workingLines.pop(0)

    while lines:
        toAdd = workingLines.pop(0)
        newList = [current, toAdd]
        reduceNum(newList)
        current = newList
    
    return current


def reduceNum(line):
    global topLevelWorkingLine
    topLevelWorkingLine = line
    clean = False
    while not clean:
        clean = findExplosions(line, {}, 1)
        if clean:
            clean = findSplits(line)
    


def findExplosions(line, depthPositions, depth):
    index = 0
    madeIt = True
    while madeIt and index < 2:
        if type(line[index]) is list:
            depthPositions[depth] = index
            if depth >= 4:
                explode(line[index], depthPositions)
                line[index] = 0
                return False
            madeIt = findExplosions(line[index], depthPositions, depth+1)
        index += 1

    return madeIt

def findSplits(line):
    index = 0
    madeIt = True
    while madeIt and index < 2:
        if type(line[index]) is list:
            madeIt = findSplits(line[index])
        elif line[index] >= 10:
            line[index] = split(line[index])
            return False
        index += 1

    return madeIt

def split(num):
    returnVal = [num//2, num//2]

    if num % 2 > 0:
        returnVal[1] += 1
    
    return returnVal
    
def explode(pair, depthPositions):
    leftAdder = pair[0]
    rightAdder = pair[1]

    addLeft(leftAdder, depthPositions)
    addRight(rightAdder, depthPositions)

def addLeft(val, depthPositions):
    newPositions = deepcopy(depthPositions)
    lists = makeListStack(newPositions)
    depth = 4
    index = newPositions[4]
    currentList = lists.pop(-1)

    while True:
        if index == 0:
            if not lists:
                return
            currentList = lists.pop(-1)
            depth -= 1
            index = newPositions[depth]
        else:
            index -= 1
            if type(currentList[index]) is int:
                currentList[index] += val
                return
            elif type(currentList[index]) is list:
                newPositions[depth] = index
                lists.append(currentList)
                currentList = currentList[index]
                depth += 1
                newPositions[depth] = 2
                index = newPositions[depth]
            
def addRight(val, depthPositions):
    lists = makeListStack(depthPositions)
    depth = 4
    index = depthPositions[4]
    currentList = lists.pop(-1)

    while True:
        if index == len(currentList) -1:
            if not lists:
                return
            currentList = lists.pop(-1)
            depth -= 1
            index = depthPositions[depth]
        else:
            index += 1
            if type(currentList[index]) is int:
                currentList[index] += val
                return
            elif type(currentList[index]) is list:
                depthPositions[depth] = index
                lists.append(currentList)
                currentList = currentList[index]
                depth += 1
                depthPositions[depth] = -1
                index = depthPositions[depth]

def makeListStack(depthPositions):
    global topLevelWorkingLine
    lists = [topLevelWorkingLine]
    currentList = topLevelWorkingLine
    for i in range(1,4,1):
        lists.append(currentList[depthPositions[i]])
        currentList = currentList[depthPositions[i]]
    
    return lists
main()

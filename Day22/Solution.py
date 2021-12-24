
def main():
    filehandle = open("./Day22/input.txt")
    lines = []

    for line in filehandle:
        lines.append(line.strip())

    commands = parse(lines)
    onList = set()
    # for comm in commands:
    #     onList = runCommand(onList, comm)

    print(len(onList))


def parse(lines):
    inputs = []

    for line in lines:
        on = False
        directions = line.split(' ')
        if directions[0] == 'on':
            on = True
        
        commands = directions[1].split(',')
        ranges = []
        for nums in commands:
            numbers = nums.split('=')
            minMax = numbers[1].split('..')
            newRange = (int(minMax[0]), int(minMax[1]))
            assert newRange[0] < newRange[1]
            ranges.append(newRange)
        
        inputs.append((on,ranges[0], ranges[1], ranges[2]))

    return inputs


def runCommand(onList, command):
    on = command[0]

    for x in range(command[1][0], command[1][1] +1, 1):
        if x > 50 or x < -50:
            continue
        for y in range(command[2][0], command[2][1] +1, 1):
            if y > 50 or y < -50:
                continue
            for z in range(command[3][0], command[3][1] +1, 1):
                if z > 50 or z < -50:
                    continue
                if on and (x,y,z) not in onList:
                    onList.add((x,y,z))
                elif not on and (x,y,z) in onList:
                    onList.remove((x,y,z))
    
    return onList

def sumCommands(rangeList,command):
    
    # range has x,y, and z ranges
    for ranges in rangeList:
        if not command[0]:
            xRange = findOverlapForRemoval(ranges[0],command[1])
            yRange = findOverlapForRemoval(ranges[1],command[2])
            zRange = findOverlapForRemoval(ranges[2],command[3])

            if xRange and yRange and zRange:
                newRange = (xRange,yRange,zRange)
                splitRanges(ranges, newRange)

def splitRanges(ranges, deletionRange):

    

def findOverlapForRemoval(establishedRange, incomingRange):
    if incomingRange[0] < establishedRange[0] and incomingRange[1] >= establishedRange[0]:
        return (establishedRange[0], incomingRange[1])

    elif incomingRange[0] >= establishedRange[0] and incomingRange[1] < establishedRange[1]:
        return incomingRange

    elif incomingRange[0] >= establishedRange[0] and incomingRange[1] >= establishedRange[1]:
        return (incomingRange[0], establishedRange[1])
    
    else:
        return None
    

    


main()

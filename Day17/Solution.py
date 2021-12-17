
def main():
    filehandle = open("./Day17/input.txt")
    lines = []

    for line in filehandle:
        lines.append(line.strip())  
    xBounds, yBounds = parse(lines[0])
    xMinV = findXVelocityMin(xBounds)
    xMaxV = findXVelocityMax(xBounds, xMinV)
    xVBounds = (xMinV, xMaxV)
    print(dumbWay(xBounds, yBounds, xVBounds))


def parse(line):
    chunks = line.split(' ')

    xString = chunks[2]
    yString = chunks[3]

    xString = xString.strip(',')
    xString = xString.strip('x=')
    xbounds = xString.split('..')

    
    yString = yString.strip(',')
    yString = yString.strip('y=')
    ybounds = yString.split('..')

    x = (int(xbounds[0]), int(xbounds[1]))
    y = (int(ybounds[0]), int(ybounds[1]))

    return x,y

def findXVelocityMin(xBounds):
    didntMakeIt = True
    xV = 1
    while didntMakeIt:
        position = 0
        tempxV = xV
        while tempxV > 0:
            position += tempxV
            tempxV -= 1
        if position >= xBounds[0]:
            didntMakeIt = False
            break
        else:
            xV += 1

    return xV

def findXVelocityMax(xBounds, xMinV):
    makesIt = True
    xV = xMinV - 1

    while makesIt:
        makesIt = False
        position = 0
        xV += 1
        tempxV = xV 
        while tempxV > 0:
            position += tempxV
            tempxV -= 1
            if xBounds[0] <= position <= xBounds[1]:
                makesIt = True
                break
        
    return xV


def runStep(position, velocity):
    x = position[0]
    y = position[1]
    xV = velocity[0]
    yV = velocity[1]

    x += xV
    y += yV
    
    if xV < 0:
        xV += 1
    elif xV > 0:
        xV -= 1
    
    yV -= 1

    return (x,y), (xV, yV)

def runningSim(xBounds, yBounds, velocity):
    initVelocity = velocity
    position = (0,0)
    yMax = -1e9
    madeIt = False
    while position[0] < xBounds[1] and position[1] > yBounds[0]:
        position, velocity = runStep(position, velocity)
        if position[1] > yMax:
            yMax = position[1]
        if xBounds[0] <= position[0] <= xBounds[1] and yBounds[0] <= position[1] <= yBounds[1]:
            madeIt = True
            break
    
    if madeIt:
        return yMax, madeIt
    return int(-1e9), madeIt


def dumbWay(xBounds, yBounds, xVBounds):
    yMax = int(-1e9)
    print(f'xVBounds:{xVBounds}')
    totalMakes = 0
    for xV in range(xVBounds[0],200, 1):
        for yV in range(-300,300, 1):
            newTop ,madeIt = runningSim(xBounds, yBounds, (xV,yV))
            if yMax < newTop:
                yMax = newTop
            if madeIt:
                totalMakes += 1
    
    return yMax, totalMakes
main()

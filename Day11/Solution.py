def main():
    filehandle = open("./Day11/input.txt")
    lines = []

    for line in filehandle:
        lines.append(line.strip())
    octos = parse(lines)
    cycle(octos)
    #print(runOneCycle(octos))


def parse(lines):
    returnVal = []

    for line in lines:
        row = []
        for char in line:
            row.append(int(char))
        returnVal.append(row)
    
    return returnVal

def cycle(octos):
    totalFlashes = 0
    for i in range(10000000):
        octos, flashes = runOneCycle(octos)
        totalFlashes += flashes
        if flashes == -1:
            print(i + 1)
            break
    #print(totalFlashes)
    
    for line in octos:
        print(line)

def runOneCycle(octos):
    hasFlashed = set()
    flashes = 0
    for y in range(len(octos)):
        for x in range(len(octos[0])):
            octos[y][x] += 1
            if octos[y][x] >= 10 and (y,x) not in hasFlashed:
                hasFlashed.add((y,x))
                flash(octos, y,x, hasFlashed)
    
    for y in range(len(octos)):
        for x in range(len(octos[0])):
             if octos[y][x] >= 10:
                 flashes += 1
                 octos[y][x] = 0
    
    if flashes == len(octos) * len(octos[0]):
        flashes = -1

    return octos, flashes

def flash(octos, y, x, hasFlashed):

    for dy in [-1,0,1]:
        for dx in [-1,0,1]:
            newx = x + dx
            newy = y + dy
            if not (dx == 0 and dy == 0) and (0 <= newx < len(octos[0])) and (0 <= newy < len(octos)):
                octos[newy][newx] +=1
                if octos[newy][newx] >= 10 and (newy,newx) not in hasFlashed:
                    hasFlashed.add((newy,newx))
                    flash(octos, newy, newx, hasFlashed)
    
    return hasFlashed


main()
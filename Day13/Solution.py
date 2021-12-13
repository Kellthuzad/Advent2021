from copy import deepcopy

def main():
    filehandle = open("./Day13/input.txt")
    lines = []

    for line in filehandle:
        lines.append(line.strip())
    coords, instructions = parse(lines)
    #fold(coords, instructions[0])
    multiFold(coords, instructions)
    
def parse(lines):
    coords = set()
    instructions = []
    instructionTime = False
    for line in lines:
        if '=' in line:
            instruction = line.split(' ')[2]
            instructions.append(instruction)
        elif ',' in line:
            nums = line.split(',')
            coords.add((int(nums[0]), int(nums[1])))

    return coords, instructions
    
def multiFold(coords, instructions):

    for instruction in instructions:
        coords = fold(coords, instruction)
    
    maxX = 0
    maxY = 0
    for coord in coords:
        if coord[0] > maxX:
            maxX = coord[0]
        if coord[1] > maxY:
            maxY = coord[1]
    
    x = ['_'] * (maxX+1)
    y = []
    for i in range((maxY+1)):
        y.append(deepcopy(x))

    for coord in coords:
        y[coord[1]][coord[0]] = '#'

    for line in y:
        print(line)

def fold(coords, instruction):
    foldSide = 0
    if 'y' in instruction:
        foldSide = 1

    value = int(instruction.split('=')[1])

    newCoords = set()

    for coord in coords:
        coordVal = coord[foldSide]
        if coordVal > value:
            diff = coordVal - value
            newCoord = makeCoord(foldSide, diff, coord, value)
            newCoords.add(newCoord)
        else:
            newCoords.add(coord)
    
    return newCoords
        
def makeCoord(foldSide, diff, coord, value):

    if foldSide == 0:
        return (value - diff, coord[1])
    else:
        return (coord[0], value - diff)

main()
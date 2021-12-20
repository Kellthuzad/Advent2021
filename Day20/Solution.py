
def main():
    global enhance
    filehandle = open("./Day20/input.txt")
    lines = []

    for line in filehandle:
        lines.append(line.strip())
    
    enhance, image = parse(lines)

    newImage = image
    for i in range(2):
        newImage = enhanceImage(enhance, newImage, i)

    total = 0
    
    for line in newImage:
        total += sum(line)
    
    print(total)
    
enhance = None

def parse(lines):
    enhance = []
    for char in lines[0]:
        if char == '#':
            enhance.append(1)
        else:
            enhance.append(0)

    image = []
    for i in range(2,len(lines),1):
        row = []
        for char in lines[i]:
            if char == '#':
                row.append(1)
            else:
                row.append(0)
        image.append(row)

    return enhance, image

def enhanceImage(enhance, image, roundNumber):
    newImage = []
    #the plus 2 is to account for the 'infinite' space. basically the dark pixels that are touching light ones. 
    for r in range(len(image)+2):
        newRow = []
        for c in range(len(image[0])+2):
            binNum = calcFromNeighbors(r-1, c-1, image, roundNumber)
            newRow.append(enhance[binNum])
        newImage.append(newRow)
    
    return newImage


def calcFromNeighbors(r, c, image, roundNumber):
    global enhance
    binNum = ''
    i = 0
    for dr in [-1,0,1]:
        for dc in [-1,0,1]:
            R = r + dr
            C = c + dc

            if 0 > R or R >= len(image) or 0 > C or C >= len(image[0]):
                if roundNumber % 2 == 1:
                    binNum += f'{enhance[0]}'
                else:
                    binNum += '0'
            else:
                binNum += f'{image[R][C]}'
            i += 1
    return int(binNum,2)
                


main()

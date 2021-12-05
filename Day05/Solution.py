def main():
    filehandle = open("./Day05/input.txt")
    lines = []

    for line in filehandle:
        lines.append(line.strip())

    calcOverlap(lines)

        
def calcOverlap(input):
    visited = {}

    for line in input:
        inputs = line.split(' -> ')

        startCoords = inputs[0].split(',')
        endCoords = inputs[1].split(',')
        sX = int(startCoords[0])
        fX = int(endCoords[0])
        sY = int(startCoords[1])
        fY = int(endCoords[1])
        stepX = 1
        stepY = 1


        if sX != fX and sY != fY:
            if sX > fX:
                stepX = -1
                fX -= 1
            else:
                fX += 1
            
            if sY > fY:
                stepY = -1
                fY -= 1
            else:
                fY += 1
            x = sX
            y = sY

            for i in range(abs(fX - sX)):
                if (x,y) in visited:
                    visited[(x,y)] += 1
                else:
                    visited[(x,y)] = 1
                x += stepX
                y += stepY


        else:
            if sX > fX:
                stepX = -1
                fX -= 1
            else:
                fX += 1
            
            if sY > fY:
                stepY = -1
                fY -= 1
            else:
                fY += 1

            for x in range(sX, fX, stepX):
                for y in range(sY, fY, stepY):
                    if (x,y) in visited:
                        visited[(x,y)] += 1
                    else:
                        visited[(x,y)] = 1

    score = 0
    for key, value in visited.items():
        if value > 1:
            score += 1

    print(score)




main()


def main():
    filehandle = open("./Day08/input.txt")
    lines = []

    for line in filehandle:
        lines.append(line.strip())
    #quickAndDirty(lines)
    print(DoPartTwo(lines))
    
def DoPartTwo(input):
    total = 0

    for line in input:
        numString = ""
        splitString = line.split('|')
        chunks = splitString[0].strip()
        output = splitString[1].strip()
        set = buildSet(chunks)

        for chunk in output.split(' '):
            val = sortAndRevertToString(chunk)
            numString += f'{set[val]}'
        
        total += int(numString)
    
    return total

def quickAndDirty(input):
    total = 0
    for line in input:
        output = line.split('|')[1]

        for chunk in output.split(' '):
            l = len(chunk.strip())
            if l == 2 or l == 4 or l == 3 or l == 7:
                total += 1
    
    print(total)

def buildSet(segment):
    chunks = segment.split(' ')
    numbers = {}

    for chunk in chunks:
        if len(chunk) == 2:
            numbers[1] = sortAndRevertToString(chunk)
        elif len(chunk) == 4:
            numbers[4] = sortAndRevertToString(chunk)
        elif len(chunk) == 3:
            numbers[7] = sortAndRevertToString(chunk)
        elif len(chunk) == 7:
            numbers[8] = sortAndRevertToString(chunk)

    isSixOrZero = []
    isFiveOrTwo = []
    for chunk in chunks:
        if len(chunk) == 6 and IsCorrectNumber(numbers[4], chunk):
            numbers[9] = sortAndRevertToString(chunk)
        elif len(chunk) == 6:
            isSixOrZero.append(chunk)
        elif len(chunk) == 5 and IsCorrectNumber(numbers[1], chunk):
            numbers[3] = sortAndRevertToString(chunk)
        elif len(chunk) == 5:
            isFiveOrTwo.append(chunk)

    for potentialNum in isSixOrZero:
        if IsCorrectNumber(numbers[1], potentialNum):
            numbers[0] = sortAndRevertToString(potentialNum)
        else:
            numbers[6] = sortAndRevertToString(potentialNum)
    
    for potentialNum in isFiveOrTwo:
        if IsCorrectNumber(numbers[6], potentialNum, 1):
            numbers[5] = sortAndRevertToString(potentialNum)
        else:
            numbers[2] = sortAndRevertToString(potentialNum)

    #Flip the dict cause i want to look up char chunks when actually doing the problem
    return dict((v,k) for k,v in numbers.items())


def IsCorrectNumber(referenceNum, potential, missesAllowed = 0):
    totalMisses = 0

    for char in referenceNum:
        if char not in potential:
            totalMisses += 1
        if totalMisses > missesAllowed:
            return False
    return True

def sortAndRevertToString(chunk):
    chunkList = sorted(chunk)
    returnVal = ""
    for char in chunkList:
        returnVal += char
    
    return returnVal
main()
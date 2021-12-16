
def main():
    filehandle = open("./Day16/input.txt")
    lines = []

    for line in filehandle:
        lines.append(line.strip())

    bString = parse(lines[0])
    print(packet(0, bString))
    # print(f'versions: {versionSum}')

def parse(line):
    bString = ''
    map = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111',}
    for char in line:
        bString += map[char]
    
    return bString

def packet(index, bin):
    global versionSum
    version = int(bin[index:index+3],2)
    versionSum += version
    index += 3

    pType = int(bin[index:index+3],2)
    index += 3

    val = 0
    if pType == 4:
        index, val = walkLiteral(index, bin)
    else:
        index, newVals = walkOperator(index, bin)
        val = operate(pType, newVals)

    
    return index, val
    
def operate(pType, vals):

    if pType == 0:
        return sum(vals)
    elif pType == 1:
        val = 1
        for num in vals:
            val *= num
        return val
    elif pType == 2:
        return min(vals)
    elif pType == 3:
        return max(vals)
    elif pType == 5:
        if vals[0] > vals[1]:
            return 1
        else:
            return 0
    elif pType == 6:
        if vals[0] < vals[1]:
            return 1
        else:
            return 0
    elif pType == 7:
        if vals[0] == vals[1]:
            return 1
        else:
            return 0

def walkOperator(index, bin):
    vals = []
    if bin[index] == '0':
        index += 1
        subPacketSize = int(bin[index: index + 15],2)
        index += 15
        endOfSubPacket = index + subPacketSize
        while index < endOfSubPacket:
            index, val = packet(index,bin)
            vals.append(val)
    else:
        index += 1
        numOfSubPackets = int(bin[index: index + 11],2)
        index += 11
        for i in range(numOfSubPackets):
            index, val = packet(index,bin)
            vals.append(val)

    return index, vals
    
def walkLiteral(index, bin):
    byteCounter = 0
    bString = ''
    while bin[index] != '0':
        byteCounter += 1
        bString += bin[(index+1): (index+5)]
        index +=5
    
    byteCounter += 1
    bString += bin[(index+1): (index+5)]
    index += 5

    val = int(bString, 2)
    return index, val

versionSum = 0
main()

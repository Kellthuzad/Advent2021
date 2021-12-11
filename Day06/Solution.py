

def main():
    filehandle = open("./Day06/input.txt")
    lines = []

    for line in filehandle:
        lines.append(line.strip())
    initialArr = quickParse(lines[0])
    replicateSpawn(initialArr)

    

def quickParse(line):
    init = emptyDict()
    for i in line.split(','):
        if int(i) in init:
            init[int(i)] += 1
        else:
            init[int(i)] = 1
    for i in range(9):
        if i not in init:
            init[i] = 0
    return init



def replicateSpawn(input):
    dictOfDays = input
    tempDictOfDays = emptyDict()

    for x in range(256):
        for i in range(9):
            value = dictOfDays[i]
            if i == 0:
                tempDictOfDays[6] += value
                tempDictOfDays[8] += value
            else:
                tempDictOfDays[i - 1] += value
        dictOfDays = tempDictOfDays
        tempDictOfDays = emptyDict()
        
    
    totalFish = 0
    for key, value in dictOfDays.items():
        totalFish += value

    print(totalFish)

def emptyDict():
    return {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}

main()

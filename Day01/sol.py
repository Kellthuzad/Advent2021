import urllib.request as Request


def main():
    filehandle = open("./Day01/input.txt")
    lines = []
    numbers = []
    for line in filehandle:
        lines.append(line)
        numbers.append(int(line))
    
    total = 0
    previous = -1
    for num in numbers:
        if previous != -1 and num > previous:
            total += 1
        
        previous = num
    
    print(total)
    partTwo(numbers)

def partTwo(numbers):
    answer = 0
    tempList = []
    tempList2 = []
    permList = []

    for num in numbers:
        for l in tempList:
            l.append(num)
            if len(l) == 3:
                permList.append(sum(l))
                if len(permList) > 1 and permList[-2] < permList[-1]:
                    answer += 1
            else:
                tempList2.append(l)
        tempList2.append([num])
        tempList = tempList2
        tempList2 = []

    print(answer)
        

main()
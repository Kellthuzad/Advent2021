
def main():
    filehandle = open("./Day19/input.txt")
    lines = []

    for line in filehandle:
        lines.append(line.strip())
    
    scannerInput = parse(lines)

    findBeacons(scannerInput)


def testShit(scannerInput, og, comparer):
    zeroMap = buildBeaconMap(og, scannerInput[og])
    newMap = buildBeaconMap(comparer, scannerInput[comparer])
    scoreMap = compareMaps(zeroMap, newMap)

    translator = None
    vector = None
    for k,v in scoreMap.items():
        translator = findOrientation(k, zeroMap, newMap)
        vector = findMagnitude(k, translator)
        break
    
    
    for i in range(len(scannerInput[comparer])):
        newPoint = translate(scannerInput[comparer][i], vector, translator)
        scannerInput[comparer][i] = newPoint
        if newPoint not in scannerInput[0]:
            scannerInput[0].append(newPoint)

def findBeacons(scannerInput):
    uniqueBeacons = set()
    for beacon in scannerInput[0]:
        uniqueBeacons.add(beacon)

    mapped = set()
    mapped.add(0)
    beaconMaps = {}
    for i in range(len(scannerInput)):
        beaconMaps[i] = buildBeaconMap(i, scannerInput[i])

    while len(mapped) < len(scannerInput):
        for i in range(1,len(scannerInput),1):
            if i in mapped:
                continue
            
            for num in mapped:
                zeroMap = beaconMaps[num]
                newMap = beaconMaps[i]
                scoreMap = compareMaps(zeroMap, newMap)
                if len(scoreMap) < 12:
                    continue
                else:
                    mapped.add(i)
                translator = None
                vector = None
                for k,v in scoreMap.items():
                    translator = findOrientation(k, zeroMap, newMap)
                    if translator is None:
                        mapped.remove(i)
                        break
                    vector = findMagnitude(k, translator)
                    break
                
                if translator is None:
                    continue

                for j in range(len(scannerInput[i])):
                    newPoint = translate(scannerInput[i][j], vector, translator)
                    scannerInput[i][j] = newPoint
                    if newPoint not in uniqueBeacons:
                        uniqueBeacons.add(newPoint)
                beaconMaps[i] = buildBeaconMap(i, scannerInput[i])
                break
        
    print(len(uniqueBeacons))

def parse(lines):
    scannerMap = {}
    scanner = 0
    for line in lines:
        if '---' in line:
            chunks = line.split(' ')
            scanner = int(chunks[2])
            scannerMap[scanner] = []
        elif len(line.strip()) > 0:
            chunks = line.split(',')
            scannerMap[scanner].append((int(chunks[0]),int(chunks[1]),int(chunks[2])))

    return scannerMap

def buildBeaconMap(scanner, beacons):
    beanconMap = {}
    for i in range(len(beacons)):
        x,y,z = beacons[i]
        beanconMap[(x,y,z)] = set()
        for j in range(len(beacons)):
            if i != j:
                dx,dy,dz = beacons[j]
                beanconMap[(x,y,z)].add((dx-x,dy-y,dz-z))
    
    return beanconMap

def compareMaps(firstMap, secondMap):
    scoreMapper = {}
    for k,v in firstMap.items():
        for sk, sv in secondMap.items():
            score = compareBeacons(v, sv)
            if score > 1:
                scoreMapper[(k,sk)] = score
    
    return scoreMapper    

def compareBeacons(first, second):
    matchCount = 0
    for i in first:
        fCoord = sortRelativeCoord(i)
        for j in second:
            sCoord = sortRelativeCoord(j)
            if sCoord == fCoord:
                matchCount += 1
                break


    return matchCount

def sortRelativeCoord(coord):
    a,b,c = coord
    a,b,c = abs(a), abs(b), abs(c)
    point = sorted([a,b,c])

    return point

def findOrientation(sameBeacon, firstMap, secondMap):
    first = sameBeacon[0]
    second = sameBeacon[1]
    point1 = None
    point2 = None
    translator = {}

    relativeBeaconList1 = firstMap[first]
    
    for i in relativeBeaconList1:
        point1 = i
        break

    relativeBeaconList2 = secondMap[second]
    sort = sortRelativeCoord(point1)
    for i in relativeBeaconList2:
        if sortRelativeCoord(i) == sort:
            point2 = i
            break
    if point2 is None and relativeBeaconList1:
        relativeBeaconList1.remove(point1)
        translator = findOrientation(sameBeacon, firstMap, secondMap)
    
    if len(translator) > 0:
        return translator

    for i in range(1,len(point1)+1,1):
        for j in range(1,len(point1)+1,1):
            if abs(point1[i-1]) == abs(point2[j-1]):
                if point1[i-1] != point2[j-1]:
                    translator[i] = -j
                else:
                    translator[i] = j
                break

    return translator

def findMagnitude(sameBeacon, translator):
    vector = [0,0,0]
    
    first = sameBeacon[0]
    second = sameBeacon[1]
    mappedSecond = [0,0,0]
    for k,v in translator.items():
        if v < 0:
            mappedSecond[k-1] = -second[abs(v+1)]
        else:
            mappedSecond[k-1] = second[v-1]
    
    for i in range(3):
        vector[i] = first[i] - mappedSecond[i]
    
    return vector

def translate(point, vector, translator):
    newPoint = [0,0,0]
    for k,v in translator.items():
        if v < 0:
            newPoint[k-1] = point[abs(v+1)]
        else:
            newPoint[k-1] = point[v-1]

    for i in range(3):
        if translator[i+1] < 0:
            newPoint[i] = newPoint[i] - vector[i]
            newPoint[i] = -newPoint[i]
        else:
            newPoint[i] = newPoint[i] + vector[i]
        
    return (newPoint[0],newPoint[1],newPoint[2])

main()

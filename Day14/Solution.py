def main():
    filehandle = open("./Day14/input.txt")
    lines = []

    for line in filehandle:
        lines.append(line.strip())

    input = lines[0]
    map = parse(lines[2:])


    runRxn(input, map)

def parse(lines):
    map = {}
    for line in lines:
        chunks = line.split(' -> ')
        map[chunks[0]] = [f"{chunks[0][0] + chunks[1]}", f"{chunks[1] + chunks[0][1]}"]

    return map

def runRxn(input, map):
    finalChar = input[-1]
    pairs = {}
    for x in range(len(input) -1):
        if input[x:x+2] in pairs:
            pairs[input[x:x+2]] += 1
        else:
            pairs[input[x:x+2]] = 1

    for i in range(40):
        pairs = polymerize(pairs, map)
    
    ans = {}
    for k,v in pairs.items():
        if k[0] in ans:
            ans[k[0]] += v
        else:
            ans[k[0]] = v
    
    ans[finalChar] += 1

    all_vals = ans.values()

    print(max(all_vals) - min(all_vals))



def polymerize(pairs, map):
    
    newPairs = {}
    
    for OGpair, v in pairs.items():
        if OGpair in map:
            for rxn in map[OGpair]:
                if rxn in newPairs:
                    newPairs[rxn] += v
                else:
                    newPairs[rxn] = v
        else:
            if OGpair in newPairs:
                newPairs[OGpair] += v
            else:
                newPairs[OGpair] = v
    
    return newPairs
main()

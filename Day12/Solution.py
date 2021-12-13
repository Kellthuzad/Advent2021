from copy import deepcopy

def main():
    filehandle = open("./Day12/input.txt")
    lines = []

    for line in filehandle:
        lines.append(line.strip())
    
    connections = parse(lines)
    answer = search(connections, set(), 'start', [], False)

    answer = sorted(answer)

    print(len(answer))

def parse(lines):
    connections = {}

    for line in lines:
        chunks = line.split('-')
        if chunks[0] not in connections:
            connections[chunks[0]] = set()
            connections[chunks[0]].add(chunks[1])
        else:
            connections[chunks[0]].add(chunks[1])
        if chunks[1] not in connections:
            connections[chunks[1]] = set()
            connections[chunks[1]].add(chunks[0])
        else:
            connections[chunks[1]].add(chunks[0])

    return connections
                
def search(connections, visited, current, currentPath, doubleUsed):
    newv = deepcopy(visited) 
    allPaths = []
    if current.islower():
        newv.add(current)

    currentPath.append(current)
    if current == 'end':
        return [currentPath]

    for direction in connections[current]:
        
        if direction not in visited:
            newPath = deepcopy(currentPath)
            allPaths.extend(search(connections, newv, direction, newPath, doubleUsed))
            
        elif not doubleUsed and direction != 'start' and direction != 'end':
            newPath = deepcopy(currentPath)
            allPaths.extend(search(connections, newv, direction, newPath, True))


    
    return allPaths

main()
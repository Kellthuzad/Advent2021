import heapq

def main():
    filehandle = open("./Day15/input.txt")
    lines = []

    for line in filehandle:
        lines.append(line.strip())
    
    grid = parse(lines)
    print(dijkstras(grid))

def dijkstras(grid):
    visited = set()
    paths = [(0, (0,0))]
    while paths:
        item = heapq.heappop(paths)
        val = item[0]
        y,x = item[1]
        if (y,x) in visited:
            continue
        visited.add((y,x))
        if x == (len(grid[0])*5) -1  and y == (len(grid)*5) -1:
            return val
        
        for dy,dx in [(1,0),(-1,0),(0,1),(0,-1)]: 
            if 0 <= x+dx < len(grid[0])*5 and 0 <= y+dy < len(grid)*5 and (y+dy, x+dx) not in visited:
                modX = x+dx
                modY = y+dy
                gridVal = hereThereBeDragons(modX, modY, grid)

                heapq.heappush(paths, (val+ gridVal, (y+dy,x+dx)))

def parse(lines):
    grid = []

    for line in lines:
        row = []
        for char in line:
            row.append(int(char))
        grid.append(row)

    return grid

def hereThereBeDragons(modX, modY, grid):
    modifier = 0
    if modX >= len(grid[0]):
        modifier += modX//len(grid[0])
        modX = modX % len(grid[0])
    if modY >= len(grid):
        modifier += modY//len(grid)
        modY = modY % len(grid)

    gridVal = grid[modY][modX] + modifier
    if gridVal > 9:
        gridVal +=1
        gridVal = gridVal % 10
    return gridVal

main()

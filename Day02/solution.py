
def main():
    filehandle = open("./Day02/input.txt")
    lines = []
    x = 0
    y = 0
    for line in filehandle:
        lines.append(line)
        
    command(lines)
        

def command(input):
    x = 0
    y = 0
    aim = 0

    for line in input:
        parsed = line.split(' ')

        if parsed[0] == "forward":
            x += int(parsed[1])
            y += (aim * int(parsed[1]))
        elif parsed[0] == "down":
            aim += int(parsed[1])
        elif parsed[0] == "up":
            aim -= int(parsed[1])

    print(x*y)

main()
    
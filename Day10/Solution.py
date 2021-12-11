def main():
    filehandle = open("./Day10/input.txt")
    lines = []

    for line in filehandle:
        lines.append(line.strip())
    
    stackItIncomplete(lines)

def stackItCorrupt(lines):
    pointMap = {')':3,']': 57, '}': 1197, '>': 25137 }
    totalScore = 0

    for line in lines:
        stack = []
        for char in line:
            if char == '(' or char == '[' or char == '{' or char == '<':
                stack.append(char)
            else:
                opener = stack.pop(-1)
                if (opener == '(' and char != ')') or (opener == '[' and char != ']') or (opener == '{' and char != '}') or (opener == '<' and char != '>'):
                    totalScore += pointMap[char]
                    print(char)
                    break
    print(totalScore)   

def stackItIncomplete(lines):
    pointMap = {')':1,']': 2, '}': 3, '>': 4 }
    scores = []

    for line in lines:
        stack = []
        corrupt = False
        for char in line:
            if char == '(' or char == '[' or char == '{' or char == '<':
                stack.append(char)
            else:
                opener = stack.pop(-1)
                if (opener == '(' and char != ')') or (opener == '[' and char != ']') or (opener == '{' and char != '}') or (opener == '<' and char != '>'):
                    corrupt = True
                    break
            
        if len(stack) > 0 and not corrupt:
            chars = findRemainingChars(stack)
            score = 0
            for char in chars:
                score *= 5
                score += pointMap[char]
            scores.append(score)
    scores = sorted(scores)
    print(scores[len(scores)//2])

def findRemainingChars(stack):
    returnVal = []
    while len(stack) > 0:
        char = stack.pop(-1)

        if char == '(':
            returnVal.append(')')
        elif char == '[':
            returnVal.append(']')
        elif char == '{':
            returnVal.append('}')
        elif char == '<':
            returnVal.append('>')
    return returnVal

main()

def main():
    filehandle = open("./Day07/input.txt")
    lines = []

    total = 0

    for line in filehandle:
        lines.append(line.strip())
       
    tempNums = lines[0].split(',')
    nums = []

    for num in tempNums:
        nums.append(int(num))

    # print(f'answer:{ans}')
    dumbWay(nums)
   

sentScore = 999999999999999

def dumbWay(input):
    bestScore = 99999999999999999999999
    winningPosition = 0
    i = min(input)
    while i < max(input):
        score = 0
        for num in input:
            n = abs(num - i)
            numerator = n * (n + 1)
            score += numerator//2
        if score < bestScore:
            bestScore = score
            winningPosition = i
        i += 1
    
    print(bestScore)
    print(f'winning Position: {winningPosition}')
    print(f'average of input: {sum(input)/len(input)}')
        
    
    

main()

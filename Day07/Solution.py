
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

    ans = bSearch(nums, max(nums), min(nums), sentScore)
    print(f'answer:{ans}')
    dumbWay(nums)
   

sentScore = 999999999999999


def bSearch(input, upper, lower, bestScore):
    print(upper)
    print(lower)
    mid = (upper + lower)// 2
    
    score = 0
    scores = []
    for num in input:
        score += abs(num - mid)

    scores.append(score)
    print(f'mid:{mid}')
    print(f'score:{score}')
    
    if upper > (lower +1) and score < bestScore:
         scores.append(bSearch(input, upper, mid, score))
         scores.append(bSearch(input, mid, lower, score))

    return min(scores)

def dumbWay(input):
    bestScore = 99999999999999999999999
    i = min(input)
    while i < max(input):
        score = 0
        for num in input:
            n = abs(num - i)
            numerator = n * (n + 1)
            score += numerator//2
        if score < bestScore:
            bestScore = score
        i += 1
    
    print(bestScore)
        
    
    

main()
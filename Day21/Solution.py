from itertools import product
from functools import lru_cache


probMap = None
def main():
    global probMap

    probMap = buildMap()
    print(probMap)
    #playDice(7,9)
    print(playDice(4,8,0,0,1))

def buildMap():
    nums = {}
    for a, b, c in product((1, 2, 3), repeat=3):
        total = a + b + c
        if total in nums:
            nums[total] += 1
        else:
            nums[total] = 1
    
    return nums


@lru_cache(None)
def playDice(pos, scores, universeCount, playerTurn):
    global probMap
    player1Wins = 0
    player2Wins = 0
    temppos = pos
    tempscore = score[playerTurn]
    tempUniCount = 1

    tempUniCount *= probMap[num]
    pos = findPosition(temppos1, num)
        += temppos1
    if tempscore1 >= 21:
        return tempUniCount * universeCount, 0
    
    newWins1, newWins2 = playDice(temppos1,temppos2, tempscore1, tempscore2, tempUniCount * universeCount)
    player1Wins += newWins1
    player2Wins += newWins2

    temppos1 = pos1
    temppos2 = pos2
    tempscore1 = score1
    tempscore2 = score2
    tempUniCount = 1
    
    return player1Wins, player2Wins





def rollDiceThrice(i):
    rolls = 0
    for j in range(3):
        if i % 100 == 0:
            rolls += 100
        else:
            rolls += i % 100
        i += 1
    
    return rolls, i

        
def findPosition(pos, sumOfRolls):
    moveNum = sumOfRolls % 10
    pos += moveNum

    if pos > 10:
        pos = pos % 10
    
    return pos

main()

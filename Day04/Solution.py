def main():
    filehandle = open("./Day04/input.txt")
    lines = []

    for line in filehandle:
        lines.append(line.strip())

    boards = parseBoards(lines)
    playBingo(boards, lines[0])
    
    

def parseBoards(input):

    boards = []
    board = []
    for i in range(2,len(input),1):
        if input[i] == '':
            boards.append(board)
            board = []
        else:
            line = []
            for num in input[i].split():
                line.append(int(num))
            board.append(line)
    boards.append(board)
    return boards
    
def playBingo(boards, input):
    
    for num in input.split(','):
        for x in range(len(boards)):
            if boards[x][0][0] != -42069:
                board, winner, score = strikeAndCalculateWin(int(num), boards[x])
                if winner:
                    print(num)
                    print(score)
    
    

def strikeAndCalculateWin(num, board):
    cX = -1
    cY = -1
    for y in range(len(board)):
        for x in range(len(board)): 
            if board[y][x] == num:
                board[y][x] = -1
                cX = x
                cY = y
                break
        if cY >= 0:
            break
    winner = True
    for x in range(len(board)):
        if board[cY][x] > 0:
            winner = False
            break
    if winner:
        score = calcScore(num, board)
        board[0][0] = -42069
        return board, True, score

    winner = True
    for y in range(len(board)):
        if  board[y][cX] > 0:
            winner = False
            break
    if winner:
        score = calcScore(num, board)
        board[0][0] = -42069
        return board, True, score

    return board, False, 0

def calcScore(num, board):
    score = 0
    for y in board:
        for x in y:
            if x > 0:
                score += x

    return score * num

            

              

main()
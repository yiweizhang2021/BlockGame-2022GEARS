import GameBoard, numpy as np
def checkBoard(board, score):
    count = 0
    # Check rows
    for i in range(10):
        for j in range(10):
            if board[i][j] !=1.0:
                break
            elif j == 9:
                count +=1
    # Columns
    for i in range(10):
        for j in range(10):
            if board[j][i] !=1.0:
                break
            elif j == 9:
                count +=1
    if count == 5:
        score+=count*10 + 200
    elif count ==6:
        score += count * 10 + 300
    else:
        score += count * 10
    return score
def main():
    board = GameBoard.GameBoard()
    tempBoard = np.zeros((10, 10))
    for i in range(3):
        for j in range(10):
            tempBoard[i][j] = 1.0
            tempBoard[j][i] = 1.0
    print(board)
if __name__ == "__main__":
    main()
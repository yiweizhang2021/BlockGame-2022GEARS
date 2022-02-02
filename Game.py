import numpy as np, random
from GameBoard import GameBoard
class Game:
    def __init__(self):
        # 19
        self.possibleMoves = [random.randint(0,18), random.randint(0,18), random.randint(0,18)]
        self.board = GameBoard()
        self.moves = self.getMoves()
    def __getitem__(self, tup):
        return self.board[tup]
    def __setitem__(self, key, value):
        x,y = key
        self.board[x,y] = value
    def __str__(self):
        return str(self.board)
    def checkIndex(self, x, y):
        return self.board[x,y]
    def getBoard(self):
        return self.board
    def getMoveIDs(self):
        return self.possibleMoves
    def checkLose(self):
        results = []
        for entry in self.possibleMoves:
            entryResult = False
            for i in range(10):
                for j in range(10):
                    if entry == 0:
                        tempResult = self.board.checkThreeByThree((i,j))
                        if tempResult:
                            entryResult = True
                    elif entry == 1:
                        tempResult = self.board.checkTwoByTwo((i, j))
                        if tempResult:
                            entryResult = True
                    elif entry == 2:
                        tempResult = self.board.checkTwoByOne((i, j))
                        if tempResult:
                            entryResult = True
                    elif entry == 3:
                        tempResult = self.board.checkThreeByOne((i, j))
                        if tempResult:
                            entryResult = True
                    elif entry == 4:
                        tempResult = self.board.checkFourByOne((i, j))
                        if tempResult:
                            entryResult = True
                    elif entry == 5:
                        tempResult = self.board.checkFiveByOne((i, j))
                        if tempResult:
                            entryResult = True
                    elif entry == 6:
                        tempResult = self.board.checkOneByOne((i, j))
                        if tempResult:
                            entryResult = True
                    elif entry == 7:
                        tempResult = self.board.checkOneByTwo((i, j))
                        if tempResult:
                            entryResult = True
                    elif entry == 8:
                        tempResult = self.board.checkOneByThree((i, j))
                        if tempResult:
                            entryResult = True
                    elif entry == 9:
                        tempResult = self.board.checkOneByFour((i, j))
                        if tempResult:
                            entryResult = True
                    elif entry == 10:
                        tempResult = self.board.checkOneByFive((i, j))
                        if tempResult:
                            entryResult = True
                    elif entry == 11:
                        tempResult = self.board.checkStep1((i, j))
                        if tempResult:
                            entryResult = True
                    elif entry == 12:
                        tempResult = self.board.checkStep2((i, j))
                        if tempResult:
                            entryResult = True
                    elif entry == 13:
                        tempResult = self.board.checkStep3((i, j))
                        if tempResult:
                            entryResult = True
                    elif entry == 14:
                        tempResult = self.board.checkStep4((i, j))
                        if tempResult:
                            entryResult = True
                    elif entry == 15:
                        tempResult = self.board.checkl1((i, j))
                        if tempResult:
                            entryResult = True
                    elif entry == 16:
                        tempResult = self.board.checkl2((i, j))
                        if tempResult:
                            entryResult = True
                    elif entry == 17:
                        tempResult = self.board.checkl3((i, j))
                        if tempResult:
                            entryResult = True
                    elif entry == 18:
                        tempResult = self.board.checkl4((i, j))
                        if tempResult:
                            entryResult = True
            results.append(entryResult)
        if False in results:
            return True
        else:
            return False
    def printBoard(self):
        print(self.board)


    def getMoves(self):
        Moves = []
        for i in self.possibleMoves:
            if i == 0:
                Moves.append("3x3")
            elif i == 1:
                Moves.append("2x2")
            elif i == 2:
                Moves.append("2x1")
            elif i == 3:
                Moves.append("3x1")
            elif i == 4:
                Moves.append("4x1")
            elif i == 5:
                Moves.append("5x1")
            elif i == 6:
                Moves.append("1x1")
            elif i == 7:
                Moves.append("1x2")
            elif i == 8:
                Moves.append("1x3")
            elif i == 9:
                Moves.append("1x4")
            elif i == 10:
                Moves.append("1x5")
            elif i == 11:
                Moves.append("Step1")
            elif i == 12:
                Moves.append("Step2")
            elif i == 13:
                Moves.append("Step3")
            elif i == 14:
                Moves.append("Step4")
            elif i == 15:
                Moves.append("L1")
            elif i == 16:
                Moves.append("L2")
            elif i == 17:
                Moves.append("L3")
            elif i == 18:
                Moves.append("L4")
        self.moves = Moves
        return self.moves
    def move(self, id, tup):
        x,y = tup
        if self.checkLose() == True:
            print("You have lost!")
            return

        print("Moves:", self.getMoves())
        self.board.printBoard()
        if id not in self.possibleMoves:
            return
            #print("Invalid block! Try again")
            #self.move()
        #x = int(input("Which row would you like to place this block on (The middle of the block)? "))
        #y = int(input("Which column would you like to place this block on (The middle of the block)? "))
        if x not in range(0,10) or y not in range(0,10):
            print("\nOut of range! Try again.\n")
            #self.move()
        formattedLocation = (x,y)
        self = self.place(id,tup)
        # if isinstance(result, bool):
        #     if result == False:
        #         print("\nUnable to place that here! Try again.\n")
                #self.move()
        self.possibleMoves.remove(id)
        if len(self.possibleMoves) == 0:
            self.possibleMoves = [random.randint(0,18), random.randint(0,18), random.randint(0,18)]
        self.board.updateBoard()
        self.getMoves()
        #self.move()
    def updateMoves(self):
        self.possibleMoves = [random.randint(0,18), random.randint(0,18), random.randint(0,18)]
    def update(self):
        self.board = self.board.updateBoard()
    def place(self, blockID, location):
        i = blockID
        if i == 0:
            return self.board.threeByThree(location)
        elif i == 1:
            return self.board.twoByTwo(location)
        elif i == 2:
            return self.board.twoByOne(location)
        elif i == 3:
            return self.board.threeByOne(location)
        elif i == 4:
            return self.board.fourByOne(location)
        elif i == 5:
            return self.board.fiveByOne(location)
        elif i == 6:
            return self.board.oneByOne(location)
        elif i == 7:
            return self.board.oneByTwo(location)
        elif i == 8:
            return self.board.oneByThree(location)
        elif i == 9:
            return self.board.oneByFour(location)
        elif i == 10:
            return self.board.oneByFive(location)
        elif i == 11:
            return self.board.step1(location)
        elif i == 12:
            return self.board.step2(location)
        elif i == 13:
            return self.board.step3(location)
        elif i == 14:
            return self.board.step4(location)
        elif i == 15:
            return self.board.l1(location)
        elif i == 16:
            return self.board.l2(location)
        elif i == 17:
            return self.board.l3(location)
        elif i == 18:
            return self.board.l4(location)
    def startGame(self):
        self.move()
def main():
    newGame = Game()
    newGame.move()
    # newGame.place(1,(3,3))
    # newGame.printBoard()
if __name__ == "__main__":
    main()
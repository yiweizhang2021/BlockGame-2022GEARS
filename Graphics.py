import Game, pygame, os, random, numpy as np, time
#import pandas as pd
def placeOptions(gameInstance: Game):
    grid1 = np.zeros((5,5))
    grid2 = np.zeros((5, 5))
    grid3 = np.zeros((5, 5))
    grids = [grid1, grid2, grid3]
    for gridnum, id in enumerate(gameInstance.getMoveIDs()):
        if id == 0:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    grids[gridnum][i + 2][j + 2] = 1.0
        elif id == 1:
            for i in range(-1, 1):
                for j in range(-1, 1):
                   grids[gridnum][i + 2][j + 2] = 1.0
        elif id == 2:
            for i in range(-1, 1):
               grids[gridnum][2 + i][2] = 1.0
        elif id == 3:
            for i in range(-1, 2):
                grids[gridnum][2 + i][2] = 1.0
        elif id == 4:
            for i in range(-2, 2):
               grids[gridnum][2 + i][2] = 1.0
        elif id == 5:
            for i in range(-2, 3):
                grids[gridnum][2 + i][2] = 1.0
        elif id == 6:
            grids[gridnum][2][2] = 1.0
        elif id == 7:
            for i in range(-1, 1):
                grids[gridnum][2][2 + i] = 1.0
        elif id == 8:
            for i in range(-1, 2):
                grids[gridnum][2][2 + i] = 1.0
        elif id == 9:
            for i in range(-2, 2):
                grids[gridnum][2][2 + i] = 1.0
        elif id == 10:
            for i in range(-2, 3):
                grids[gridnum][2][2 + i] = 1.0
        elif id == 11:
            grids[gridnum][2][2] = 1.0
            grids[gridnum][2 + 1][2] = 1.0
            grids[gridnum][2][2 + 1] = 1.0
        elif id == 12:
            grids[gridnum][2][2] = 1.0
            grids[gridnum][2 - 1][2] = 1.0
            grids[gridnum][2][2 + 1] = 1.0
        elif id == 13:
            grids[gridnum][2][2] = 1.0
            grids[gridnum][2 + 1][2] = 1.0
            grids[gridnum][2][2 - 1] = 1.0
        elif id == 14:
            grids[gridnum][2][2] = 1.0
            grids[gridnum][2 - 1][2] = 1.0
            grids[gridnum][2][2 - 1] = 1.0
        elif id == 15:
            grids[gridnum][2][2] = 1.0
            grids[gridnum][3][2] = 1.0
            grids[gridnum][2][3] = 1.0
            grids[gridnum][4][2] = 1.0
            grids[gridnum][2][4] = 1.0
        elif id == 16:
            grids[gridnum][2][2] = 1.0
            grids[gridnum][1][2] = 1.0
            grids[gridnum][2][3] = 1.0
            grids[gridnum][0][2] = 1.0
            grids[gridnum][2][4] = 1.0
        elif id == 17:
            grids[gridnum][2][2] = 1.0
            grids[gridnum][3][2] = 1.0
            grids[gridnum][2][1] = 1.0
            grids[gridnum][4][2] = 1.0
            grids[gridnum][2][0] = 1.0
        elif id == 18:
            grids[gridnum][2][2] = 1.0
            grids[gridnum][1][2] = 1.0
            grids[gridnum][2][1] = 1.0
            grids[gridnum][0][2] = 1.0
            grids[gridnum][2][0] = 1.0
    return grids

def startGame(gameInstance: Game):
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (0,0,255)

    WIDTH = 36
    HEIGHT = 36
    MARGIN = 2

    grid = []
    for row in range(10):
        grid.append([])
        for column in range(10):
            grid[row].append(0)
    pygame.init()

    WINDOW_SIZE = [390, 844]

    screen = pygame.display.set_mode(WINDOW_SIZE)

    pygame.display.set_caption("Block Game")

    done = False

    close = pygame.time.Clock()

    # Display score
    font = pygame.font.Font('freesansbold.ttf', 32)

    text = font.render('Score: 0', True, GREEN, BLACK)

    # create a rectangular object for the
    # text surface object
    textRect = text.get_rect()

    # set the center of the rectangular object.
    textRect.center = (WINDOW_SIZE[0] // 2, 75)

    while not done:
        #selected = False
        autoPlay = True
        if autoPlay:
            # df = gameInstance.getPossibleStates()
            df = gameInstance.deepSearch(.05)
            print(df)
            evalSort = df.sort_values('eval', ascending=False)
            if len(evalSort) == 0:
                evalSort = gameInstance.getPossibleStates()
            for i in range(len(evalSort)):
                block = evalSort.iloc[i]['BlockID']
                blockLocation = evalSort.iloc[i]['Location']
                if gameInstance.place(block,blockLocation):
                    gameInstance.update()
                    gameInstance.possibleMoves.remove(block)
                    time.sleep(.5)
                    break
            # id = df['eval'].idxmax()
            # maxentry = df.iloc[df['eval'].idxmax()]
            # print(maxentry)
            # print(gameInstance.board)
            # x, y = maxentry['Location']
            # if gameInstance.place(maxentry['BlockID'], (x, y)):
            #     gameInstance.update()
            #     gameInstance.possibleMoves.remove(maxentry['BlockID'])
            if len(gameInstance.possibleMoves) == 0:
                gameInstance.updateMoves()
            if gameInstance.checkLose() == True:
                # time.sleep(25)
                print("You have lost! Final score:",gameInstance.getBoard().getScore())
                time.sleep(5)
                done = True

            placeOptions(gameInstance)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                try:
                    #if selected == False:
                    pos = pygame.mouse.get_pos()
                    horizontal = pos[0]
                    vertical = pos[1]
                    column = (pos[0] - 4) // (WIDTH + MARGIN)
                    row = (pos[1] - 100) // (HEIGHT + MARGIN)
                    #print(horizontal, vertical)



                    chosen = False
                    if chosen == False:
                        if (horizontal <= 92) and (516 <= vertical <= 588):
                            # Place 1st block
                            id = gameInstance.getMoveIDs()[0]
                            print("Selected 0")
                            chosen = True
                        elif (horizontal <= 237) and (516 <= vertical <= 588):
                            # Place 2nd block
                            id = gameInstance.getMoveIDs()[1]
                            print("Selected 1")
                            chosen = True
                        elif (horizontal <= 382) and (516 <= vertical <= 588):
                            # Place 3rd block
                            id = gameInstance.getMoveIDs()[2]
                            print("Selected 2")
                            chosen = True
                    if vertical < 516:
                        print(gameInstance.possibleMoves, id)
                        if gameInstance.place(id,(row,column)) and id in gameInstance.possibleMoves:
                            gameInstance.possibleMoves.remove(id)
                            id = None
                        if len(gameInstance.possibleMoves) == 0:
                            gameInstance.updateMoves()
                            id = None
                        gameInstance.update()
                    if gameInstance.checkLose() == True:
                        print("You have lost!")
                        done = True
                    placeOptions(gameInstance)
                    # pos = pygame.mouse.get_pos()
                    # column = (pos[0] - 4) // (WIDTH + MARGIN)
                    # row = (pos[1] - 100) // (HEIGHT + MARGIN)
                    #gameInstance[row,column] = 1
                except IndexError:
                    continue


        screen.fill(BLACK)
        scoreText = str(gameInstance.getBoard().getScore())
        text = font.render('Score: ' + scoreText, True, GREEN, BLACK)
        screen.blit(text, textRect)
        for row in range(10):
            for column in range(10):
                color = WHITE
                if gameInstance.checkIndex(row, column) == 1.0:
                    color = GREEN
                pygame.draw.rect(screen,
                                 color,
                                 [(MARGIN + WIDTH) * column + MARGIN + 4,
                                  (MARGIN + HEIGHT) * row + MARGIN + 100,
                                  WIDTH,
                                  HEIGHT])
        WIDTH1 = 16
        HEIGHT1 = 16
        MARGIN1 = 2
        moveGrids = placeOptions(gameInstance)
        for row in range(5):
            for column in range(5):
                color = WHITE
                if moveGrids[0][row][column] == 1:
                    color = GREEN
                if row == 2 and column == 2:
                    color = RED
                pygame.draw.rect(screen,
                                 color,
                                 [(MARGIN1 + WIDTH1) * column + MARGIN1 + 4,
                                  (MARGIN1 + HEIGHT1) * row + MARGIN1 + 500,
                                  WIDTH1,
                                  HEIGHT1])
        WIDTH2 = 16
        HEIGHT2 = 16
        MARGIN2 = 2
        for row in range(5):
            for column in range(5):
                color = WHITE
                if moveGrids[1][row][column] == 1:
                    color = GREEN
                if row == 2 and column == 2 and len(gameInstance.getMoveIDs()) >= 2:
                    color = RED
                pygame.draw.rect(screen,
                                 color,
                                 [(MARGIN2 + WIDTH2) * column + MARGIN2 + 149,
                                  (MARGIN2 + HEIGHT2) * row + MARGIN2 + 500,
                                  WIDTH2,
                                  HEIGHT2])
        WIDTH3 = 16
        HEIGHT3 = 16
        MARGIN3 = 2
        for row in range(5):
            for column in range(5):
                color = WHITE
                if moveGrids[2][row][column] == 1:
                    color = GREEN
                if row == 2 and column == 2 and len(gameInstance.getMoveIDs()) >= 3:
                    color = RED
                pygame.draw.rect(screen,
                                 color,
                                 [(MARGIN3 + WIDTH3) * column + MARGIN3 + 294,
                                  (MARGIN3 + HEIGHT3) * row + MARGIN3 + 500,
                                  WIDTH3,
                                  HEIGHT3])
        close.tick(60)
        pygame.display.flip()
    pygame.quit()
testGame = Game.Game()
startGame(testGame)

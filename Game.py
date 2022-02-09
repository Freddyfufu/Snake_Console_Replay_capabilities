import random
import copy

class Game:
    def __init__(self):
        self.score = 0
        self.boardLen = 30
        self.snake = [(10, 10)]
        self.appleX = None
        self.appleY = None
        self.keyPressed = None
        self.gameBoard = self.createEmptyGameboard()



    def showGameboard(self):
        print("+" + (self.boardLen) * "-" + "+")
        for row in self.gameBoard:
            print("|", end="")
            for e, column in enumerate(row):
                print(column, end="") if e != (len(row) - 1) else print(column + "|")
        print("+" + (self.boardLen) * "-" + "+")

    def createEmptyGameboard(self) -> list:
        board = []
        for i in range(self.boardLen):
            cache = []
            for n in range(self.boardLen):
                cache.append(" ")
            board.append(cache)
        return board

    def getGameboard(self):
        return copy.deepcopy(self.gameBoard)

    def resetField(self,x, y):
        self.gameBoard[x][y] = " "

    def istKante(self,y, x):
        maxC = self.boardLen - 1
        return (y == maxC and x == 0) or (x == maxC and y == 0) or (x == 0 and y == 0) or x == maxC and y == maxC

    def placeRandomApple(self):
        while True:
            randomRow = random.randint(0, self.boardLen - 1)
            randomColumn = random.randint(0, self.boardLen - 1)
            if (randomRow, randomColumn) in self.snake or self.istKante(randomRow, randomColumn):
                continue
            self.gameBoard[randomRow][randomColumn] = "A"
            self.appleX,self.appleY = randomRow,randomColumn
            return randomRow, randomColumn

    def getApple(self):
        return self.appleX, self.appleY

    def blitSnake(self):
        for i in range(len(self.gameBoard)):
            for c in range(len(self.gameBoard)):
                if (i, c) in self.snake:
                    self.gameBoard[i][c] = "X"
                elif self.gameBoard[i][c] == "A":
                    pass
                else:
                    self.gameBoard[i][c] = " "

    def getHeadCoords(self):
        return self.snake[-1]

    def executeButtonPress(self,keyPressed):
        if keyPressed == None:
            return
        if keyPressed == "w":
            x, y = self.getHeadCoords()
            del self.snake[0]
            self.snake.append((x - 1, y))
            self.resetField(x, y)
            ### entferne schwanz
            self.lastPressed = "w"
        elif keyPressed == "d":
            x, y = self.getHeadCoords()
            del self.snake[0]
            self.snake.append((x, y + 1))
            self.resetField(x, y)
            ### entferne schwanz
            self.lastPressed = "d"
        elif keyPressed == "s":
            x, y = self.getHeadCoords()
            del self.snake[0]
            self.snake.append((x + 1, y))
            self.resetField(x, y)
            ### entferne schwanz
            self.lastPressed = "s"
        elif keyPressed == "a":
            x, y = self.getHeadCoords()
            del self.snake[0]
            self.snake.append((x, y - 1))
            self.resetField(x, y)
            ### entferne schwanz
            self.lastPressed = "a"

    def getTail(self):
        return self.snake[0]

    def verlaengereSchlange(self,lastPressed):
        if lastPressed == "w":
            newCoords = self.getHeadCoords()

            self.snake.append((newCoords[0] - 1, newCoords[1]))
            self.appleX, self.appleY = self.placeRandomApple()
        elif lastPressed == "d":
            newCoords = self.getHeadCoords()

            self.snake.append((newCoords[0], newCoords[1] + 1))
            self.appleX, self.appleY = self.placeRandomApple()
        elif lastPressed == "s":
            newCoords = self.getHeadCoords()

            self.snake.append((newCoords[0] + 1, newCoords[1]))
            self.appleX, self.appleY = self.placeRandomApple()
        elif lastPressed == "a":
            newCoords = self.getHeadCoords()

            self.snake.append((newCoords[0], newCoords[1] - 1))
            self.appleX, self.appleY = self.placeRandomApple()

    def resetBoard(self):
        self.gameBoard = self.createEmptyGameboard()
        self.appleX, self.appleY = self.placeRandomApple()
        self.snake = [(10, 10)]
        self.speed = 10
        self.score = 0

    def upScore(self):
        self.score += 1

    def isLost(self):
        x, y = self.getHeadCoords()
        dupl = [a for a in self.snake if self.snake.count(a) > 1]
        return x < 0 or x > self.boardLen - 1 or y < 0 or y > self.boardLen - 1 or len(dupl) > 1

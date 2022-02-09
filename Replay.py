import time

import Helps


class Replay:
    def __init__(self):
        self.gameList = []

    def addFrame(self,frame):
        self.gameList.append(frame)

    def showLastGame(self):
        for frame in self.gameList:
            self.showGameboard(frame)
            time.sleep(0.1)
            Helps.clear()

    def resetGameList(self):
        self.gameList = []

    def showGameboard(self,board):
        print("+" + (30) * "-" + "+")
        for row in board:
            print("|", end="")
            for e, column in enumerate(row):
                print(column, end="") if e != (len(row) - 1) else print(column + "|")
        print("+" + (30) * "-" + "+")
import pickle
import datetime
import time

import Helps


class BinaryPersistancy:
    def __init__(self,path):
        self.path = path
        try:
            self.userInfo = self.readUserInfoFromBinary()
        except:
            self.userInfo = list()
        self.name = self.getLastPlayer()
        self.gameReplay = None


    def setName(self,_name):
        self.name = _name

    def getName(self):
        return self.name


    def getLastPlayer(self):
        try:
            return self.userInfo[-1]["username"]
        except:
            return None

    def resetUserInfo(self):
        self.userInfo = list()


    def addData(self,_score):
        timestamp = datetime.datetime.now()
        timestamp = timestamp.strftime("%Y/%m/%d %H:%M:%S")
        data = {"username":self.name,
                "score":_score,
                "timestamp":timestamp,
                "replay":self.gameReplay
                }
        self.userInfo.append(data)
        self.writeUserInfoIntoBinary()

    def readUserInfoFromBinary(self):
        try:
            with open(self.path, "rb") as file:
                data = pickle.load(file)
                return data
        except EOFError:
            print("Noch nichts gespeichert!")
            print(self.userInfo)
            self.userInfo = list()
            print(self.userInfo)

    def writeUserInfoIntoBinary(self):
        with open(self.path, "wb") as file:
            pickle.dump(self.userInfo, file)

    def getHighscore(self):
        try:
            return max([x["score"] for x in self.userInfo])
        except:
            print("Noch kein Score gespeichert")

    def setGameReplay(self,replay):
        self.gameReplay = replay

    def resetGameplay(self):
        self.gameReplay = None

    def showGame(self,_index):
        lastgame = self.userInfo[_index]["replay"]
        spieler = self.userInfo[_index]["username"]
        timestamp = self.userInfo[_index]["timestamp"]
        score = self.userInfo[_index]["score"]
        for frame in lastgame:
            self._showGameboard(frame)
            print(f"Spieler: {spieler}\nScore: {score}\n{timestamp}")
            time.sleep(0.1)
            Helps.clear()

    def _showGameboard(self,board):
        print("+" + (30) * "-" + "+")
        for row in board:
            print("|", end="")
            for e, column in enumerate(row):
                print(column, end="") if e != (len(row) - 1) else print(column + "|")
        print("+" + (30) * "-" + "+")
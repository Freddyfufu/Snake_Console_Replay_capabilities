
import sys
import Commands
from Game import Game
import Helps
import Replay
import UserInput
from Persistancy import binaryPers

pers = binaryPers.BinaryPersistancy("Persistancy/binary.ser")
replay = Replay.Replay()
game = Game()
replay.addFrame(game.gameBoard)


def calculateStart():
    if pers.name == None:
        pers.name = input("Willkommen! Wie heißt du?\n")
    while True:
        eingabe = input("Drücke 'start' zum starten oder 'commands' für andere Befehle!\n")
        if eingabe == "start":
            break
        elif eingabe == "commands":
            Commands.showCommands()
        elif eingabe == "changename":
            pers.name = input("Name?").title()
        elif eingabe == "quit":
            sys.exit()
        elif eingabe == "replay":
            pers.showGame(int(input("Wieviele Spiele zurück? (zB -3; -1 für das letzte)")))


### start loop zur abfrage der wünsche des users
calculateStart()

game.placeRandomApple()

highscore = pers.getHighscore()

count = 0
while True:
    print(f"Hey {pers.getName()}!\n")
    print(f"Score: {game.score}\n")
    print(f"Highscore: {highscore}")

    dir = UserInput.getDirectionFromUser()
    game.executeButtonPress(dir)
    Helps.clear()
    game.blitSnake()
    game.showGameboard()
    replay.addFrame(game.getGameboard())
    count += 1
    ### apfel aufgehoben
    if game.getHeadCoords() == game.getApple():
        game.upScore()
        game.verlaengereSchlange(game.lastPressed)
        replay.addFrame(game.getGameboard())

    if game.isLost():
        pers.setGameReplay(replay.gameList)
        eingabe = None
        alterHighscore = highscore
        pers.addData(game.score)
        highscore = pers.getHighscore()
        pers.resetGameplay()
        replay.resetGameList()
        apples = "Apfel" if game.score == 1 else "Äpfel"

        try:
            if highscore > alterHighscore:
                print(f"NEUER HIGHSCORE!!!! Du hast {game.score} {apples} eingesammelt\n")
        finally:
            print(f"Leider verloren! Du hast {game.score} {apples} eingesammelt\n")

        eingabe = input("Drücke Enter\n")

        while True:
            eingabe = input("Nochmal spielen? (y) Kommandos (commands)\n")
            if eingabe == "y":
                game.resetBoard()
                break
            elif eingabe == "commands":
                Commands.showCommands()
            elif eingabe == "changename":
                pers.name = input("Wie lautet dein Name?\n").title()
                game.resetBoard()
            elif eingabe == "quit":
                sys.exit()
            elif eingabe == "replay":
                pers.showGame(int(input("Wieviele Spiele zurück? (zB -3; -1 für das letzte)")))
              

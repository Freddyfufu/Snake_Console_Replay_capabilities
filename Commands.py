commands = {"changename":"zum Wechseln des usernames",
            "quit":"zum Beenden des Programms",
            "replay":"zum schauen eines vergangenen spiels"}

def showCommands():
    for key, value in commands.items():
        print(f"{key}: {value}")
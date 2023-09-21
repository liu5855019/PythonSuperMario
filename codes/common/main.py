
from codes.scene import MainMenu, LoadScreen, Level
from codes.common import Game, consts


def main():
    sceneDict = {
        consts.strMainMenu: MainMenu.MainMenu(),
        consts.strLoadScreen: LoadScreen.LoadScreen(),
        consts.strLevel1: Level.Level()
    }

    game = Game.Game(sceneDict, consts.strLoadScreen)
    game.run()


if __name__ == '__main__':
    main()

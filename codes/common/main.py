
from codes.states import MainMenu, LoadScreen, Level
from codes.common import Game, consts


def main():

    sceneDict = {
        consts.strMainMenu: MainMenu.MainMenu(),
        consts.strLoadScreen: LoadScreen.LoadScreen(),
        consts.strLevel1: Level.Level()
    }

    game = Game.Game(sceneDict, consts.strMainMenu)
    # menu = MainMenu.MainMenu()
    # menu = LoadScreen.LoadScreen()
    # menu = Level.Level()



    game.run()
    return


if __name__ == '__main__':
    main()

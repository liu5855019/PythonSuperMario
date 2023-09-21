
from codes.scene import main_menu, load_screen, level
from codes.common import game, consts


def main():
    sceneDict = {
        consts.str_main_menu: main_menu.MainMenu(),
        consts.str_load_screen: load_screen.LoadScreen(),
        consts.str_level1: level.Level()
    }

    cgame = game.Game(sceneDict, consts.str_load_screen)
    cgame.run()


if __name__ == '__main__':
    main()

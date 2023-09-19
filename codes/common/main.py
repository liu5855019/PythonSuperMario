
import Game
from codes.states import MainMenu

def main():
    game = Game.Game()
    menu = MainMenu.MainMenu()
    game.run(menu)
    return


if __name__ == '__main__':
    main()
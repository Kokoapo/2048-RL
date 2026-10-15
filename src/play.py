from game import Game

if __name__ == "__main__":
    game = Game(4)
    game.print_grid()

    print("")

    game.step((1, 0))
    game.print_grid()

    print("")

    game.step((-1, 0))
    game.print_grid()

    print("")

    game.step((0, 1))
    game.print_grid()

    print("")

    game.step((0, -1))
    game.print_grid()
from game import DynamiteGame
from bot import PowerBot
from states import *


def main():
    points_max = POINTS_MAX
    rounds_max = ROUNDS_MAX

    bot = PowerBot()
    game = DynamiteGame(bot=bot, points_max=points_max, rounds_max=rounds_max)

    print("DYNAMITE")
    print(" Max Points: {0}".format(points_max))
    print(" Max Rounds: {0}".format(rounds_max))
    print()

    while True:
        console_prompt(game)


def console_prompt(game):
    print("Select a move:")
    print("  (R)ock")
    print("  (P)aper")
    print("  (S)cissors")
    print("  (D)ynamite")
    print("  (W)ater Balloon")
    print("  (E)xit Game")

    option = get_str_input("> ", 1, 1).capitalize()

    print()
    if option == EXIT:
        exit()

    elif option in MOVES:
        if game.next_round(option):
            exit()

    else:
        print("Invalid move {0}".format(option))
    print()


def get_str_input(text: str, len_min: int, len_max: int) -> str:
    user_input = None

    while user_input is None:
        try:
            user_input = input(text)

            if not (len_min <= len(user_input) <= len_max):
                user_input = None
        except Exception as e:
            user_input = None
            print("Input must be at least {0} in length".format(len_min))

    return user_input


if __name__ == "__main__":
    main()

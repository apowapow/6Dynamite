from game import DynamiteGame, DynamiteState, MOVES
from bot import PowerBot

EXIT = "E"


def main():
    state = DynamiteState
    bot = PowerBot
    game = DynamiteGame(state=state, bot=bot)

    while True:
        try:
            console_prompt_pick_move(game, state, bot)
        except Exception as e:
            print("Error: {0}".format(str(e)))


def console_prompt_pick_move(game, state, bot):
    print("Select a move:")
    print("  (R)ock")
    print("  (P)aper")
    print("  (S)cissors")
    print("  (D)ynamite")
    print("  (W)ater Balloon")
    print("  (E)xit Game")

    option = get_str_input("> ", 1, 1)

    if option == EXIT:
        game.finish()
        exit()

    elif option in MOVES:
        game.user_move(move=option)
        # todo

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

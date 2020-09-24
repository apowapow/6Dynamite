ROCK = "R"
PAPER = "P"
SCISSORS = "S"
DYNAMITE = "D"
WATER_BALLOON = "W"

MOVES = [
    ROCK,
    PAPER,
    SCISSORS,
    DYNAMITE,
    WATER_BALLOON
]

ROUNDS = "rounds"
P1_BOT = "p1"
P2_USER = "p2"

DYNAMITE_MAX = 100
POINTS_MAX = 1000
ROUNDS_MAX = 2500


class DynamiteGame:

    def __init__(self, state, bot):
        self._state = state
        self._bot = bot

        self._points_bot = 0
        self._points_user = 0
        self._points_accum = 1

    def next_round(self, move_user: str) -> bool:
        if not self._game_finished():
            move_bot = self._bot.make_move(gamestate=self._state.get_game_state())
            winner = self._get_winner(move_bot=move_bot, move_user=move_user)

            if winner is None:  # a draw
                self._points_accum += 1  # add point to accumulator for next round
            else:
                if winner == P1_BOT:  # bot won
                    self._points_bot += self._points_accum

                elif winner == P2_USER:  # user won
                    self._points_user += self._points_accum

                else:
                    raise Exception("Invalid winner {0}".format(winner))

                self._points_accum = 1  # reset points

            self._state.add_round(move_bot=move_bot, move_user=move_user)

            return self._game_finished()
        else:
            return True  # game has finished

    def _game_finished(self) -> bool:
        return self._state.completed_rounds() < ROUNDS_MAX or \
               self._points_bot >= POINTS_MAX or \
               self._points_user >= POINTS_MAX

    def _get_winner(self, move_bot, move_user) -> str:
        pass  # todo

class DynamiteState:

    def __init__(self):
        self._rounds = {ROUNDS: []}
        self._dynamite = DYNAMITE_MAX

    def add_round(self, move_bot: str, move_user: str) -> None:
        self._rounds[ROUNDS].append({
            P1_BOT: move_bot,
            P2_USER: move_user
        })

    def completed_rounds(self) -> int:
        return len(self._rounds[ROUNDS])

    def get_dynamite_left(self) -> int:
        return self._dynamite

    def get_game_state(self) -> dict:
        return self._rounds

    def get_rounds(self) -> list:
        return self._rounds[ROUNDS]

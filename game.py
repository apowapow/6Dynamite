from states import *


class DynamiteGame:

    def __init__(self, bot, points_max=POINTS_MAX, rounds_max=ROUNDS_MAX):
        self.bot = bot
        self._rounds = {ROUNDS: []}

        self._points_bot = 0
        self._points_user = 0
        self._dynamite_user = 100
        self._points_accum = 1

        self._points_max = points_max
        self._rounds_max = rounds_max

    def next_round(self, move_user: str) -> bool:
        if not self.game_finished():

            if move_user == DYNAMITE:
                if self._dynamite_user == 0:
                    print("User has no dynamite left")
                    return False

                self._dynamite_user -= 1

            move_bot = self.bot.make_move(gamestate=self._rounds)
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

            self.add_round(move_bot=move_bot, move_user=move_user)
            print("Round {0}/{1}:".format(len(self._rounds[ROUNDS]), self._rounds_max))
            print("{0} (bot):  move={1}, points={2}, dynamite={3}".format(
                P1_BOT, move_bot, self._points_bot, self.bot.get_dynamite_left()))
            print("{0} (user): move={1}, points={2}, dynamite={3}".format(
                P2_USER, move_user, self._points_user, self._dynamite_user))
            print("> Winner = {0}".format(winner))

            return self.game_finished()

        else:
            return True  # game has finished

    def game_finished(self) -> bool:
        return len(self._rounds[ROUNDS]) >= self._rounds_max or \
               self._points_bot >= self._points_max or \
               self._points_user >= self._points_max

    def add_round(self, move_bot: str, move_user: str) -> None:
        self._rounds[ROUNDS].append({
            P1_BOT: move_bot,
            P2_USER: move_user
        })

    def _get_winner(self, move_bot, move_user) -> str:
        if move_bot == move_user:
            return None

        if move_bot == DYNAMITE and move_user != WATER_BALLOON:
            return P1_BOT

        if move_bot == WATER_BALLOON and move_user == DYNAMITE:
            return P1_BOT

        if move_bot == ROCK and (move_user == SCISSORS or move_user == WATER_BALLOON):
            return P1_BOT

        if move_bot == SCISSORS and (move_user == PAPER or move_user == WATER_BALLOON):
            return P1_BOT

        if move_bot == PAPER and (move_user == ROCK or move_user == WATER_BALLOON):
            return P1_BOT

        return P2_USER

import random


class PowerBot:

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

    def __init__(self):
        self._name = "p1"
        self._dynamite = 100

        self._distribution = {
            self.ROCK: 0,
            self.PAPER: 0,
            self.SCISSORS: 0,
            self.DYNAMITE: 0,
            self.WATER_BALLOON: 0
        }

    def make_move(self, gamestate):
        last_round = self._get_last_round(gamestate)

        if last_round is not None:
            self._update_distribution(last_round)

            # todo
            # remove below
            return self._random_move()

        else:  # no prior rounds
            return self._random_move()  # first ever move is random

    def get_dynamite_left(self) -> int:
        return self._dynamite

    def _get_last_round(self, gamestate):
        if len(gamestate[self.ROUNDS]) > 0:
            return gamestate[self.ROUNDS][-1]
        return None

    def _update_distribution(self, last_round):
        pass  # todo

    def _random_move(self) -> str:
        choice = None

        while choice is None or (choice == self.DYNAMITE and self._dynamite == 0):
            choice = random.choice(self.MOVES)

        if choice == self.DYNAMITE:
            self._dynamite -= 1

        if self._dynamite < 0:
            raise Exception("Dynamite count is {0}, but should not be below {1}".format(self._dynamite, 0))

        return choice

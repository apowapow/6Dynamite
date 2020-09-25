import random


class PowerBot:
    global random

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

    P1 = "p1"
    P2 = "p2"
    ROUNDS = "rounds"
    DISTRIBUTION_WINDOW = 5

    def __init__(self):
        self._dynamite = 100

        self._p2_distribution = None
        self._p2_last_move = None
        self._p2_dynamite = 100

    def make_move(self, gamestate):
        # first ever move is random
        if len(gamestate[self.ROUNDS]) == 0:
            return self._random_move_from_list(self.MOVES)

        # update bot models
        self._process_gamestate(gamestate)
        self._print_statistics()

        # select winning move based on p2 moves of highest frequency
        # e.g. if p2 often chooses rock, then choose paper, etc.
        highest_frequency = max(self._p2_distribution.values())
        freq_moves = []
        next_moves = []

        for move, freq in self._p2_distribution.items():
            if freq == highest_frequency:
                freq_moves.append(move)

        if self.ROCK in freq_moves:
            next_moves.append(self.PAPER)

        if self.PAPER in freq_moves:
            next_moves.append(self.SCISSORS)

        if self.SCISSORS in freq_moves:
            next_moves.append(self.ROCK)

        # if p2 often chooses dynamite
        if self.DYNAMITE in freq_moves:
            # if still has dynamite left, include water balloon
            if self._p2_dynamite > 0:
                next_moves.append(self.WATER_BALLOON)

        # if p2 does not frequently choose water balloon, and there's dynamite left, and multiple next moves
        if self.WATER_BALLOON not in freq_moves and self._dynamite > 0 and len(next_moves) > 1:
            next_moves.append(self.DYNAMITE)

        # pick next move (randomly if multiple optimal choices)
        return self._random_move_from_list(next_moves if len(next_moves) > 0 else self.MOVES)

    def get_dynamite_left(self) -> int:
        return self._dynamite

    def _process_gamestate(self, gamestate):
        rounds = gamestate[self.ROUNDS]

        # p2 last move
        self._p2_last_move = rounds[-1][self.P2]

        if self._p2_last_move == self.DYNAMITE:
            self._p2_dynamite -= 1

        # p2 last n moves
        self._p2_distribution = {
            self.ROCK: 0,
            self.PAPER: 0,
            self.SCISSORS: 0,
            self.DYNAMITE: 0,
            self.WATER_BALLOON: 0
        }
        window = min(len(rounds), self.DISTRIBUTION_WINDOW)
        for move_dist in rounds[-window:]:
            self._p2_distribution[move_dist[self.P2]] += 1

    def _print_statistics(self):
        print("Distribution")
        print("  Rock:     {0}".format(self._p2_distribution[self.ROCK]))
        print("  Paper:    {0}".format(self._p2_distribution[self.PAPER]))
        print("  Scissors: {0}".format(self._p2_distribution[self.SCISSORS]))
        print("  Dynamite: {0}".format(self._p2_distribution[self.DYNAMITE]))
        print("  Water:    {0}".format(self._p2_distribution[self.WATER_BALLOON]))
        print("Last Move:  {0}".format(self._p2_last_move))
        print()

    def _random_move_from_list(self, move_list) -> str:
        choice = None

        while choice is None or (choice == self.DYNAMITE and self._dynamite == 0):
            choice = random.choice(move_list)

        if choice == self.DYNAMITE:
            self._dynamite -= 1

        return choice

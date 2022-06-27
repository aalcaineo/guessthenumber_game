from dataclasses import dataclass, field

from src.ui import UI
from src.player import Player
from src.bot import Bot


@dataclass
class Game:
    """Game class"""

    ui: UI
    player: Player
    opponent: Player
    min_num: int
    max_num: int
    trials: int
    number: int = field(init=False)

    def __post_init__(self) -> None:
        if isinstance(self.opponent, Bot):
            self.number = self.opponent.set_number(self.min_num, self.max_num)
        else:
            self.number = self.opponent.set_number(self.ui)

    def play(self) -> None:
        i = 0
        sense = 0
        while i < self.trials:
            self.ui.show_round_count(i)

            guess = self.turn(sense)
            sense = -1 * ((self.number - guess) < 0) + 1 * ((self.number - guess) > 0)

            if not sense:  # True if sense == 0
                break

            self.ui.try_again(sense)

            i += 1

        self.set_winner(not sense)

    def turn(self, sense: int) -> int:
        guess = self.min_num - 1
        while guess not in range(self.min_num, self.max_num + 1):
            try:
                if isinstance(self.player, Bot):
                    guess = self.player.make_guess(self.min_num, self.max_num, sense)
                    self.ui.show_bot_guess(guess)
                else:
                    guess = self.player.make_guess(self.ui)
            except ValueError:
                guess = self.min_num - 1

        return guess

    def set_winner(self, win: bool) -> None:
        if win:
            self.ui.player_wins(self.player.get_name())
        else:
            self.ui.player_looses(self.player.get_name(), self.number)

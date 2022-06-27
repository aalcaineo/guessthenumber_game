from dataclasses import dataclass

from src.game import Game
from src.ui import UI
from src.human import Human
from src.bot import Bot


@dataclass
class Configurator:
    """Configurator dataclass"""

    ui: UI

    def configure(self, min_num: int = 1, max_num: int = 20, trials: int = 6) -> "Game":
        self.ui.show_menu()

        option = ""
        while option not in list("ab"):
            try:
                option = self.ui.get_menu_option()
            except ValueError:
                option = ""

        if option == "a":
            game = Game(self.ui, Human(self.ui), Bot(), min_num, max_num, trials)
        else:
            game = Game(self.ui, Bot(), Human(self.ui), min_num, max_num, trials)

        return game

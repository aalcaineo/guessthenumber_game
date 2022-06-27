from src.ui import UI


class Human:
    """Human player class"""

    def __init__(self, ui: UI) -> None:
        self.name = ui.get_human_name()

    def get_name(self) -> str:
        return self.name

    def set_number(self, ui: UI) -> int:
        return ui.get_human_number()

    def make_guess(self, ui: UI) -> int:
        return ui.get_player_guess()

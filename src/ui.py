from typing import Protocol


class UI(Protocol):
    def show_rules(self) -> str:
        raise NotImplementedError()

    def show_menu(self) -> None:
        raise NotImplementedError()

    def get_menu_option(self) -> str:
        raise NotImplementedError()

    def get_human_name(self) -> str:
        raise NotImplementedError()

    def get_human_number(self) -> int:
        raise NotImplementedError()
 
    def get_player_guess(self) -> int:
        raise NotImplementedError()

    def show_round_count(self) -> None:
        raise NotImplementedError()
    
    def show_bot_guess(self) -> None:
        raise NotImplementedError()

    def player_wins(self) -> None:
        raise NotImplementedError()

    def player_looses(self) -> None:
        raise NotImplementedError()

    def try_again(self) -> None:
        raise NotImplementedError()

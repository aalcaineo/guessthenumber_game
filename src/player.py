from typing import Protocol

class Player(Protocol):
    def __init__(self) -> None:
        raise NotImplementedError
    
    def get_name(self) -> str:
        raise NotImplementedError()

    def set_number(self) -> int:
        raise NotImplementedError()

    def make_guess(self) -> int:
        raise NotImplementedError()
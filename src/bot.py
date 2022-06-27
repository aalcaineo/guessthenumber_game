import random


class Bot:
    def __init__(self) -> None:
        self.name = "cpu"
        self.min = None
        self.max = None
        self._last_guess = None

    def get_name(self) -> str:
        return self.name

    def set_number(self, min_num: int, max_num: int) -> int:
        return random.randint(min_num, max_num)

    def make_guess(self, min_num: int, max_num: int, sense: int) -> int:
        """Divide and conquer algorithm"""
        if self._last_guess is None:
            self.min = min_num
            self.max = max_num
            self._last_guess = (self.max - self.min + 1) // 2
        elif sense > 0:
            self.min = self._last_guess
            self._last_guess += (self.max - self.min + 1) // 2
        else:
            self.max = self._last_guess
            self._last_guess -= (self.max - self.min + 1) // 2

        return self._last_guess

_MENU = """\nWhat game do you want to play?
\ta) CPU vs. Player.
\tb) Player vs. CPU."""


class Terminal:
    """Terminal UI class."""

    def show_rules(self, min_num: int = 1, max_num: int = 20, trials: int = 6) -> str:
        print(
            f"""
Try to guess the number:
\t * The number is between {min_num:d} and {max_num:d}.
\t * You have only {trials:d} opportunities."""
        )

    def show_menu(self) -> None:
        print(_MENU)

    def get_menu_option(self) -> str:
        return input("Choose an availabe option: ")

    def get_human_name(self) -> str:
        return input("What is your name?: ")

    def get_human_number(self) -> int:
        return int(input(f"Choose a number: "))

    def get_player_guess(self) -> int:
        return int(input("Guess the number: "))

    def show_round_count(self, count: int) -> None:
        print(f"\nRound {count+1}:")
    
    def show_bot_guess(self,guess) -> None:
        print(f"CPU guesses: {guess}")

    def player_wins(self, name: str) -> None:
        print(f"\n>>>> {name.upper()} WINS <<<<")

    def player_looses(self, name: str, number: int) -> None:
        print(f"\n>>>> {name.upper()} LOOSE <<<<")
        print(f"The number was: {number}.")

    def try_again(self, sense: int) -> None:
        if sense < 0:
            print("\n>>>> TOO HIGH <<<<")
        else:
            print("\n>>>> TOO LOW <<<<")

from src.configurator import Configurator
from src.terminal import Terminal

def main() -> None:
    ui = Terminal()
    ui.show_rules()

    config = Configurator(ui)
    game = config.configure()

    game.play()

if __name__ == "__main__":
    main()
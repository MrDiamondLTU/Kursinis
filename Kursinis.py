from abc import ABC, abstractmethod
import random

# --- PRODUKTAS (Abstrakcija) ---
class Player(ABC):
    def __init__(self, symbol):
        self.symbol = symbol

    @abstractmethod
    def get_move(self, board): 
        pass

# --- KONKRETŪS PRODUKTAI ---
class HumanPlayer(Player):
    def get_move(self, board):
        while True:
            try:
                user_input = input(f"Žaidėjau {self.symbol}, įvesk eilutę ir stulpelį (1-3): ").split()
                row, col = int(user_input[0]) - 1, int(user_input[1]) - 1
                return row, col
            except (ValueError, IndexError):
                print("Klaida! Bandyk dar kartą.")
class AIPlayer(Player):
    def get_move(self, board):
        print(f"AI ({self.symbol}) mąsto...")
        # Paprasta logika: randa laisvas vietas ir pasirenka atsitiktinę
        available_moves = [(r, c) for r in range(3) for c in range(3) if board.is_valid_move(r, c)]
        return random.choice(available_moves)

# --- GAMYKLA (Factory) ---
class PlayerFactory:
    """Tai yra 'Gamykla', kuri atsakinga už objektų kūrimą."""
    @staticmethod
    def create_player(player_type, symbol):
        if player_type == "human":
            return HumanPlayer(symbol)
        elif player_type == "ai":
            return AIPlayer(symbol)
        else:
            raise ValueError("Nežinomas žaidėjo tipas")

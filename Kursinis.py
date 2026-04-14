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

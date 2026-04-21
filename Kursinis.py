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

# --- ŽAIDIMO LOGIKA ---
class TicTacToe:
    def __init__(self):
        self.__board = [[" " for _ in range(3)] for _ in range(3)]
    
    def is_valid_move(self, r, c):
        return 0 <= r < 3 and 0 <= c < 3 and self.__board[r][c] == " "

    def make_move(self, r, c, symbol):
        if self.is_valid_move(r, c):
            self.__board[r][c] = symbol
            return True
        return False

    def display_board(self):
        for i, row in enumerate(self.__board):
            print(" " + " | ".join(row))
            if i < 2: print("---+---+---")

    def check_winner(self):
        b = self.__board
        lines = b + list(map(list, zip(*b)))
        lines.append([b[i][i] for i in range(3)])
        lines.append([b[i][2-i] for i in range(3)])
        for line in lines:
            if line[0] == line[1] == line[2] and line[0] != " ":
                return line[0]
        return None

    def is_full(self):
        return all(cell != " " for row in self.__board for cell in row)

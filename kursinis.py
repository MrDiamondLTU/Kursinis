from abc import ABC, abstractmethod

# 1. ABSTRACTION: Defining what a "Player" must be able to do
class Player(ABC):
    def __init__(self, symbol):
        self.symbol = symbol

    @abstractmethod
    def get_move(self, board):
        pass

# 3. INHERITANCE: HumanPlayer "is a" Player
class HumanPlayer(Player):
    def get_move(self, board):
        while True:
            try:
                user_input = input(f"Player {self.symbol}, enter row and col (1-3): ").split()
                # Converting 1-3 input to 0-2 index
                row, col = int(user_input[0]) - 1, int(user_input[1]) - 1
                return row, col
            except (ValueError, IndexError):
                print("Invalid input. Try again.")

# 2. ENCAPSULATION: Logic and data are bundled together
class TicTacToe:
    def __init__(self):
        # Private attribute: The board state is hidden from direct outside access
        self.__board = [[" " for _ in range(3)] for _ in range(3)]
    
    def display_board(self):
        print("\n")
        for i, row in enumerate(self.__board):
            print(" " + " | ".join(row))
            if i < 2: print("---+---+---")

    def is_valid_move(self, r, c):
        return 0 <= r < 3 and 0 <= c < 3 and self.__board[r][c] == " "

    def make_move(self, r, c, symbol):
        if self.is_valid_move(r, c):
            self.__board[r][c] = symbol
            return True
        return False

    def check_winner(self):
        b = self.__board
        lines = b + list(map(list, zip(*b))) # Rows/Cols
        lines.append([b[i][i] for i in range(3)]) # Diagonals
        lines.append([b[i][2-i] for i in range(3)])
        
        for line in lines:
            if line[0] == line[1] == line[2] and line[0] != " ":
                return line[0]
        return None

    def is_full(self):
        return all(cell != " " for row in self.__board for cell in row)

# Running the Game
def play_game():
    game = TicTacToe()
    # 4. POLYMORPHISM: We treat these as generic "Players"
    players = [HumanPlayer("X"), HumanPlayer("O")]
    current_idx = 0

    while True:
        game.display_board()
        player = players[current_idx]
        
        # Polymorphic call: The game doesn't care how get_move works internally
        r, c = player.get_move(game)
        
        if game.make_move(r, c, player.symbol):
            winner = game.check_winner()
            if winner:
                game.display_board()
                print(f"Player {winner} wins!")
                break
            if game.is_full():
                game.display_board()
                print("It's a draw!")
                break
            current_idx = 1 - current_idx # Swap players
        else:
            print("Invalid move! Spot taken or out of bounds.")

if __name__ == "__main__":
    play_game()
# tic_tac_toe.py
# 간단한 콘솔 기반 틱택토 게임

from typing import List, Optional


class TicTacToe:
    def __init__(self):
        # 3x3 게임판 초기화
        self.board: List[List[Optional[str]]] = [[None] * 3 for _ in range(3)]
        self.current_player: str = "X"

    def print_board(self) -> None:
        # 게임판 출력
        for row in self.board:
            row_str = "|".join([cell if cell is not None else " " for cell in row])
            print(row_str)
            print("-" * 5)

    def make_move(self, row: int, col: int) -> bool:
        # 유효한 위치에 플레이어 표시
        if 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] is None:
            self.board[row][col] = self.current_player
            return True
        return False

    def switch_player(self) -> None:
        # 플레이어 전환
        self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self) -> Optional[str]:
        # 가로, 세로, 대각선 체크
        lines = self.board + [list(col) for col in zip(*self.board)]  # 행 + 열
        diag1 = [self.board[i][i] for i in range(3)]
        diag2 = [self.board[i][2 - i] for i in range(3)]
        lines.append(diag1)
        lines.append(diag2)

        for line in lines:
            if line[0] is not None and all(cell == line[0] for cell in line):
                return line[0]
        return None

    def is_full(self) -> bool:
        # 게임판이 다 찼는지 확인
        return all(cell is not None for row in self.board for cell in row)


def play_game():
    game = TicTacToe()
    winner: Optional[str] = None

    while not winner and not game.is_full():
        game.print_board()
        try:
            move = input(
                f"Player {game.current_player}, enter row and column (0-2, space separated): "
            )
            row, col = map(int, move.strip().split())
            if not game.make_move(row, col):
                print("Invalid move! Try again.")
                continue
            winner = game.check_winner()
            if winner:
                break
            game.switch_player()
        except Exception:
            print("Invalid input! Please enter numbers 0-2. ")

    game.print_board()
    if winner:
        print(f"Player {winner} wins!")
    else:
        print("It's a draw!")


if __name__ == "__main__":
    play_game()

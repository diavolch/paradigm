class TicTacToe:
    def __init__(self):
        self.board = [' ' for i in range(9)]
        self.current_player = 'X'

    def draw_bord(self, board):
        print('-' * 13)
        for i in range(3):
            print('|', board[0 + i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
            print('-' * 13)

    def make_move(self, num):
        if not self.check_win() and self.board[num] == ' ':
            self.board[num] = self.current_player
            self.draw_bord(self.board)
            if self.check_win():
                print(f'Победил игрок c {self.current_player}!')
            if self.current_player == 'X':
                self.current_player = '0'
            else:
                self.current_player = 'X'
        else:
            print('Недопустимый ход')

    def check_win(self):
        win_list = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for win in win_list:
            if self.board[win[0]] == self.board[win[1]] == self.board[win[2]] != ' ':
                return self.board[win[0]]
        return False


game = TicTacToe()
game.make_move(0)
game.make_move(0)
game.make_move(4)
game.make_move(3)
game.make_move(8)
game.make_move(6)
game.make_move(1)

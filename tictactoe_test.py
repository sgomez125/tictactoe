import unittest
from tictactoe import initial_state, X, O, EMPTY, player, actions, result, winner, terminal

class TestTictactoeMethods(unittest.TestCase):

    def test_player_empty_board(self):
        self.assertEqual(player(initial_state()), X)
    
    def test_player_x_turn_board(self):
        o_board = [[EMPTY, X, EMPTY],
            [O, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
        self.assertEqual(player(o_board), X)

    def test_player_o_turn_board(self):
        x_board = [[EMPTY, O, EMPTY],
            [X, EMPTY, EMPTY],
            [EMPTY, X, EMPTY]]
        self.assertEqual(player(x_board), O)

    def test_actions_method_empty_board(self):
        actions_to_do = actions(initial_state())
        for row in range(3):
            for col in range(3):
                self.assertTrue((row, col) in actions_to_do)

    def test_player_o_result(self):
        board = [[EMPTY, O, EMPTY],
            [X, EMPTY, EMPTY],
            [EMPTY, X, EMPTY]]
        result_board = [[EMPTY, O, EMPTY],
            [X, EMPTY, O],
            [EMPTY, X, EMPTY]]
        self.assertEqual(result(board, (1, 2)), result_board)
    
    def test_no_winner(self):
        board = [[EMPTY, O, EMPTY],
            [X, EMPTY, EMPTY],
            [EMPTY, X, EMPTY]]
        self.assertEqual(winner(board), None)

    def test_winner_row(self):
        board = [[O, O, EMPTY],
            [X, O, EMPTY],
            [X, X, X]]
        self.assertEqual(winner(board), X)
    
    def test_winner_row_2(self):
        board = [[X, X, X],
            [X, O, EMPTY],
            [EMPTY, X, EMPTY]]
        self.assertEqual(winner(board), X)
    
    def test_winner_col(self):
        board = [[X, O, EMPTY],
            [X, O, EMPTY],
            [X, X, O]]
        self.assertEqual(winner(board), X)
    
    def test_winner_diagonal(self):
        board = [[O, O, EMPTY],
            [X, O, X],
            [X, X, O]]
        self.assertEqual(winner(board), O)
    
    def test_winner_back_diagonal(self):
        board = [[X, O, O],
            [X, O, X],
            [O, X, O]]
        self.assertEqual(winner(board), O)
    
    def test_not_terminal(self):
        board = [[O, O, EMPTY],
                 [X, O, X],
                 [X, X, EMPTY]]
        self.assertFalse(terminal(board))
    
    def test_terminal(self):
        board = [[O, O, O],
            [X, O, X],
            [X, X, O]]
        self.assertTrue(terminal(board))

if __name__ == '__main__':
    unittest.main()
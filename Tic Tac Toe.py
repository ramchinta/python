'''Design a Tic-tac-toe game that is played between two players on a n x n grid.

You may assume the following rules:

A move is guaranteed to be valid and is placed on an empty block.
Once a winning condition is reached, no more moves is allowed.
A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.
Example:
Given n = 3, assume that player 1 is "X" and player 2 is "O" in the board.

TicTacToe toe = new TicTacToe(3);

toe.move(0, 0, 1); -> Returns 0 (no one wins)
|X| | |
| | | |    // Player 1 makes a move at (0, 0).
| | | |

toe.move(0, 2, 2); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 2 makes a move at (0, 2).
| | | |

toe.move(2, 2, 1); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 1 makes a move at (2, 2).
| | |X|

toe.move(1, 1, 2); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 2 makes a move at (1, 1).
| | |X|

toe.move(2, 0, 1); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 1 makes a move at (2, 0).
|X| |X|

toe.move(1, 0, 2); -> Returns 0 (no one wins)
|X| |O|
|O|O| |    // Player 2 makes a move at (1, 0).
|X| |X|

toe.move(2, 1, 1); -> Returns 1 (player 1 wins)
|X| |O|
|O|O| |    // Player 1 makes a move at (2, 1).
|X|X|X|
Follow up:
Could you do better than O(n2) per move() operation?'''


class TicTacToe:

    def __init__(self, n):
        """Initialize your data structure here.
        """
        self.n = n
        # n rows, n cols, 1 main diagonal (dial), 1 anti diagonal (anti) to win the game
        # bitmask, use the nums 0..00 to represent player 1's or player 2's taken on the row, col and diag
        # win? if == 1..11, otherwise no win, each move up to 4 O(1) update and 4 O(1) comparisons
        # actually, no win at all can be checked and stop early, but no need here.
        self.status = [
            # 2 players, each n rows, n cols, 1 dial, 1 anti.
            [[0] * n, [0] * n, 0, 0], [[0] * n, [0] * n, 0, 0],
        ]
        self.win = (1 << n) - 1

    def move(self, row, col, player):
        """Player {player} makes a move at ({row}, {col}).
          @param row The row of the board.
          @param col The column of the board.
          @param player The player, can be either 1 or 2.
          @return The current winning condition, can be either:
                  0: No one wins.
                  1: Player 1 wins.
                  2: Player 2 wins.
        """
        # on r-th row, k-th col is taken by player
        self.status[player - 1][0][row] |= 1 << col
        if self.status[player - 1][0][row] == self.win:
            return player
        # on k-th col, r-th row is taken by player
        self.status[player - 1][1][col] |= 1 << row
        if self.status[player - 1][1][col] == self.win:
            return player
        # main diagonal
        if row == col:
            self.status[player - 1][2] |= 1 << col
            if self.status[player - 1][2] == self.win:
                return player
        # anti diagonal
        if row + col == self.n - 1:
            self.status[player - 1][3] |= 1 << row
            if self.status[player - 1][3] == self.win:
                return player
        # note: rows, cols, dial and anti, if already been taken by both, can be skipped for winning possible
        # this can be achieved/implemented by holding an additional bothTaken data.
        return 0
    
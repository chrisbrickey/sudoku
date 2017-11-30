import unittest


def dfs(tree):
    if is_valid_leaf(tree):  # current node IS a leaf
        leaf = tree["board"]
        if is_valid_board(leaf):
            return True  # will this stop recursion? - yes
    else:  # current node is not a leaf
        children = tree["children"]
        for child in children:
            return dfs(child)

    return False


# while len(current_node["children]) > 0
# grab a child
# current_node = child


def create_tree(board):
    valid_node = {"board": [['3'] * 9 for i in range(9)], "children": []}
    tree = {"board": [['3'] * 9 for i in range(9)], "children": [valid_node]}
    return tree


def sudoku_solve(board):
    tree = create_tree(board)
    return dfs(tree)


def is_valid_leaf(node):
    if len(node["children"]) == 0:
        return True
    else:
        return False


def is_valid_board(board):
    for row in board:
        for cell in row:
            if cell == ".":
                return False

    return True


class SudokuTest(unittest.TestCase):

    def test_valid_board(self):
        board = [[".", ".", ".", "7", ".", ".", "3", ".", "1"],
                 ["3", ".", ".", "9", ".", ".", ".", ".", "."],
                 [".", "4", ".", "3", "1", ".", "2", ".", "."],
                 [".", "6", ".", "4", ".", ".", "5", ".", "."],
                 [".", ".", ".", ".", ".", ".", ".", ".", "."],
                 [".", ".", "1", ".", ".", "8", ".", "4", "."],
                 [".", ".", "6", ".", "2", "1", ".", "5", "."],
                 [".", ".", ".", ".", ".", "9", ".", ".", "8"],
                 ["8", ".", "5", ".", ".", "4", ".", ".", "."]]
        self.assertTrue(sudoku_solve(board))

    def test_invalid_board(self):
        board = [[".", "8", "9", ".", "4", ".", "6", ".", "5"],
                 [".", "7", ".", ".", ".", "8", ".", "4", "1"],
                 ["5", "6", ".", "9", ".", ".", ".", ".", "8"],
                 [".", ".", ".", "7", ".", "5", ".", "9", "."],
                 [".", "9", ".", "4", ".", "1", ".", "5", "."],
                 [".", "3", ".", "9", ".", "6", ".", "1", "."],
                 ["8", ".", ".", ".", ".", ".", ".", ".", "7"],
                 [".", "2", ".", "8", ".", ".", ".", "6", "."],
                 [".", ".", "6", ".", "7", ".", ".", "8", "."]]
        self.assertFalse(sudoku_solve(board))


class BoardValidatorTest(unittest.TestCase):

    def test_valid_board(self):
        board = [['3'] * 9 for i in range(9)]
        self.assertTrue(is_valid_board(board))

    def test_invalid_board_58(self):
        board = [['3'] * 9 for i in range(9)]
        board[5][8] = "."
        self.assertFalse(is_valid_board(board))

    def test_invalid_board_12(self):
        board = [['3'] * 9 for i in range(9)]
        board[1][2] = "."
        self.assertFalse(is_valid_board(board))


class LeafValidatorTest(unittest.TestCase):

    def test_invalid_leaf(self):
        node = {"board": 1, "children": [{"board": 2, "children": []}, {"board": 3, "children": []}]}
        self.assertFalse(is_valid_leaf(node))

    def test_valid_leaf(self):
        node = {"board": 1, "children": []}
        self.assertTrue(is_valid_leaf(node))


class DfsTest(unittest.TestCase):

    def test_dfs(self):
        invalid_node = {"board": [['.'] * 9 for i in range(9)], "children": []}
        invalid_tree = {"board": [['.'] * 9 for i in range(9)], "children": [invalid_node]}
        self.assertFalse(dfs(invalid_tree))





















# describe '#sudoku_solve' do
#
#   it "works1" do
#     input = [[".",".",".","7",".",".","3",".","1"],["3",".",".","9",".",".",".",".","."],[".","4",".","3","1",".","2",".","."],[".","6",".","4",".",".","5",".","."],[".",".",".",".",".",".",".",".","."],[".",".","1",".",".","8",".","4","."],[".",".","6",".","2","1",".","5","."],[".",".",".",".",".","9",".",".","8"],["8",".","5",".",".","4",".",".","."]]
#     expect(sudoku_solve(input)).to eq(true)
#   end
#
#   it "works2" do
#     input = [[".","8","9",".","4",".","6",".","5"],[".","7",".",".",".","8",".","4","1"],["5","6",".","9",".",".",".",".","8"],[".",".",".","7",".","5",".","9","."],[".","9",".","4",".","1",".","5","."],[".","3",".","9",".","6",".","1","."],["8",".",".",".",".",".",".",".","7"],[".","2",".","8",".",".",".","6","."],[".",".","6",".","7",".",".","8","."]]
#     expect(sudoku_solve(input)).to eq(false)
#   end
#
#   it "works3" do
#     input = [[".","2","3","4","5","6","7","8","9"],["1",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]
#     expect(sudoku_solve(input)).to eq(false)
#   end
#
#   it "works4" do
#     input = [[".",".","5",".",".","2",".",".","."],[".",".","9",".","4","7",".","2","."],[".",".","8",".","5","6",".",".","1"],[".",".",".",".",".","8","3","4","."],[".",".",".",".",".",".",".",".","6"],[".",".",".",".","3",".","1","8","."],[".","2",".",".",".",".",".",".","."],[".","9",".",".","8",".","6","7","."],["3",".","6","5","7",".",".",".","."]]
#     expect(sudoku_solve(input)).to eq(true)
#   end
#
#   it "works5" do
#     input = [[".",".","3","8",".",".","4",".","."],[".",".",".",".","1",".",".","7","."],[".","6",".",".",".","5",".",".","9"],[".",".",".","9",".",".","6",".","."],[".","2",".",".",".",".",".","1","."],[".",".","4",".",".","3",".",".","2"],[".",".","2",".",".",".","8",".","."],[".","1",".",".",".",".",".","5","."],["9",".",".",".",".","7",".",".","3"]]
#     expect(sudoku_solve(input)).to eq(true)
#   end
#
#   it "works5" do
#     input = [[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]
#     expect(sudoku_solve(input)).to eq(true)
#   end
#
# end

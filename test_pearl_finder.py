import unittest

from logicaMasyu import jugadorAutomatico

class TestFindStartingPearl(unittest.TestCase):

    def test_first_row_white_pearl(self):
        matrix = [
            [1, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.assertEqual(jugadorAutomatico.find_starting_pearl(matrix), (0, 0, 1))


    def test_last_row_white_pearl(self):
        matrix = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 1]
        ]
        self.assertEqual(jugadorAutomatico.find_starting_pearl(matrix), (2, 2, 1))

    def test_first_column_white_pearl(self):
        matrix = [
            [0, 0, 0],
            [1, 0, 0],
            [0, 0, 0]
        ]
        self.assertEqual(jugadorAutomatico.find_starting_pearl(matrix), (1, 0, 2))

    def test_last_column_white_pearl(self):
        matrix = [
            [0, 0, 0],
            [0, 0, 1],
            [0, 0, 0]
        ]
        self.assertEqual(jugadorAutomatico.find_starting_pearl(matrix), (1, 2, 2))

    def test_corner_black_pearl(self):
        matrix = [
            [2, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.assertEqual(jugadorAutomatico.find_starting_pearl(matrix), (0, 0, 3))

    def test_any_white_pearl(self):
        matrix = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]
        self.assertEqual(jugadorAutomatico.find_starting_pearl(matrix), (1, 1, 4))

    def test_any_black_pearl(self):
        matrix = [
            [0, 0, 0],
            [0, 2, 0],
            [0, 0, 0]
        ]
        self.assertEqual(jugadorAutomatico.find_starting_pearl(matrix), (1, 1, 5))

    def test_no_pearl(self):
        matrix = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.assertIsNone(jugadorAutomatico.find_starting_pearl(matrix))

if __name__ == '__main__':
    unittest.main()

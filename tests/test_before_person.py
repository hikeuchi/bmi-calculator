import unittest


class TestCalculateBmi(unittest.TestCase):

    def test_valid(self):
        from Before.person import Person

        # （期待値, personのインスタンス）
        test_cases = (
            (19.5, Person(weight=50, height_cm=160)),
        )

        for expected, person in test_cases:
            with self.subTest():
                actual = person._calculate_bmi()
                self.assertEqual(expected, actual)


if __name__ == "__main__":
    import os
    import sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    unittest.main()

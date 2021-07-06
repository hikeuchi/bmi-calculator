import unittest


class TestCalculateBmi(unittest.TestCase):

    def test_valid(self):
        from Before.user import User

        # （期待値, userのインスタンス）
        test_cases = (
            (19.5, User(weight=50, height_cm=160)),
        )

        for expected, user in test_cases:
            with self.subTest():
                actual = user._calculate_bmi()
                self.assertEqual(expected, actual)


if __name__ == "__main__":
    import os
    import sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    unittest.main()

import unittest


class TestCalculateBmi(unittest.TestCase):

    def test_valid(self):
        from After.person import _calculate_bmi

        # （期待値, 体重, 身長）
        test_cases = (
            (19.5, 50, 1.6),
        )

        for expected, weight, height in test_cases:
            with self.subTest():
                actual = _calculate_bmi(weight=weight, height=height)
                self.assertEqual(expected, actual)


if __name__ == "__main__":
    import os
    import sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    unittest.main()

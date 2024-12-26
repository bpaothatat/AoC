import os
import unittest
from solution import SafetyManual, parse_input, solve_part1#, solve_part2

class TestSolution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Load and parse the input file once for all test cases."""
        file_path = os.path.join(os.path.dirname(__file__), "test_input.txt")
        with open(file_path, 'r') as f:
            input_data = f.read()
        cls.safety_manual = parse_input(input_data)

    def test_part1(self):
        """Test part 1 of the solution."""
        expected = 143
        self.assertEqual(solve_part1(self.safety_manual), expected)

    # def test_part2(self):
    #     """Test part 2 of the solution."""
    #     expected = 31 
    #     self.assertEqual(solve_part2(self.col1, self.col2), expected)

if __name__ == "__main__":
    unittest.main()
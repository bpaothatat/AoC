import os
from collections import Counter

def read_input(file_path: str) -> str:
    """Read input from a file and return its contents as a string."""
    with open(file_path, 'r') as f:
        return f.read()

def parse_input(input_data: str):
    """Convert the raw input data into a structured format."""
    lines = input_data.splitlines()
    column1, column2 = [], []
    for line in lines:
        col1, col2 = map(int, line.split())
        column1.append(col1)
        column2.append(col2)

    sorted_column1 = sorted(column1)
    sorted_column2 = sorted(column2)

    return sorted_column1, sorted_column2

def solve_part1(col1: list[int], col2: list[int]):
    """Solve part 1 of the day's challenge."""
    return sum(abs(a-b) for a, b in zip(col1, col2))

def count_occurences(nums: list[int]) -> dict[int, int]:
    return dict(Counter(nums))

def solve_part2(col1: list[int], col2: list[int]):
    """Solve part 2 of the day's challenge."""
    lookup = count_occurences(col2)
    return sum(a * lookup.get(a,0) for a in col1)

if __name__ == "__main__":
    # Load and parse input
    file_path = os.path.join(os.path.dirname(__file__), "input.txt")
    input_data = read_input(file_path)
    col1, col2 = parse_input(input_data)
    
    # Solve parts
    print("Part 1:", solve_part1(col1, col2))
    print("Part 2:", solve_part2(col1, col2))

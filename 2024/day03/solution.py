import os
import re

def read_input(file_path: str) -> str:
    """Read input from a file and return its contents as a string."""
    with open(file_path, 'r') as f:
        return f.read()

def parse_input(input_data: str) -> list[list[int]]:
    """Convert the raw input data into a structured format."""
    data = []
    lines = input_data.splitlines()
  
    for line in lines:
        data += find_mul_instances(line)

    return data

def find_mul_instances(line: str) ->  list[str]:
    pattern = r'mul\(\d{1,3},\d{1,3}\)'
    
    matches = re.findall(pattern, line)
    return matches

def calculate_instructions(data: list[str]) -> int:
    result = 0

    for item in data:
        pattern = r'mul\((\d+),(\d+)\)'
        match = re.search(pattern, item)
        if match:
            number1, number2 = match.groups()
            result += int(number1) * int(number2)
    return result

def solve_part1(data: list[str]):
    """Solve part 1 of the day's challenge."""
    return calculate_instructions(data)


def solve_part2(data: list[list[int]]):
    """Solve part 2 of the day's challenge."""
    return 0

if __name__ == "__main__":
    # Load and parse input
    file_path = os.path.join(os.path.dirname(__file__), "input.txt")
    input_data = read_input(file_path)
    col1 = parse_input(input_data)
    
    # Solve parts
    print("Part 1:", solve_part1(col1))
    # print("Part 2:", solve_part2(col1, col2))

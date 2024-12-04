import os

def read_input(file_path: str) -> str:
    """Read input from a file and return its contents as a string."""
    with open(file_path, 'r') as f:
        return f.read()

def parse_input(input_data: str) -> list[list[int]]:
    """Convert the raw input data into a structured format."""
    data = []
    lines = input_data.splitlines()
  
    for line in lines:
        data.append(list(map(int, line.split())))

    return data

def solve_part1(data: list[list[int]]):
    """Solve part 1 of the day's challenge."""
    counter = 0
    for line in data:
        differences = [line[i + 1] - line[i] for i  in range(len(line) - 1)]
        if all(num < 0 and num > -4 for num in differences) or all(num < 4 and num > 0 for num in differences):
            counter += 1
    return counter

def solve_part2(data: list[list[int]]):
    """Solve part 2 of the day's challenge."""
    counter = 0
    for line in data:
        differences = [line[i + 1] - line[i] for i  in range(len(line) - 1)]
        if all(num < 0 and num > -4 for num in differences) or all(num < 4 and num > 0 for num in differences):
            counter += 1
    return counter

if __name__ == "__main__":
    # Load and parse input
    file_path = os.path.join(os.path.dirname(__file__), "input.txt")
    input_data = read_input(file_path)
    col1 = parse_input(input_data)
    
    # Solve parts
    print("Part 1:", solve_part1(col1))
    # print("Part 2:", solve_part2(col1, col2))

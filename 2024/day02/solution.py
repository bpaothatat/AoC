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
        if (is_increasing_in_range(line) or
            is_decreasing_in_range(line)):
                counter += 1
    return counter

def is_increasing_in_range(data:  list[int]):
    return all(data[i] < data[i + 1] and data[i + 1] - data[i] < 4 for i in range(len(data) - 1))

def is_decreasing_in_range(data:  list[int]):
    return all(data[i] > data[i + 1] and data[i] - data[i + 1] < 4 for i in range(len(data) - 1))

def is_increasing_in_range_with_ignore(data: list[int]):
    for i in range(len(data)):
        temp_data =  data[:i] + data[i+1:]
        if is_increasing_in_range(temp_data):
            return True
    return False

def is_decreasing_in_range_with_ignore(data: list[int]):
    for i in range(len(data)):
        temp_data =  data[:i] + data[i+1:]
        if is_decreasing_in_range(temp_data):
            return True
    return False

def solve_part2(data: list[list[int]]):
    """Solve part 2 of the day's challenge."""
    counter = 0
    for line in data:
        if (is_increasing_in_range(line) or
            is_decreasing_in_range(line) or
            is_increasing_in_range_with_ignore(line) or
            is_decreasing_in_range_with_ignore(line)):
            counter += 1
    return counter

if __name__ == "__main__":
    # Load and parse input
    file_path = os.path.join(os.path.dirname(__file__), "input.txt")
    input_data = read_input(file_path)
    col1 = parse_input(input_data)
    
    # Solve parts
    print("Part 1:", solve_part1(col1))
    print("Part 2:", solve_part2(col1))

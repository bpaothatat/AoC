import os

def read_input(file_path: str) -> str:
    """Read input from a file and return its contents as a string."""
    with open(file_path, 'r') as f:
        return f.read()

def parse_input(input_data: str) -> list[list[int]]:
    """Convert the raw input data into a structured format."""
    data = []
    return  input_data.splitlines()

def solve_part1(grid: list[str], word: str):
    """Solve part 1 of the day's challenge."""
    rows = len(grid)
    cols = len(grid[0])
    total_count = 0

    # Define all eight directions (row delta, column delta)
    directions = [
        (0, 1),  # Right
        (0, -1), # Left
        (1, 0),  # Down
        (-1, 0), # Up
        (1, 1),  # Down-right
        (1, -1), # Down-left
        (-1, 1), # Up-right
        (-1, -1) # Up-left
    ]

    # Iterate over every cell in the grid
    for row in range(rows):
        for col in range(cols):
            # Check all directions from the current cell
            for delta_row, delta_col in directions:
                total_count += search_direction(grid, row, col, delta_row, delta_col, word)

    return total_count

def search_direction(grid: list[str], start_row: int, start_col: int, delta_row: int, delta_col: int, word: str):
    rows = len(grid)
    cols = len(grid[0])
    word_length = len(word)

    # Check boundary conditions for the word to fit
    for i in range(word_length):
        r = start_row + i * delta_row
        c = start_col + i * delta_col
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != word[i]:
            return 0
    return 1
    

def x_mas_search(grid: list[str], r: int, c: int):
    row_length = len(grid)
    col_length = len(grid[0])
    if r - 1 >= 0 and r + 1 < row_length and  c - 1 >= 0 and c + 1 < col_length:
        if ((grid[r-1][c+1] == 'S' and grid[r+1][c-1] == 'M') or (grid[r-1][c+1] == 'M' and grid[r+1][c-1] == 'S')) and ((grid[r-1][c-1] == 'S' and grid[r+1][c+1] == 'M') or (grid[r-1][c-1] == 'M' and grid[r+1][c+1] == 'S')):
            return 1
    return 0

def solve_part2(grid: list[str]):
    rows = len(grid)
    cols = len(grid[0])
    total_count = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 'A':
                total_count += x_mas_search(grid, row, col)

    return total_count

if __name__ == "__main__":
    # Load and parse input
    file_path = os.path.join(os.path.dirname(__file__), "input.txt")
    input_data = read_input(file_path)
    grid = parse_input(input_data)
    
    # Solve parts
    print("Part 1:", solve_part1(grid, "XMAS"))
    print("Part 2:", solve_part2(grid))

import os

class SafetyManual:
    def __init__(self, rules: list[str], pages: list[str]):
        self.rules = self.parse_rules(rules)
        self.pages = pages

    def parse_rules(self, rules: list[str]) -> dict:
        result = {}
        for rule in rules:
            first, second = rule.split('|')
            if first in result:
                result[first].append(second)
            else:
                result[first] = [second]
        return result
    
    def evaulate_2(self) -> int:
        result = 0
        for page in self.pages:
            page_list = page.split(',')
            valid = True
            for page_number in page_list:
                if page_number in self.rules and not self.valid_pages(page_number, page, self.rules[page_number]):
                    valid = False
                    break
            if not valid:
                result += self.reorder(page_list)
        return result
    
    def reorder(self, page_list: list[str]) -> int:
        new_list = []
        for page in page_list:
            if len(new_list) > 0 and page in self.rules:
                for i, later_page in enumerate(new_list):
                    if later_page in self.rules[page]:
                        new_list.insert(i, page)
                        break
            if page not in new_list:
                new_list.append(page)
        return int(new_list[len(new_list)//2])
    
    def evaulate(self) -> int:
        result = 0
        for page in self.pages:
            page_list = page.split(',')
            valid = True
            for page_number in page_list:
                if page_number in self.rules and not self.valid_pages(page_number, page, self.rules[page_number]):
                    valid = False
                    break
            if valid:
                result += int(page_list[len(page_list)//2])
        return result

    def valid_pages(self, page_number: str, page_list: str, later_page_numbers: list[str]) -> bool:
        page_number_index = page_list.find(page_number)
        for later_page_number in later_page_numbers:
            later_page_number_index = page_list.find(later_page_number)
            if later_page_number_index != -1 and later_page_number_index < page_number_index:
                return False
        return True

    def __str__(self):
        return 'Rules: ' + str(self.rules) + '\n Pages: ' + str(self.pages)
    

def read_input(file_path: str) -> str:
    """Read input from a file and return its contents as a string."""
    with open(file_path, 'r') as f:
        return f.read()

def parse_input(input_data: str) -> SafetyManual:
    """Convert the raw input data into a structured format."""
    data = []
    rules, pages = input_data.split('\n\n')
 
    return SafetyManual(rules.splitlines(), pages.splitlines())

def solve_part1(safetyManuel: SafetyManual) -> int:
    return safetyManuel.evaulate()


def solve_part2(safetyManuel: SafetyManual):
    return safetyManuel.evaulate_2()


if __name__ == "__main__":
    # Load and parse input
    file_path = os.path.join(os.path.dirname(__file__), "input.txt")
    input_data = read_input(file_path)
    col1 = parse_input(input_data)
    
    # Solve parts
    print("Part 1:", solve_part1(col1))
    print("Part 2:", solve_part2(col1))

"""Part 6"""
from typing import List, Dict
from pathlib import Path
import re


def load_input() -> List[str]:
    with open(
        Path(__file__).parents[2].absolute().resolve() / "input" / "6.txt",
        encoding="utf8",
    ) as infile:
        return [line.strip() for line in infile.readlines()]


def do_instruction(
    instruction: str, grid: List[List[int]], start: tuple, end: tuple
) -> List[List[int]]:
    """
    Modify the grid according to the instruction and coordinates

    >>> grid = [[0] * 10 for i in range(10)]
    >>> do_instruction(instruction="toggle", grid=grid, start=(0,0), end=(2,2))
    [[1, 1, 1, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    """
    for row in range(start[0], end[0] + 1):
        for col in range(start[1], end[1] + 1):
            if instruction == "toggle":
                grid[row][col] = grid[row][col] ^ 1
            elif instruction == "turn on":
                grid[row][col] = 1
            elif instruction == "turn off":
                grid[row][col] = 0
            else:
                raise RuntimeError("Instructions unclear. Set house on fire")
    return grid


# %%
def parse_instruction(inst: str) -> Dict:
    """
    Take a line from the input data and return an instruction dictionary
    with start and end coordinates

    >>> parse_instruction("turn on 0,0 through 999,999")
    {'instruction': 'turn on', 'start': (0, 0), 'end': (999, 999)}
    >>> parse_instruction("toggle 0,0 through 999,0")
    {'instruction': 'toggle', 'start': (0, 0), 'end': (999, 0)}
    >>> parse_instruction("turn off 499,499 through 500,500")
    {'instruction': 'turn off', 'start': (499, 499), 'end': (500, 500)}
    """

    patt = re.compile(
        r"(?P<instruction>\w+\s*\w*) (?P<start>\d+,\d+) through(?P<end> \d+,\d+)"
    )
    match = re.match(patt, inst)
    match_dict = match.groupdict()
    for pos in ["start", "end"]:
        match_dict[pos] = tuple([int(i) for i in match_dict[pos].split(",")])
    return match_dict


# %%
if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Learned a painful lesson: Do not initialize a matrix via [[0] * 10] * 10
    # Each row in the matrix will be a reference to the first row created
    # So modifying a single element will apply to the entire column
    light_grid = [[0] * 1000 for i in range(1000)]
    data = load_input()
    for line in data:
        instr = parse_instruction(line)
        light_grid = do_instruction(
            instruction=instr["instruction"],
            grid=light_grid,
            start=instr["start"],
            end=instr["end"],
        )
    num_on = 0
    for row in light_grid:
        num_on += sum(row)
    print(num_on)


# %%

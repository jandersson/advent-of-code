import pathlib
from typing import Tuple


def handle_command(cmd: str, depth, h_pos, aim=None) -> Tuple:
    cmd = cmd.lower()
    dir, amt = cmd.split()
    amt = int(amt)
    if dir == "forward":
        if aim is not None:
            depth += aim * amt
        h_pos += amt
    elif dir == "up":
        if aim is not None:
            aim -= amt
        else:
            depth -= amt
    elif dir == "down":
        if aim is not None:
            aim += amt
        else:
            depth += amt
    else:
        raise RuntimeError("Out of Cheese Error. Redo From Start")
    return (depth, h_pos, aim)


def part_one(data: list) -> None:
    depth = 0
    h_pos = 0
    for command in data:
        res = handle_command(command, depth, h_pos)
        depth = res[0]
        h_pos = res[1]
    print(depth * h_pos)


def part_two(data: list) -> None:
    depth = 0
    h_pos = 0
    aim = 0
    for command in data:
        res = handle_command(command, depth, h_pos, aim)
        depth = res[0]
        h_pos = res[1]
        aim = res[2]
    print(depth * h_pos)


with open(pathlib.Path(__file__).parent / "input.txt") as infile:
    data = [line.strip() for line in infile.readlines()]
part_one(data)
part_two(data)

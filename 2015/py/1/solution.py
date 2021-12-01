from pathlib import Path

# TODO: Fix import issue
# from ..definitions import INPUT_PATH  #ImportError: attempted relative import with no known parent package

INPUT_PATH = Path("../../input")


def floor_sum(data, find_basement=False):
    level_up_counter = 0
    level_down_counter = 0
    for i, char in enumerate(data):
        if char == "(":
            level_up_counter += 1
        elif char == ")":
            level_down_counter += 1
        else:
            raise ValueError("Unidentified character: Only '(' or ')' allowed")

        if find_basement:
            if level_up_counter - level_down_counter + 1 == -1:
                return i
    return level_up_counter - level_down_counter


with open(INPUT_PATH / "1.txt") as infile:
    indata = infile.read()

basement_index = None

print("Part one!")
print(f"Santas delivery floor: {floor_sum(indata)}")
print("Part two!")
print(f"Index of basement floor: {floor_sum(indata, find_basement=True)}")
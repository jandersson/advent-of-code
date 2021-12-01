import math
import pathlib


def compute_slack(l, w, h):
    return min(l * w, w * h, h * l)


def compute_min_paper(l, w, h):
    return 2 * ((l * w) + (w * h) + (h * l))


def compute_paper(l, w, h):
    return compute_min_paper(l, w, h) + compute_slack(l, w, h)


assert compute_slack(1, 1, 10) == 1
assert compute_slack(2, 3, 4) == 6
assert compute_min_paper(2, 3, 4) == 52
assert compute_min_paper(1, 1, 10) == 42
assert compute_paper(2, 3, 4) == 58
assert compute_paper(1, 1, 10) == 43

data = []
with open(pathlib.Path(__file__).parents[2] / "input/2.txt") as infile:
    indata = infile.readlines()
    for i, line in enumerate(indata):
        line = line.strip().split("x")
        data.append(sorted([int(item) for item in line]))

paper = 0
ribbon = 0
for line in data:
    paper += compute_paper(line[0], line[1], line[2])
    ribbon += (sum(line[:2]) * 2) + math.prod(line)

print("First Solution!")
print(f"paper: {paper}")
print("Second Solution!")
print(f"ribbon: {ribbon}")

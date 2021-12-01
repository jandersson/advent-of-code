import pathlib

with open(pathlib.Path(__file__).parent / "input.txt") as infile:
    indata = infile.readlines()
data = [int(item) for item in indata]

memo = None
counter = 0
for item in data:
    if memo and memo < item:
        counter += 1
    memo = item
print(counter)

counter = 0
memo = 0
for idx in range(len(data) - 2):
    total = sum(data[idx : idx + 3])
    if memo and memo < total:
        counter += 1
    memo = total
print(counter)
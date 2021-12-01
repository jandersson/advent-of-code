import pathlib


def move(pos: tuple, dir: str) -> tuple:
    if direction == ">":
        return (pos[0], pos[1] + 1)
    if direction == "<":
        return (pos[0], pos[1] - 1)
    if direction == "^":
        return (pos[0] + 1, pos[1])
    if direction == "v":
        return (pos[0] - 1, pos[1])


with open(pathlib.Path(__file__).parents[2] / "input/3.txt") as infile:
    indata = infile.read()

visited = [(0, 0)]
for i, direction in enumerate(indata):
    visited.append(move(visited[i], direction))

print("First solution")
print(f"Number of houses that receive at least one gift: {len(set(visited))}")


robo_visited = [(0, 0)]
santa_visited = [(0, 0)]
for i, direction in enumerate(indata):
    if i % 2 == 0:
        santa_visited.append(move(santa_visited[-1], direction))
    else:
        robo_visited.append(move(robo_visited[-1], direction))

print("Second solution")
print(f"Number of houses that receive at least one gift: {len(set(robo_visited + santa_visited))}")

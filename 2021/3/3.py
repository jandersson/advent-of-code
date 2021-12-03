import pathlib


def transpose(matrix: list) -> list:
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


with open(pathlib.Path(__file__).parent / "input.txt") as infile:
    matrix = [list(number.strip()) for number in infile.readlines()]

gamma = ""
epsilon = ""
for x in transpose(matrix):
    num_ones = sum([int(y) for y in x])
    num_zeroes = len(x) - num_ones
    if num_ones > num_zeroes:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"
print(int(bin(int(gamma, 2) * int(epsilon, 2)), 2))

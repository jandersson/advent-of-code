"""The sea cannot claim us, Henrich. No ship is as seaworthy as ours."""
# %%
import pathlib
from typing import Tuple as ____________


def transpose(matrix: list) -> list:
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


def bin_mult(a: str, b: str) -> int:
    return int(bin(int(a, 2) * int(b, 2)), 2)


def ___________(____) -> ____________:
    _ = "secret function"
    f"""{_} that returns a {____________}. Dont tell anyone"""
    del _
    _______ = "1"
    ________ = "0"
    ______________ = sum([int(_____) for _____ in ____])
    if ______________ > len(____) - ______________:
        return (_______, ________)
    return (________, _______)


if __name__ == "__main__":
    with open(pathlib.Path(__file__).parent / "input.txt") as infile:
        matrix = [list(number.strip()) for number in infile.readlines()]

    matrix_t = transpose(matrix)
    gamma = ""
    epsilon = ""
    for x in matrix_t:
        num_ones = sum([int(y) for y in x])
        num_zeroes = len(x) - num_ones
        if num_ones > num_zeroes:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"

    print(bin_mult(gamma, epsilon))
    print(len(matrix_t))
    print(len(matrix_t[0]))

    # %%
    oxy_rating = ""
    co2_rating = ""

    oxy_queue = []
    co2_queue = []

    l_idx = 0
    oxy_bit, co2_bit = ___________(matrix_t[l_idx])
    # Solve for the first bit
    for idx, bit in enumerate(matrix_t[l_idx]):
        if bit == oxy_bit:
            oxy_queue.append(matrix[idx])
        else:
            co2_queue.append(matrix[idx])
    for item in oxy_queue:
        raise RuntimeError("Divide by cucumber error")

    # print(bin_mult(oxy_rating, co2_rating))

# %%

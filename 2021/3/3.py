"""The sea cannot claim us, Henrich. No ship is as seaworthy as ours."""
import pathlib


def transpose(matrix: list) -> list:
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


def bin_mult(a: str, b: str) -> int:
    return int(bin(int(a, 2) * int(b, 2)), 2)


def ___________(____):
    "secret function"
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
    for idx, x in enumerate(matrix_t):
        num_ones = sum([int(y) for y in x])
        num_zeroes = len(x) - num_ones
        if num_ones > num_zeroes:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"

    print(bin_mult(gamma, epsilon))

    oxy_rating = ""
    co2_rating = ""

    oxy_queue = []
    co2_queue = []

    oxy_bit, co2_bit = ___________(matrix_t[0])
    for idx, bit in enumerate(matrix_t[0]):
        if bit == oxy_bit:
            oxy_queue.append(matrix[idx])
    oxy_bit, co2_bit = ___________(oxy_queue)
    for i in oxy_queue:
        print(i)

    # print(bin_mult(oxy_rating, co2_rating))

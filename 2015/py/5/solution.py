# %%
import re
import string
import pathlib

ALPHABET = list(string.ascii_lowercase)


def num_vowels(instring) -> int:
    """Counts the number of vowels in a string"""
    vowels = r"[aieou]"
    return len(re.findall(vowels, instring))


def has_bad_strings(instring) -> bool:
    """Boolean that determines if a given string has 'bad' substrings"""
    bad_strings = ["ab", "cd", "pq", "xy"]
    return any(bad_string in instring for bad_string in bad_strings)


def has_doubles(instring):
    doubles = [char + char for char in string.ascii_lowercase]
    return any(double in instring for double in doubles)


def part_one_is_nice(instring):
    return (
        num_vowels(instring) > 2
        and not has_bad_strings(instring)
        and has_doubles(instring)
    )


assert not part_one_is_nice("aei")
assert part_one_is_nice("ugknbfddgicrmopn")
assert part_one_is_nice("aaa")
assert not part_one_is_nice("jchzalrnumimnmhp")
assert not part_one_is_nice("haegwjzuvuyypxyu")
assert not part_one_is_nice("dvszwmarrgswjxmb")

with open(pathlib.Path(__file__).parents[2] / "input/5.txt") as infile:
    data = [line.strip() for line in infile.readlines()]

num_nice = 0
for line in data:
    if part_one_is_nice(line):
        num_nice += 1

print("First Solution")
print(f"Number of nice lines: {num_nice}")

## Part 2

# %%


def split_into_pairs(instring):
    """
    >>> split_into_pairs("aaa")
    ['aa', 'aa']
    >>> split_into_pairs("aabaaz")
    ['aa', 'ab', 'ba', 'aa', 'az']
    """
    pairs = []
    for idx in range(len(instring) - 1):
        pairs.append(instring[idx] + instring[idx + 1])
    return pairs


def map_multi_pair_occurences(pairs: list):
    pair_dict = {}
    for pair in set(pairs):
        count = pairs.count(pair)
        if count > 1:
            pair_dict[pair] = count
    return pair_dict


def get_indices_of_pair(pairs: list, pair: str) -> list:
    return [i for i, x in enumerate(pairs) if x == pair]


def is_overlapping(indices: list) -> bool:
    """
    If any of the indices are next to each other then its an overlap

    >>> is_overlapping([3,4])
    True
    >>> is_overlapping([3,4,10])
    False
    >>> is_overlapping([0,1])
    True
    >>> is_overlapping([0,1,2])
    False
    """
    if len(indices) > 2:
        return False
    has_overlap = True
    for i in range(len(indices) - 1):
        if abs(indices[i] - indices[i + 1]) != 1:
            has_overlap = False
    return has_overlap


def has_multi_pair_without_overlap(instring: str) -> bool:
    """
    Checks the niceness string property of having multiple two letter pairs that do
    not overlap each other.

    >>> has_multi_pair_without_overlap("xyxy")
    True
    >>> has_multi_pair_without_overlap("aabcdefgaa")
    True
    >>> has_multi_pair_without_overlap("aaa")
    False
    """
    pairs = split_into_pairs(instring)
    pair_dict = map_multi_pair_occurences(pairs)
    if not pair_dict:
        return False
    for pair in list(pair_dict.keys()):
        if not is_overlapping(get_indices_of_pair(pairs, pair)):
            return True
    return False


def has_repeat_with_one_letter_between(instring: str) -> bool:
    """
    Checks the niceness string property of having at least one letter which repeats
    with exactly one letter between them.

    >>> has_repeat_with_one_letter_between("xyx")
    True
    >>> has_repeat_with_one_letter_between("abcdefeghi")
    True
    >>> has_repeat_with_one_letter_between("aaa")
    True
    """
    patts = [f"({char}[a-z]{char})" for char in string.ascii_lowercase]
    pattern = "|".join(patts)
    # TODO: This was fixed by switching match to findall. Why?
    if not re.findall(pattern, instring):
        return False
    return True


# %%
def part_two_is_nice(instring: str) -> bool:
    """
    Now, a nice string is one with all of the following properties:

    It contains a pair of any two letters that appears at least twice in the string
    without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).

    It contains at least one letter which repeats with exactly one letter between them, like xyx,
    abcdefeghi (efe), or even aaa.

    >>> part_two_is_nice("qjhvhtzxzqqjkmpb")
    True
    >>> part_two_is_nice("xxyxx")
    True
    >>> part_two_is_nice("uurcxstgmygtbstg")
    False
    >>> part_two_is_nice("ieodomkazucvgmuy")
    False
    >>> part_two_is_nice("aaabbgbbzbbb")
    True
    """
    return has_repeat_with_one_letter_between(
        instring
    ) and has_multi_pair_without_overlap(instring)


# %%
nice_list = []
print("Second solution")
for line in data:
    if part_two_is_nice(line):
        nice_list.append(line)
print(f"{len(nice_list)} nice strings :)")

if __name__ == "__main__":
    import doctest

    doctest.testmod()

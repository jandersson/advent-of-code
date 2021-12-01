import re
import string
import pathlib


def num_vowels(instring):
    vowels = r"[aieou]"
    return len(re.findall(vowels, instring))


def has_bad_strings(instring):
    bad_strings = ["ab", "cd", "pq", "xy"]
    return any(bad_string in instring for bad_string in bad_strings)


def has_doubles(instring):
    doubles = [char + char for char in string.ascii_lowercase]
    return any(double in instring for double in doubles)


def has_two_char_doubles(instring):
    # Think the memoization might be pointless since if its in the memo then it means we've hit
    # a second occurrence
    memo = {}
    for i in range(len(instring) - 1):
        pair = instring[i] + instring[i + 1]
        if pair in memo:
            continue
        else:
            count = instring.count(pair)
            if count > 1:
                return True
            else:
                memo[pair] = count
    return False


def has_repeat_with_middle(instring):
    patts = [f"{char}[^{char}]{char}" for char in string.ascii_lowercase]
    pattern = re.compile("|".join(patts))
    if re.match(pattern, instring):
        return True
    else:
        return False


def is_nice(instring):
    return num_vowels(instring) > 2 and not has_bad_strings(instring) and has_doubles(instring)


assert not is_nice("aei")
assert is_nice("ugknbfddgicrmopn")
assert is_nice("aaa")
assert not is_nice("jchzalrnumimnmhp")
assert not is_nice("haegwjzuvuyypxyu")
assert not is_nice("dvszwmarrgswjxmb")

with open(pathlib.Path(__file__).parents[2] / "input/5.txt") as infile:
    data = infile.readlines()

num_nice = 0
for line in data:
    if is_nice(line):
        num_nice += 1

print("First Solution")
print(f"Number of nice lines: {num_nice}")

assert has_two_char_doubles("aabcdefgaa")
assert has_two_char_doubles("xyxy")
assert not has_two_char_doubles("aaa")
assert has_two_char_doubles("qjhvhtzxzqqjkmpb")
assert has_two_char_doubles("xxyxx")
assert has_two_char_doubles("uurcxstgmygtbstg")
assert not has_two_char_doubles("ieodomkazucvgmuy")

assert has_repeat_with_middle("qjhvhtzxzqqjkmpb")

print("Second solution")

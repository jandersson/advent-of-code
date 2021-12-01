import hashlib

key = "iwrupvqb"
lowest_5_found = False
lowest_6_found = False
for i in range(100_000_000):
    dig = hashlib.md5((key + str(i)).encode("utf-8")).hexdigest()
    if dig[:5] == "00000" and not lowest_5_found:
        print(f"Five zeros: {i}")
        lowest_5_found = True
    if dig[:6] == "000000" and not lowest_6_found:
        print(f"Six zeros: {i}")
        lowest_6_found = True

    if lowest_6_found and lowest_5_found:
        break

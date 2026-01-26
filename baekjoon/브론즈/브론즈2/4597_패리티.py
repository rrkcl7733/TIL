import sys

for line in sys.stdin:
    line = line.strip()
    if line == "#":
        exit()

    bits = line[:-1]
    count_ones = bits.count("1")

    if line[-1] == "e":
        if count_ones % 2:
            print(bits + "1")
        else:
            print(bits + "0")
    else:
        if count_ones % 2:
            print(bits + "0")
        else:
            print(bits + "1")

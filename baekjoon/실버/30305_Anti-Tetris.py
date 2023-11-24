import re


def rot_90(blk):
    return [list(reversed(x)) for x in zip(*blk)]


h, w = map(int, input().split())
block = [list(input()) for _ in range(h)]
for _ in range(4):
    block = rot_90(block)
    if all(re.match(r"^#*\.*$", "".join(line)) for line in block):
        hh, ww = len(block[0]), len(block)
        print(1000, 1000)
        print("\n".join(["." * 1000] * (1000 - hh)))
        front = "#" * ((1000 - ww) // 2)
        back = "#" * (1000 - ww - (1000 - ww) // 2)
        print(front + f"{back}\n{front}".join("".join("." if c == "#" else "#" for c in line) for line in rot_90(block)) + back)
        exit()
print("impossible")

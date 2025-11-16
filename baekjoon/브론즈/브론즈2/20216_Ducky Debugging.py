import sys


for line in sys.stdin:
    line = line.rstrip("\n")

    if line == "I quacked the code!":
        break
    elif line.endswith("?"):
        print("Quack!", flush=True)
    elif line.endswith("."):
        print("*Nod*", flush=True)

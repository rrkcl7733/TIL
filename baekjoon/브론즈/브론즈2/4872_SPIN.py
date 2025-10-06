import sys


input_lines = sys.stdin.read().splitlines()
start = input_lines[0]
buttons = input_lines[1:]

wheels = [int(c) for c in start]

for button in buttons:
    for i in range(len(wheels)):
        wheels[i] = (wheels[i] + int(button[i])) % 10

print(*wheels, sep='')

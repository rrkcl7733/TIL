for _ in range(int(input())):
    n = int(input())
    intervals = [input().split() for _ in range(n)]
    results = []
    max_time = 0
    for interval in intervals:
        max_time = max(max_time, int(interval[2]))
    tape = []
    leds = [0] * 26
    for t in range(max_time):
        for letter, a, b in intervals:
            if int(a) <= t < int(b):
                leds[ord(letter) - ord('A')] = 1
            else:
                leds[ord(letter) - ord('A')] = 0

        on_leds = sum(leds)
        if on_leds > 0:
            tape.append(chr(ord('A') + on_leds - 1))
        else:
            tape.append('')

    print(''.join(tape))

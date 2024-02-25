for _ in range(int(input())):
    b, p = map(float, input().split())
    bpm = 60 * b / p

    print(f"{bpm - bpm / b:.5f} {bpm:.5f} {bpm + bpm / b:.5f}")

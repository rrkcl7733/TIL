import sys

data = sys.stdin.read().strip().split()
it = iter(data)
for n_str, k_str in zip(it, it):
    n = int(n_str)
    k = int(k_str)
    print(n + (n - 1) // (k - 1))

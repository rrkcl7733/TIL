import sys
input = sys.stdin.read
def main():
    data = input().split()
    N = int(data[0])
    T = int(data[1])
    arr = list(map(int, data[2:2+N]))
    
    iCow(arr, N, T)

def iCow(arr, N, T):
    output = []
    
    for _ in range(T):
        idx = findBiggest(arr, N)
        output.append(str(idx + 1))
        provide(arr, N, idx)
    
    sys.stdout.write("\n".join(output) + "\n")

def findBiggest(arr, N):
    max_val = -float('inf')
    idx = -1
    for i in range(N):
        if arr[i] > max_val or (arr[i] == max_val and idx > i):
            idx = i
            max_val = arr[i]
    return idx

def provide(arr, N, idx):
    tmp = arr[idx]
    div = tmp // (N - 1)
    rem = tmp % (N - 1)

    for i in range(N):
        if i != idx:
            arr[i] += div

    added = 0
    i = 0
    while added < rem:
        if i != idx:
            arr[i] += 1
            added += 1
        i += 1

    arr[idx] = 0

if __name__ == "__main__":
    main()

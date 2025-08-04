def next_iteration(lst):
    n = len(lst)
    return [abs(lst[i] - lst[(i + 1) % n]) for i in range(n)]

def all_equal(lst):
    return all(x == lst[0] for x in lst)

case_num = 1
while 1:
    N = int(input())
    if N == 0:
        exit()
    nums = list(map(int, input().split()))
    count = 0

    while not all_equal(nums):
        nums = next_iteration(nums)
        count += 1
        if count > 1000:
            break

    if count > 1000:
        print(f"Case {case_num}: not attained")
    else:
        print(f"Case {case_num}: {count} iterations")
    case_num += 1

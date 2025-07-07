seen = set()
count = 0
current = int(input())
while current not in seen:
    seen.add(current)
    count += 1
    mid = (current // 10) % 100
    current = mid * mid
    
print(count)

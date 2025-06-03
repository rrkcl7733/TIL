A, B, N = map(int, input().split())
best_cost = float('inf')

for _ in range(N):
    cost, route_length = map(int, input().split())
    route = list(map(int, input().split()))

    if A in route and B in route:
        if route.index(A) < route.index(B):
            best_cost = min(best_cost, cost)

if best_cost == float('inf'):
    print(-1)
else:
    print(best_cost)

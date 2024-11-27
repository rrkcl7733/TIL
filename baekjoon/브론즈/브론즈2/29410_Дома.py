N, a, b = map(int, input().split())
total_cost = 0
for _ in range(N):
    streets = list(map(int, input().split()))[1:]

    for house_number in streets:
        binary_representation = bin(house_number)[2:]
        total_cost += binary_representation.count('0') * a + binary_representation.count('1') * b
        
print(total_cost)

airports = [[int(i) for i in input().split()] for i in range(int(input()))]
print(min([sum([((x-a)**2 + (y-b)**2)**.5 for a,b in airports]) for x,y in airports]) / (len(airports)-1))

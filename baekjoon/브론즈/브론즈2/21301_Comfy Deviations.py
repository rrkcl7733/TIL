import math, statistics


temperatures = list(map(float, input().split()))
n = len(temperatures)
mean = sum(temperatures) / n
variance = statistics.variance(temperatures)
std_dev = math.sqrt(variance)
print("COMFY" if std_dev <= 1 else "NOT COMFY")

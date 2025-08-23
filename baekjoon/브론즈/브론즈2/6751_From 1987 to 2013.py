Y = int(input()) + 1
while not len(set(str(Y))) == len(str(Y)):
    Y += 1
print(Y)

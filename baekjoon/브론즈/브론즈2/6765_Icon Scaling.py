k = int(input())
for line in ["*x*", " xx", "* *"]:
    scaled_line = ''.join(char * k for char in line)
    for _ in range(k):
        print(scaled_line)
    

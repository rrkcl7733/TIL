blocks = {
    'A': ["***", "*.*", "***", "*.*", "*.*"],
    'B': ["***", "*.*", "***", "*.*", "***"],
    'C': ["***", "*..", "*..", "*..", "***"],
    'D': ["***", "*.*", "*.*", "*.*", "***"],
    'E': ["***", "*..", "***", "*..", "***"]
}

input()
block_rows = [""] * 5
for letter in input():
    block = blocks[letter]
    for i in range(5):
        block_rows[i] += block[i]
print(*block_rows, sep='\n')

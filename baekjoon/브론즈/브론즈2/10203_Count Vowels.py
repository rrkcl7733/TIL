vowels = {'a', 'e', 'i', 'o', 'u'}


for _ in range(int(input())):
    word = input()
    count = sum(1 for char in word if char in vowels)
    print(f'The number of vowels in {word} is {count}.')

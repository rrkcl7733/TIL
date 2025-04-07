vowels = [char for char in input() if char in 'aeiou']
print('S' if vowels == vowels[::-1] else 'N')

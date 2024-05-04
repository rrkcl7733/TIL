input_str = input()
digits = sorted([c for c in input_str if c.isdigit()], reverse=True)
letters = sorted([c for c in input_str if c.isalpha()])
    
password = ''.join([letters[i//2] if i % 2 == 0 else digits[i//2] for i in range(6)])
print(password)

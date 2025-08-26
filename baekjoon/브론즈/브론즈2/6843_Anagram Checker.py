from collections import Counter


phrase1 = input()
phrase2 = input()

if Counter(phrase1.replace(" ", "")) == Counter(phrase2.replace(" ", "")):
    print("Is an anagram.")
else:
    print("Is not an anagram.")

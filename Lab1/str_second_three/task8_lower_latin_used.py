def used_lower_latin(s):
    letters = set()
    for ch in s:
        if 'a' <= ch <= 'z':
            letters.add(ch)
    return letters

print(used_lower_latin("Hello, World! a b c"))
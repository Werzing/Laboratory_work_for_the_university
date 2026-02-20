# accent_check.py

n = int(input())
dictionary = set()
for _ in range(n):
    dictionary.add(input().strip())

text = input().strip().split()
errors = 0

for word in text:
    capitals = 0
    for ch in word:
        if ch.isupper():
            capitals += 1

    if word not in dictionary:
        if capitals != 1:
            errors += 1

print(errors)
# task1/polyglots.py

n = int(input())
all_langs = None          # множество языков, которые знают все
any_langs = set()         # множество языков, которые знает хотя бы один

for i in range(n):
    k = int(input())
    student_langs = set()
    for _ in range(k):
        lang = input().strip()
        student_langs.add(lang)
    if all_langs is None:
        all_langs = student_langs.copy()
    else:
        all_langs &= student_langs
    any_langs |= student_langs


print(len(all_langs))
for lang in sorted(all_langs):
    print(lang)

print(len(any_langs))
for lang in sorted(any_langs):
    print(lang)
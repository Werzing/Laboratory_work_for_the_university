def count_cyrillic(s):
    cnt = 0
    for ch in s:
        if ('а' <= ch <= 'я') or ('А' <= ch <= 'Я'):
            cnt += 1
    return cnt

print(count_cyrillic("Привет, мир!"))
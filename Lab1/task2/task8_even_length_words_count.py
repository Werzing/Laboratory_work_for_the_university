def count_even_length_words(s):
    words = s.split()
    count = 0
    for w in words:
        if len(w) % 2 == 0:
            count = count + 1
    return count

print(count_even_length_words("a bb ccc dddd"))
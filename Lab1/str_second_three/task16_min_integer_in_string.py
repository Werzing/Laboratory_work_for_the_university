def min_integer_in_string(s):
    numbers = []
    for word in s.split():
        if word.lstrip('-').isdigit() and word.count('-') <= 1:
            if word.startswith('-') and len(word) > 1:
                numbers.append(int(word))
            elif word.isdigit():
                numbers.append(int(word))

    return min(numbers) if numbers else None


print(min_integer_in_string("цена -50 руб, 20 долларов, 0"))  # -50

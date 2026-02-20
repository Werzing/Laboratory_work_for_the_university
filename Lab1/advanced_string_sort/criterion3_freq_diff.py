def sort_strings_by_criterion3(strings):
    rus_freq = {
        'о': 0.090, 'е': 0.072, 'а': 0.062, 'и': 0.062, 'н': 0.053,
        'т': 0.053, 'с': 0.045, 'р': 0.040, 'в': 0.038, 'л': 0.035,
        'к': 0.028, 'м': 0.026, 'д': 0.025, 'п': 0.023, 'у': 0.021,
        'я': 0.020, 'ы': 0.016, 'ь': 0.014, 'г': 0.013, 'з': 0.016,
        'б': 0.014, 'ч': 0.012, 'й': 0.010, 'х': 0.009, 'ж': 0.007,
        'ю': 0.006, 'ш': 0.006, 'ц': 0.004, 'щ': 0.003, 'э': 0.003,
        'ф': 0.002, 'ъ': 0.0002,
    }

    eng_freq = {
        'e': 0.12702, 't': 0.09056, 'a': 0.08167, 'o': 0.07507, 'i': 0.06966,
        'n': 0.06749, 's': 0.06327, 'h': 0.06094, 'r': 0.05987, 'd': 0.04253,
        'l': 0.04025, 'c': 0.02782, 'u': 0.02758, 'm': 0.02406, 'w': 0.02360,
        'f': 0.02228, 'g': 0.02015, 'y': 0.01974, 'p': 0.01929, 'b': 0.01492,
        'v': 0.00978, 'k': 0.00772, 'j': 0.00153, 'x': 0.00150, 'q': 0.00095,
        'z': 0.00074,
    }

    def most_freq_char(s):
        if not s:
            return 0, ''
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        max_cnt = max(freq.values())
        for ch, cnt in freq.items():
            if cnt == max_cnt:
                return cnt / len(s), ch
        return 0, ''

    def alphabet_freq(ch):
        """Частота символа в алфавите (0, если не буква)."""
        low = ch.lower()
        if 'а' <= low <= 'я':
            return rus_freq.get(low, 0.0)
        if 'a' <= low <= 'z':
            return eng_freq.get(low, 0.0)
        return 0.0

    def key_func(s):
        freq, ch = most_freq_char(s)
        if ch == '':
            return 0.0
        return freq - alphabet_freq(ch)


    return sorted(strings, key=key_func)



if __name__ == '__main__':
    test = ["hello", "привет", "aaabbb", "world", "тест"]
    print("Исходный:", test)
    result = sort_strings_by_criterion3(test)
    print("Отсортированный:", result)
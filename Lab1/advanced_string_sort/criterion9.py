
def max_ascii(s):
    """Максимальный ASCII-код символа в строке."""
    if not s:
        return 0
    return max(ord(ch) for ch in s)

def avg_mirror_diff(s):
    n = len(s)
    if n < 2:
        return 0
    total = 0
    for i in range(n // 2):
        total += abs(ord(s[i]) - ord(s[n - 1 - i]))
    return total / (n // 2)

def criterion9_key(s):
    if not s:
        return 0.0
    max_a = max_ascii(s)
    avg = avg_mirror_diff(s)
    return (max_a - avg) ** 2

def sort_by_criterion9(strings):
    return sorted(strings, key=criterion9_key)



if __name__ == '__main__':
    test = ["abc", "radar", "hello", "world", "aba"]
    print("Исходный:", test)
    result = sort_by_criterion9(test)
    print("Отсортированный:", result)

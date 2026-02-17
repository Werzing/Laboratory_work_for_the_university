
def max_triple_avg(s):
    if len(s) < 3:
        return 0
    max_avg = 0
    for i in range(len(s) - 2):
        avg = (ord(s[i]) + ord(s[i+1]) + ord(s[i+2])) / 3
        if avg > max_avg:
            max_avg = avg
    return max_avg

def sort_by_criterion11(strings):
    if not strings:
        return []
    ref = max_triple_avg(strings[0])
    def key_func(s):
        return (max_triple_avg(s) - ref) ** 2
    return sorted(strings, key=key_func)



if __name__ == '__main__':
    test = ["hello", "world", "python", "code", "abc"]
    print("Исходный:", test)
    result = sort_by_criterion11(test)
    print("Отсортированный:", result)
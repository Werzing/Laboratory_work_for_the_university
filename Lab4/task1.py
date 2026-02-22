import math

def solve_file(filename):
    with open(filename, 'r') as f:
        first = f.readline().split()
        if not first:
            return 0
        N = int(first[0])
        V = int(first[1])
        data = []
        for _ in range(N):
            d, p = map(int, f.readline().split())
            cnt = (p + V - 1) // V          # ceil(p / V)
            data.append((d, cnt))

    # сортировка по расстоянию
    data.sort(key=lambda x: x[0])
    dist = [x[0] for x in data]
    w    = [x[1] for x in data]
    n = len(data)

    # префиксные суммы
    pref_w  = [0] * (n + 1)
    pref_wd = [0] * (n + 1)
    for i in range(1, n + 1):
        pref_w[i]  = pref_w[i-1] + w[i-1]
        pref_wd[i] = pref_wd[i-1] + w[i-1] * dist[i-1]

    total_w  = pref_w[n]
    total_wd = pref_wd[n]
    min_cost = None

    for i in range(n):
        left_w  = pref_w[i]
        left_wd = pref_wd[i]
        wi = w[i]
        di = dist[i]

        cost_left  = di * left_w - left_wd
        right_w    = total_w - left_w - wi
        right_wd   = total_wd - left_wd - wi * di
        cost_right = right_wd - di * right_w
        total_cost = cost_left + cost_right

        if min_cost is None or total_cost < min_cost:
            min_cost = total_cost

    return min_cost

if __name__ == '__main__':
    res_a = solve_file('27-122a.txt')
    res_b = solve_file('27-122b.txt')
    print(res_a)
    print(res_b)
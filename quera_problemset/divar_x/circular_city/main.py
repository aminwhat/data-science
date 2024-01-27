(n, m) = list(map(int, input().split(" ")))
# n = direct streets
# m = circular streets

n_ways = list(map(int, input().split(" ")))  # direct streets ways
m_ways = list(map(int, input().split(" ")))  # circular streets ways

all_meets = (n * m) + 1


def calc_meets() -> int:
    direct_street_meets = 0
    circular_street_meets = 0
    for i in range(n):
        for j in range(i + 1, n):
            if n_ways[i] == n_ways[j]:
                direct_street_meets += 1

    for i in range(m):
        for j in range(i + 1, m):
            if m_ways[i] == m_ways[j]:
                circular_street_meets += 1

    return (direct_street_meets + circular_street_meets + 1) * 2


calculated_meets = calc_meets()

if calculated_meets == all_meets:
    print("YES")
else:
    print("NO")

from math import gcd

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0

    for l in range(n):
        g = a[l]
        cur = 0

        for r in range(l + 1, n):
            x = a[r]
            rem = x % g
            cost = min(rem, g - rem)
            cur = max(cur, cost)
            ans += cur
            g = gcd(g, x)

    print(ans)
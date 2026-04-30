def helper(arr):
    m = len(arr)

    d1 = [0] * m
    l, r = 0, -1

    for i in range(m):
        if i > r:
            k = 1
        else:
            k = min(d1[l + r - i], r - i + 1)

        while i - k >= 0 and i + k < m and arr[i - k] == arr[i + k]:
            k += 1
        d1[i] = k

        if i + k - 1 > r:
            l = i - k + 1
            r = i + k - 1

    d2 = [0] * m
    l, r = 0, -1

    for i in range(m):
        if i > r:
            k = 0
        else:
            k = min(d2[l + r - i + 1], r - i + 1)

        while i - k - 1 >= 0 and i + k < m and arr[i - k - 1] == arr[i + k]:
            k += 1
        d2[i] = k

        if i + k - 1 > r:
            l = i - k
            r = i + k - 1

    return d1, d2

def solve(arr, n) -> None:
    m = 2 * n
    d1, d2 = helper(arr)
    pos = [[] for _ in range(n)]

    for i, x in enumerate(arr):
        pos[x].append(i)

    buckets = [[] for _ in range(2 * m - 1)]

    for i, x in enumerate(arr):
        buckets[2 * i].append(x)

    for x in range(n):
        p, q = pos[x]
        if p > q:
            p, q = q, p
        s = p + q

        if s % 2 == 0:
            c = s // 2
            needed_radius = c - p + 1

            if d1[c] >= needed_radius:
                buckets[s].append(x)

        else:
            c = (s + 1) // 2
            needed_radius = c - p

            if d2[c] >= needed_radius:
                buckets[s].append(x)

    ans = 0

    for vals in buckets:
        seen = set(vals)
        mex = 0

        while mex in seen:
            mex += 1

        ans = max(ans, mex)

    print(ans)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        solve(arr, n)
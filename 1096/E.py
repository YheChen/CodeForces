def solve(arr, n) -> None:
    suffix_min = [0] * n
    suffix_min[-1] = arr[-1]

    for i in range(n - 2, -1, -1):
        suffix_min[i] = min(arr[i], suffix_min[i + 1])

    total = sum(arr)
    non_moving = sum(suffix_min)
    base = total - non_moving

    freq = {}
    best = 0

    for i in range(n):
        x = suffix_min[i]
        freq[x] = freq.get(x, 0) + 1

        count = freq.get(arr[i], 0)
        best = max(best, count)

    ans = base + max(0, best - 1)
    print(ans)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        solve(arr, n)
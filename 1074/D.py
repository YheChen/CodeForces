# t = int(input())
# for _ in range(t):
#     n, m, h = map(int, input().split())
#     a = list(map(int, input().split()))
#     original = a[:]
#     for _ in range(m):
#         b, c = map(int, input().split())
#         a[b - 1] += c
#         if a[b - 1] > h:
#             a = original[:]
#     print(" ".join(map(str, a)))
t = int(input())
for _ in range(t):
    n, m, h = map(int, input().split())
    original = list(map(int, input().split()))

    delta = [0] * n
    seen = [0] * n
    version = 1

    for _ in range(m):
        b, c = map(int, input().split())
        b -= 1

        if seen[b] != version:
            seen[b] = version
            delta[b] = 0

        delta[b] += c

        if original[b] + delta[b] > h:
            version += 1

    ans = []
    for i in range(n):
        if seen[i] == version:
            ans.append(original[i] + delta[i])
        else:
            ans.append(original[i])

    print(*ans)
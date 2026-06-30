t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    pref_sum = 0
    ok = True

    for i in range(n):
        pref_sum += b[i] - a[i]
        if pref_sum < 0:
            ok = False
            break
    print("YES" if ok else "NO")
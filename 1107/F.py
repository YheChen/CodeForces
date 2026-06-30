t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()
    l = 0

    while l < n and s[l] == '0':
        l += 1
    r = n - 1

    while r >= l and s[r] == '1':
        r -= 1
    ok = False
    i = l

    while i <= r:
        j = i

        while j <= r and s[j] == s[i]:
            j += 1
        length = j - i
        
        if length % 2 == 1:
            ok = True
        i = j

    print("Alice" if ok else "Bob")
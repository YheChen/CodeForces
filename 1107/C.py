t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()
    changes = 0
    for i in range(1, n):
        if s[i] != s[i - 1]:
            changes += 1
    if changes == 1:
        print(2)
    else:
        print(1)
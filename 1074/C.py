m = int(input())
for _ in range(m):
    n = int(input())
    lst = sorted(set(map(int, input().split())))
    
    best = 1
    curr = 1
    for i in range(1, len(lst)):
        if lst[i] == lst[i - 1] + 1:
            curr += 1
        else:
            best = max(best, curr)
            curr = 1
    best = max(best, curr)
    print(best)
        
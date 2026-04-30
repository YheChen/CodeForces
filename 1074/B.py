m = int(input())
for _ in range(m):
    n = int(input())
    lst = list(map(int, input().split()))
    print(max(lst) * n)
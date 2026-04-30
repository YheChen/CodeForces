def solve(arr) -> None:
    n = len(arr)
    div6 = []
    div2 = []
    notdiv = []
    div3 = []
    for i in range(n):
        item = arr[i]
        if item % 6 == 0:
            div6.append(item)
        elif item % 3 == 0:
            div3.append(item)
        elif item % 2 == 0:
            div2.append(item)
        else:
            notdiv.append(item)
    ans = div6 + div2 + notdiv + div3
    print(*ans)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        solve(arr)
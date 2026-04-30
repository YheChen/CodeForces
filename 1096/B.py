def solve(n: int, s: str) -> None:
    count = {"(": 0, ")": 0}
    for i in range(n):
        count[s[i]] += 1
    if count["("] == count[")"]:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = str(input())
        solve(n, s)
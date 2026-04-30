from typing import List

INF = 10**18


def solve(n: int, a: int, b: int, g: List[str]) -> int:
    if a == 0 and b == 0:
        ans = 0
        for i in range(n):
            for j in range(n):
                if g[i][j] != 'W':
                    ans += 1
        return ans

    dr, dc = b, a
    ans = 0

    for i in range(n):
        for j in range(n):
            if i - dr >= 0 and j - dc >= 0:
                continue

            dp0, dp1 = 0, INF
            r, c = i, j

            while r < n and c < n:
                ch = g[r][c]
                ndp0, ndp1 = INF, INF

                if ch == 'W':
                    if dp0 < INF:
                        ndp0 = dp0

                elif ch == 'B':
                    if dp1 < INF:
                        v = dp1 + 1
                        ndp0 = min(ndp0, v)
                        ndp1 = min(ndp1, v)

                else:
                    if dp0 < INF:
                        v = dp0 + 1
                        ndp0 = min(ndp0, v)
                        ndp1 = min(ndp1, v)
                    if dp1 < INF:
                        ndp0 = min(ndp0, dp1)

                dp0, dp1 = ndp0, ndp1
                r += dr
                c += dc

            best = min(dp0, dp1)
            if best >= INF:
                return -1
            ans += best

    return ans


def main() -> None:
    t = int(input())
    for _ in range(t):
        n, a, b = map(int, input().split())
        g = [input().strip() for _ in range(n)]
        print(solve(n, a, b, g))


if __name__ == "__main__":
    main()
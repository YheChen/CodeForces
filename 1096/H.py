def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        g = [[] for _ in range(n + 1)]

        for _ in range(n - 1):
            u, v = map(int, input().split())
            g[u].append(v)
            g[v].append(u)
        
        root = 1
        for i in range(1, n + 1):
            if len(g[i]) > 1:
                root = i
                break
        parent = [0] * (n + 1)
        parent[root] = -1
        order = [root]

        # Iterative DFS order.
        for u in order:
            for v in g[u]:
                if v == parent[u]:
                    continue
                parent[v] = u
                order.append(v)

        cnt = [0] * (n + 1)
        total_leaves = 0
        base = 0

        for u in reversed(order):
            if len(g[u]) == 1:
                cnt[u] = 1
                total_leaves += 1
            else:
                for v in g[u]:
                    if parent[v] == u:
                        cnt[u] += cnt[v]

            if u != root and cnt[u] % 2 == 1:
                base += 1

        if total_leaves % 2 == 0:
            print(base)
            continue

        adjust = [0] * (n + 1)

        for u in order:
            for v in g[u]:
                if parent[v] == u:
                    if cnt[v] % 2 == 1:
                        change = -1
                    else:
                        change = 1

                    adjust[v] = adjust[u] + change

        ans = 10**18

        for u in range(1, n + 1):
            if len(g[u]) == 1:
                ans = min(ans, base + adjust[u])

        print(ans)
    
if __name__ == "__main__":
    solve()
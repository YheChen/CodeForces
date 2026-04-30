n = int(input())
for _ in range(n):
    m = int(input())
    output = []
    for i in range(1, m + 1):
        output.append(i)
    print(" ".join(map(str, output)))

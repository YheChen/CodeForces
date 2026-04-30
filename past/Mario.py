n = int(input())
for _ in range(n):
    m = int(input())
    mini = maxi = 0
    s  = str(input())
    s1 = list(s)
    s2 = s1[:]
    for i in range(1, m - 1):
        if s1[i - 1] == '1' and s1[i + 1] == '1':
            s1[i] = '1'
        if s2[i - 1] == '1' and s2[i + 1] == '1':
            s2[i] = '0'
    for i in range(m):
        if s2[i] == '0':
            mini += 1
        if s1[i] == '1':
            maxi += 1
        
    print(mini, maxi)
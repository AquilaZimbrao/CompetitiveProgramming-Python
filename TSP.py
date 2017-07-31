
N = 20
inf = 12345678

dis = [[0]*N]*N
pd = [[0]*N] * (1 << N)
n = 30
s = 50

def f(x, mask):
    if (mask == (1 << n) - 1 and x == s):
        return 0
    if (pd[x][mask] != -1):
        return pd[x][mask]

    pd[x][mask] = inf
    for i in range(n):
        if (dis[x][i] == inf):
            continue
        pd[x][mask] = min(pd[x][mask], dis[x][i] + f(i, mask | (1 << i)))

    return pd[x][mask]




pd = map(-1,pd)
f(s, 1 << s)

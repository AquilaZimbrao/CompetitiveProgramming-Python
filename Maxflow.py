import math
MAXN = 100500

f = [[0]*MAXN]*MAXN
g = [[0]*MAXN]*MAXN
pai = [0]*MAXN
n = 0



def bfs(source, sink,):
    q = list()
    global pai
    pai = map(-1,pai)
    q.append(source)

    pai[source] = source
    while(len(q) > 0):
        x = q[len(q)-1]
        q.remove(len(q)-1)
        for i in range(len(q)):
            y = q[x][i]
            if(f[x][y] > 0 and pai[y] == -1):
                q.append(y)
                pai[y] =x
    return (pai[sink] != -1)


def maxflow(source, sink):
    flow =0
    while(bfs(source,sink)):
        garg = math.inf
        v = sink
        while(v != source):
            garg = min(garg, f[pai[v]][v])
            v = pai[v]
        flow += garg
        v = sink
        while(v != source):
            f[pai[v]][v] -= garg
            f[v][pai[v]] += garg
            v = pai[v]
    return flow


n = int(input())
m = int(input())

for i in range(n):
    x, y, c = [(int (a)) for a in input().split(' ')]
    g[x].append(y)
    g[y].append(x)
    f[x][y] += c
    fluxo = maxflow(0, n - 1)



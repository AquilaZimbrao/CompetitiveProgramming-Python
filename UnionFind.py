MAXN = 100000

pai = [0]*MAXN
rank = [0]*MAXN


def findc(x):
    if (pai[x] == x):
        return x

    pai[x] = findc(pai[x])
    return pai[x]


def junta(x, y):
    gX = findc(x)
    gY = findc(y)

    if (rank[gX] > rank[gY]):
        pai[gY] = gX
    elif(rank[gY] > rank[gX]):
        pai[gX] = gY
    else:
        pai[gY] = gX
        rank[gX]+=1

MAXN = 50000


def last(x):
    return x & (-x)


v = [0] * MAXN
ft = [[0] * MAXN]*MAXN


def update(pos, valor):
    noX = pos
    while (noX < MAXN):
        noY = noX
        while(noY < MAXN):
            ft[noX][noY] = max(ft[noX][noY],valor)
            noY += last(noY)
        noX += last(noX)


def query(pos):
    maior = -232
    noX = pos
    while (noX > 0):
        noY = noX
        while (noY > 0):
            maior = max(ft[noX][noY], maior)
            noY -= last(noY)
        noX -= last(noX)

    return maior

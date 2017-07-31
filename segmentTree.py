MAXN = 100000

v = [0]*MAXN
st = [-1] * (4 * MAXN)

def build(no, l, r):
    if (l == r):
        st[no] = v[l]
        return

    noL = 2 * no
    noR = 2 * no + 1
    mid = (l + r) / 2

    build(noL, l, mid)
    build(noR, mid + 1, r)
    st[no] = st[noL] + st[noR]

def  update(no,l, r, pos,valor):
    if (not (l <= pos and pos <= r)):
        return

    if (l == r and l == pos):
        st[no] = valor
        return

    noL = 2 * no
    noR = 2 * no + 1
    mid = (l + r) / 2
    update(noL, l, mid, pos, valor)
    update(noR, mid + 1, r, pos, valor)
    st[no] = st[noL] + st[noR]


def query(no, l, r, i, j):
    if (l > j or r < i):
        return 0

    if (l >= i and r <= j):
        return st[no]

    noL = 2 * no
    noR = 2 * no + 1
    mid = (l + r) / 2
    vL = query(noL, l, mid, i, j)
    vR = query(noR, mid + 1, r, i, j)
    return vL + vR

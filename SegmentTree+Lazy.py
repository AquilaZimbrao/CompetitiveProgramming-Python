MAXN = 100000

v = [0] * MAXN
st = [-1] * (4 * MAXN)
lz = [0] * (4 * MAXN)

def prop(no, noL,noR, l, r, mid):
    lz[noL] += lz[no]
    lz[noR] += lz[no]
    st[noL] += lz[no] * (mid - l + 1)
    st[noR] += lz[no] * (r - (mid + 1) + 1)
    lz[no] = 0

def update(no, l, r, posL, posR, valor):
    if (posL > r and posR < l):
        return

    if (posL <= l and r <= posR):
        st[no] += (r - l + 1) * valor
        lz[no] += valor
        return

    noL = 2 * no
    noR = 2 * no + 1
    mid = (l + r) / 2
    prop(no, noL, noR, l, r, mid)
    update(noL, l, mid, posL, posR, valor)
    update(noR, mid + 1, r, posL, posR, valor)
    st[no] = st[noL] + st[noR]


def query(no, l, r, i, j):
    if (l > j or r < i):
        return 0

    if (l >= i and r <= j):
        return st[no]

    noL = 2 * no
    noR = 2 * no + 1
    mid = (l + r) / 2
    prop(no, noL, noR, l, r, mid)
    vL = query(noL, l, mid, i, j)
    vR = query(noR, mid + 1, r, i, j)
    return vL + vR

MAXN = 100500


valor = [0]*MAXN
peso = [0]*MAXN
pd = [[0]*MAXN]*MAXN
n = 500


def mochila(disp, item):
    if (disp == 0):
        return 0

    if (item == n):
        return 0

    if (pd[disp][item] != -1):
        return pd[disp][item]

    if (peso[item] <= disp):
        pd[disp][item] = max(mochila(disp, item+1), valor[item]+mochila(disp-peso[item], item+1))
    else:
        pd[disp][item] = mochila(disp, item+1)

    return pd[disp][item]

MAXN = 100500

valor = [0]*MAXN
peso = [0]*MAXN
n = 50
pd = [[-1]*MAXN]*MAXN

def mochila(disp, item):
    if disp == 0 or item == 0:
        return 0

    if pd[disp][item] != -1:
        return pd[disp][item]

    if peso[item] <= disp:
        pd[disp][item] = max(mochila(disp,item+1), valor[item]+mochila(disp-peso[item], item+1))
    else:
        pd[disp][item] = mochila(disp, item+1)

    return pd[disp][item]


resp = list()

def rec(disp, item):
    if disp == 0 or item == 0:
        return None

    if (peso[item] <= disp):
        if (mochila(disp, item+1) == pd[disp][item]):
            rec(disp, item+1)
        else:
            resp.append(item)
            rec(disp-peso[item], item+1)
    else:
        rec(disp, item+1)



MAXN = 100500

valor = [0]*MAXN
peso = [0]*MAXN
n = 50
pd = [-1]*MAXN

def mochila(disp):
    if (disp == 0):
        return 0

    if (pd[disp] != -1):
        return pd[disp]

    pd[disp] = 0
    for i in range(n):
        if (peso[i] <= disp):
            pd[disp] = max(pd[disp], valor[i]+mochila(disp-peso[i]))

    return pd[disp]




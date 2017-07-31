import math
maxn = 100100
logn = 20

n = 0
v = [0]*maxn
pd = [[0]*logn]*maxn

def calc():
    for i in range(n):
        pd[i][0] = v[i]

    for j in range(logn+1)[1:]:
        for i in range(n):
            i2 = min(n-1, i+(1 << (j-1)))
            pd[i][j] = min(pd[i][j-1], pd[i2][j-1])


def getMin(l, r):
    pot = math.log(r - l + 1,2)
    ans = min(pd[l][pot], pd[r - (1 << pot) + 1][pot])
    return ans




n = int(input())

for i in range(n):
    v[i] = int(input())
calc()
m = getMin(l, r)

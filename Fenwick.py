MAXN = 50000

def last(x):
    return x & (-x)

v = [0]*MAXN
ft = [0]*MAXN

def update(pos,valor):
    no = pos
    while(no < MAXN):
        ft[no] += valor
        no += last(no)

def query(pos):
    soma = 0
    no = pos
    while(no > 0):
        soma += ft[no]
        no -= last(no)

    return soma

n = int(input())

for i in range(n):
    v[i] = int(input())
    update(i,v[i])
    
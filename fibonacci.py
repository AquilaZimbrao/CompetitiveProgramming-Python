MAXN = 100002

pd = [-1]*MAXN

def fib(n):
    if(n<=1):
        return 1
    if(pd[n] != -1):
        return pd[n]

    pd[n] = fib(n-1)+fib(n-2)
    return pd[n]



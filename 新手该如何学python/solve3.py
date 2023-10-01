# solve3.py
def A(n, m):
    " [排列]组合 "
    # n! / (n-m)!
    res = 1
    # n!
    for i in range(1, n+1):
        res *= i
    # / (n-m)!
    for i in range(1, n-m+1):
        res /= i
    return res

def C(n, m):
    " 排列[组合] "
    return A(n, m) / A(n, n)

print(A(4, 8), )

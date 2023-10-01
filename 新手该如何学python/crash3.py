# crash3.py
# 这次是一个错误结果
def A(n, m):
    " [排列]组合 "
    # n! / (n-m)!
    res = 1
    # n!
    for i in range(n+1):
        res *= i
    # / (n-m)!
    for i in range(n-m+1):
        res /= i
    return res

def C(n, m):
    " 排列[组合] "
    return A(n, m) / A(n, n)

print(A(4, 8), )

"""
为什么会是0呢，进入crash3_2看看
（虽说这个错误很明显。。。）
"""

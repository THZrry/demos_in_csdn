# crash3_2.py
# 这次是一个错误结果
def A(n, m):
    " [排列]组合 "
    # n! / (n-m)!
    res = 1
    # n!
    print("before", res)
    for i in range(n+1):
        res *= i
        print("n!", i, res)
    # / (n-m)!
    for i in range(n-m+1):
        res /= i
        print("(n-m)!", i, res)
    return res

def C(n, m):
    " 排列[组合] "
    return A(n, m) / A(n, n)

print(A(4, 8), )

"""
加完print一运行，立马就知道问题了，你就能很快把它改对了。
"""

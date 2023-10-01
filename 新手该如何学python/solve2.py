# solve2.py
prices_ = {"apple": 1, "banana": 1, "watermelon": 4, "haoge's watermelon": 5, \
           "grape": 1, "badapple": 4}
PRICE = 1 # 要卖光的价格

# 法一
prices = prices_.copy() # 为了演示两种方法，copy了一个，现实中没必要
change_list = []
for fruit, price in prices.items():
    if price == PRICE:
        #del prices[fruit] # NO
        change_list.append(fruit) # 加入待删列表
for fruit in change_list:         # 开始删除
    del prices[fruit]
print(prices) # 成功。



# 法二
prices = prices_.copy()
for fruit, price in tuple(prices.items()): # list也可以
    if price == PRICE:
        del prices[fruit]

print(prices) # 成功。

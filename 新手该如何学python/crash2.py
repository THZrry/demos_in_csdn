# crash2.py
# 注：此事由真实事件改编。
# 卖光某一价格的水果
prices = {"apple": 1, "banana": 1, "watermelon": 4, "haoge's watermelon": 5, \
          "grape": 1, "badapple": 4}
PRICE = 1 # 要卖光的价格

for fruit, price in prices.items():
    if price == PRICE:
        del prices[fruit]

print(prices)

"""
Traceback (most recent call last):
  File "1145141919810新手该如何学python\crash2.py", line 6, in <module>
    for fruit, price in prices.items():
RuntimeError: dictionary changed size during iteration
你能直接看懂它， 字典在iteration(遍历)期间大小改变了，进而想到你删了一些键，那要么你
  先把它整进一个列表里，要么你先想想，反正没遍历到的键值又不会变，干脆在访问前把它
  “固化”下来不就是了，于是你就能把它改成 for fruit, price in tuple(prices.items())
  当然，前提是你了解了足够的与迭代器有关的知识
"""

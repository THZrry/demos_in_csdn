# crash1.py
bdata = b'\xd4\xad\xc9\xf1\xa3\xbf\xc6\xf4\xb6\xaf\xa3\xa1'

print(bdata.decode())

"""
Traceback (most recent call last):
  File "1145141919810\新手该如何学python\crash1.py", line 4, in <module>
    print(bdata.decode())
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xc9 in position 2: invalid\
  continuation byte

解释一下：
【Traceback (most recent call last):】 错误栈（不用管）
  【File "1145141919810\新手该如何学python\crash1.py", line 4, in <module>】*1
    【print(bdata.decode())】*2
【UnicodeDecodeError: 'utf-8' codec can't decode byte 0xc9 in position 2:invalid
  continuation byte】*3

*1：出错文件，行数。如果这个文件不是你写的，有可能是它本身有BUG（低概率）或你调用出错
    了。
*2：出错代码。仔细看看哪里不对，我是py3.6， 新版本或ipython会有更好的提示。
*3：错误类型。冒号前是错误类型，后面是（较）详细的信息。搜索时把这行复制上去效果最好。
"""

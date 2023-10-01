# solve1.py
bdata = b'\xd4\xad\xc9\xf1\xa3\xbf\xc6\xf4\xb6\xaf\xa3\xa1'

# 解决方法1
# 尝试换成本地语言，即中文专用编码，如gbk(cp936)、gb2312、BIG5之类的。
print(bdata.decode("gbk"))

print()

# 解决方法2
# 使用chardet模块分析编码。
# 安装：pip install chardet -i https://pypi.tuna.tsinghua.edu.cn/simple/
import chardet
res = chardet.detect(bdata)
print(res) # {'encoding': 编码, 'confidence': 正确概率, 'language': 语言}
print(bdata.decode(res["encoding"])) # 当然，这个例子不太好因为它失败了
# 如果你没安装chardet肯定会报错，那么请你自己搜索试试解决。

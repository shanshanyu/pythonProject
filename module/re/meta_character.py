'''
2024/3/25 21:40

元字符

\w 表示匹配字母、数字、下划线
\S 匹配任意非空字符
上述两者有什么区别？
\S 的范围更广，比如 @ 这种特殊字符属于 \S，但是不属于 \w

'''
import re

prog = re.compile(r'\S')

res = prog.match('@')
print(res)

prog1 = re.compile(r'\w')
res1 = prog1.match('@')
print(res1)
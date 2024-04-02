'''
create_time: 2024/3/28 17:44
author: yss
version: 1.0

class collections.defaultdict(default_factory=None, /[, ...])

如果 default_factory 属性为 None，则调用本方法会抛出 KeyError 异常，附带参数 key。

如果 default_factory 不为 None，则它会被（不带参数地）调用来为 key 提供一个默认值，这个值和 key 作为一对键值对被插入到字典中，并作为本方法的返回值返回。
'''



from collections import defaultdict


def main():
    s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
    d = defaultdict(list)
    for k, v in s:
    # print(k)
    # print(v)
        d[k].append(v)
    print(d,type(d))   #<class 'collections.defaultdict'>  d 是一个 defaultdict 类型的对象
    print(d.items())  #把一个字典转换成了 [(),(),()] 列表嵌套元组的形式


if __name__ == '__main__':
    main()


import re


def replace_char(sentence):
    res = re.sub(r'fuck|shit|[傻煞沙][比笔逼叉缺吊碉雕]','*',sentence,flags=re.IGNORECASE)
    print(res)


def main():
    sentence = '你是傻逼吗'
    replace_char(sentence)

if __name__ == '__main__':
    main()
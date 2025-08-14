import re

def split_str(sentence):
    sentence_list = re.split(r'[，。]',sentence)
    sentence_list = [sentence for sentence in sentence_list if sentence]  #去除列表中的空白项
    print(sentence_list)


def main():
    sentence = '窗前明月光，疑是地上霜。举头望明月，低头思故乡。'
    split_str(sentence)


if __name__ == '__main__':
    main()
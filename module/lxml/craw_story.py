#抓取小说数据
import requests
from lxml import etree


def crawl_story(url,text_name):
    HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

    while len(url) > 0 and url != 'https://www.85xs.cc/book/douluodalu1':
        try:
            # 访问url，获取响应
            response = requests.get(url, headers=HEADERS)
            response.encoding = 'utf-8'

            e = etree.HTML(response.text)  # 获得一个etreeElement对象

            # 获取文本
            info = ''.join(e.xpath('//div[@class="m-post"]/p/text()'))
            title = '\n'.join(e.xpath('//h1/text()'))
            #写入数据
            with open(text_name,'a',encoding='utf-8') as f:
                f.write(title+'\n'+info+'\n\n')

            url = 'https://www.85xs.cc' + e.xpath('/html/body/div/div[2]/table[1]/tbody/tr/td[2]/a/@href')[0]
            print(title+'抓取完成！')
        except Exception as e:
            print(e)


def main():
    URL = 'https://www.85xs.cc/book/douluodalu1/1.html'
    TXT_NAME = '斗罗大陆.txt'
    crawl_story(URL,TXT_NAME)


if __name__ == '__main__':
    main()




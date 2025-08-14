import requests

def send_msg(tel,content):
    res = requests.post(url='http://sms-api.luosimao.com/v1/send.json',
                  auth=('api','key-454c96724389160d5e7ed3bc89c44d94'),
                  data={'mobile':tel,'message':content},
                  timeout=10,
                  verify=False
                  )
    return res.json()


def main():
    phone = '15375456189'
    content = '短信验证码是 {1234},不要给别人看奥【铁壳测试】'
    print(send_msg(tel=phone,content=content))


if __name__ == '__main__':
    main()

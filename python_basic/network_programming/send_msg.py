'''
create_time: 2024/5/22 10:19
author: yss
version: 1.0

desc: 发送短信
建立连接->发送请求->获取响应->关闭连接
'''
import urllib.parse
import http.client


def main():
    host = "106.ihuyi.com"
    sms_send_uri = "/webservice/sms.php?method=Submit"
    # 下面的参数需要填入自己注册的账号和对应的密码
    params = urllib.parse.urlencode({'account': 'C84085902', 'password':'65981eaf4e405f8bc45de5a188ca7ede',
                                     'content': '您的验证码是：0000。请不要把验证码泄露给其他人。',
                                     'mobile': '15375456189', 'format': 'json'})
    headers = {'Content-type': 'application/x-www-form-urlencoded', 'Accept': 'text/plain'}

    conn = http.client.HTTPConnection(host, port=80, timeout=30)
    conn.request('POST', sms_send_uri, params, headers)  # 方法，url，请求体，请求头
    response = conn.getresponse()
    response_str = response.read().decode('utf-8')
    print(response_str)
    conn.close()


if __name__ == '__main__':
    main()
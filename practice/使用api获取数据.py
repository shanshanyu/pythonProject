import requests

def main():
    ret = requests.get('https://apis.tianapi.com/tianqishiju/index?key=d3838c975aed394cad6c84d393162a27')
    if ret.status_code == 200:
        data = ret.json()
        print(data['result'])
        print(type(data['result']))
        for k,v in data['result'].items():
            print(k,v)

if __name__ == '__main__':
    main()
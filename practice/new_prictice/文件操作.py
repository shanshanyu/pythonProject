def main():
    f = open('craps.py','r',encoding='utf-8')
    lines = f.readlines()
    for line in lines:
        print(line,end='')



if __name__ == '__main__':
    main()
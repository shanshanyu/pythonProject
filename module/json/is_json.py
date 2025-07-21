import json

def is_file_all_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line:  # 忽略空行
                    json.loads(line)
        return True
    except (json.JSONDecodeError, UnicodeDecodeError):
        return False

def main():
    ret = is_file_all_json('../json/test.json')
    if ret:
        print('yes')
    else:
        print('no')

if __name__ == '__main__':
    main()
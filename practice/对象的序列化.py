import json

my_dict = {
    'name': '骆昊',
    'age': 40,
    'friends': ['王大锤', '白元芳'],
    'cars': [
        {'brand': 'BMW', 'max_speed': 240},
        {'brand': 'Audi', 'max_speed': 280},
        {'brand': 'Benz', 'max_speed': 280}
    ]
}


with open('craps1.py','w') as f1:
   json.dump(my_dict,f1)


with open('craps1.py','r') as f1:
    ret = json.load(f1)
    print(ret)
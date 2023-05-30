'''
create_time: 2023/5/30 10:19
author: yss
version: 1.0
'''

goods = []  #用列表加字典的方式进行存储

def insert_goods():
    while True:
        input_goods = input('请输入商品编号和商品名称进行入库，每次只能输入一件商品，例：1001  手机 ：')
        if input_goods == 'q':
            break
        num,val = input_goods.split()
        tmp = {num:val}  #通过花括号创建的字典 key 可以是表达式，通过 dict(key=val)，key不能是表达式
        goods.append(tmp)

def display_goods():
    for item in goods:  #遍历列表，列表中的每个元素是一个字典
        for i,j in item.items():  #遍历字典，获取每个字典的元素的 k,v
            print(i,j)

def purchase_goods():
    shop_lst = []
    while True:
        shop = input('请输入要购买的商品编号：')
        if shop == 'q':
            break

        #查找的时候加个标志，避免查找全部
        flag = False
        for item in goods:
            for key in item:
                if key == shop:
                    shop_lst.append({key:item[key]})
                    flag = True
        if flag:
            print('商品已添加到购物车')
        else:
            print('没有找到该商品')




    print(shop_lst)


if __name__ == '__main__':
    insert_goods()
    purchase_goods()
    display_goods()

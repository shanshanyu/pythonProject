'''
create_time: 2023/5/30 09:55
author: yss
version: 1.0
'''

year = [82,89,88,86,85,00,99]

new_year = []

#千年虫实现方法一
for i in year:
    if i == 0:
        tmp = int('200'+str(i))
    else:
        tmp = int('19'+str(i))

    new_year.append(tmp)

print(year)
print(new_year)

#用 enumerate 方法实现

for i,ele in enumerate(year):
    if ele != 0:
        year[i] += 1900
    else:
        year[i] += 2000
print(year)

print(str(00))  # 0



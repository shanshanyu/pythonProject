'''斐波那契额数列前20个数'''

a,b = 0,1
for _ in range(20):
    print(a)
    a,b = b,a+b


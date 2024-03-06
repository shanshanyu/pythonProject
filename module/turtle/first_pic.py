'''
create_time: 2024/3/5 10:17
author: yss
version: 1.0
'''
import turtle

for steps in range(100):
    for c in ('blue', 'red', 'green'):
        turtle.color(c)
        turtle.forward(steps)
        turtle.right(30)


turtle.mainloop()

# -*- coding:utf-8 -*-
#简单的对python中的数据进行学习。
#先写一个冒泡算法
a = [15,21,35,48,12]
for waiceng in range(len(a)):
    for neiceng in range(len(a)-waiceng-1):
        if a[neiceng] >a[neiceng+1]:
            val=a[neiceng]
            a[neiceng] = a[neiceng+1]
            a[neiceng+1] =val
for x in range(len(a)):
    print(a[x])
    
# -*- coding: utf-8 -*-
# @Time     : 2018/1/21 8:34
# @Author   : ice
# @File     : step_study.py
# @Software : PyCharm


def step(num):
    count = 0
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    else:
        for item in range(1, num, 1):
            count += step(num - item)
        count += 1
    return count


if __name__ == '__main__':
    print step(4)
    # for i in range(1,5, 1):
    #     print(i)
    fib = lambda n: n if n < 2 else 2 * fib(n - 1)
    print(fib(4))

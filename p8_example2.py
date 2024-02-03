# -*- coding: utf-8 -*-
# @Time    : 2024/2/4 2:51
# @Author  : listem
# @FileName: p8_example2.py
# @Software: PyCharm

def find_divisor(n):
    """
    分解质因数
    找了该数的所有factor 包括1和它自己
    :param n:
    :type n:
    :return:
    :rtype:
    """
    divisor = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisor.append(i)

    return divisor


# B版 数论 例2
def verify_form(lis: list, n: int):
    mul_numpy = 1
    for i in lis:
        mul_numpy *= i

    # print(mul_numpy ** 2)
    # print(n ** len(lis))
    return mul_numpy ** 2 == n ** len(lis)


if __name__ == '__main__':
    print(all([verify_form(find_divisor(i), i) for i in range(1000)]))  # 例2

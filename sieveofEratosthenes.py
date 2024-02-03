# -*- coding: utf-8 -*-
# @Time    : 2024/2/4 1:15
# @Author  : listem
# @FileName: sieveofEratosthenes.py
# @Software: PyCharm
import math

"""
输入：整数n > 1
 
设A为布尔值矩阵，下标是2至n的整数，
初始时全部设成true。
 
 for i = 2, 3, 4, ..., 不超过
�
{\displaystyle {\sqrt {n}}}：
  if A[i]为true：
    for j = i2, i2+i, i2+2i, i2+3i, ..., 不超过n：
      A[j] := false
 
输出：使A[i]为true的所有i。

https://zh.wikipedia.org/wiki/%E5%9F%83%E6%8B%89%E6%89%98%E6%96%AF%E7%89%B9%E5%B0%BC%E7%AD%9B%E6%B3%95
"""


def eratosthenes(number: int):
    is_prime = [True] * (number + 1)  # 步骤1：初始化数组，默认都是质数
    is_prime[0] = is_prime[1] = False  # 0和1不是质数，将其标记为False

    for i in range(2, int(math.sqrt(number)) + 1):  # 步骤2 标记根号number下的所有数
        if is_prime[i]:
            for j in range(i * i, number + 1, i):  # 从i^2开始 把所有是素数倍数的数字筛掉
                is_prime[j] = False

    primes = [i for i in range(2, number + 1) if is_prime[i]]  # 返回所有满足条件的素数

    return primes


if __name__ == '__main__':
    print(eratosthenes(100))

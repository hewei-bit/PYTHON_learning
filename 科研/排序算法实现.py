"""
这次收集整理并用Python实现了八大经典排序算法，
包括冒泡排序，插入排序，选择排序，希尔排序，归并排序，快速排序，堆排序以及基数排序。
希望能帮助到有需要的同学。之所以用 Python 实现，
主要是因为它更接近伪代码，能用更少的代码实现算法，更利于理解。
本篇博客所有排序实现均默认从小到大。
"""
from time import *

class sort:
    """
    冒泡排序的原理非常简单，它重复地走访过要排序的数列，
    一次比较两个元素，如果他们的顺序错误就把他们交换过来。
    """

    def bubble_sort(self, ary):
        n = len(ary)
        for i in range(n):
            flag = True
            for j in range(1, n - i):
                if ary[j - 1] > ary[j]:
                    temp = ary[j - 1]
                    ary[j - 1] = ary[j]
                    ary[j] = temp
                    flag = False
            if flag:
                break

        return ary

    """
    选择排序是另一个很容易理解和实现的简单排序算法。
    学习它之前首先要知道它的两个很鲜明的特点。
    1. 运行时间和输入无关
    2. 数据移动是最少的
    """

    def select_sort(self, ary):

        n = len(ary)
        for i in range(0, n):
            min = i  # 最小元素下表标记
            for j in range(i + 1, n):
                if ary[j] < ary[min]:
                    min = j  # 找到最小值下标
            ary[min], ary[i] = ary[i], ary[min]  # 交换两者


if __name__ == '__main__':
    l = [123, 42, 543, 345, 12, 321, 12]
    begin_time = time()

    # sort().bubble_sort(l)
    sort().select_sort(l)

    end_time = time()
    runtime = end_time - begin_time
    print(runtime)
    print(l)


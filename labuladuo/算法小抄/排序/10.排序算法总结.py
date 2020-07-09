"""

"""


class Sort:
    # 1.冒泡排序
    def bubbleSort(self, arry: list) -> list:
        n = len(arry)
        for i in range(n):
            for j in range(1, n - i):
                if arry[j - 1] > arry[j]:
                    arry[j - 1], arry[j] = arry[j], arry[j - 1]
        return arry

    def bubble_sort2(self, ary):
        n = len(ary)
        for i in range(n):
            flag = True  # 标记
            for j in range(1, n - i):
                if ary[j] < ary[j - 1]:
                    ary[j], ary[j - 1] = ary[j - 1], ary[j]
                    flag = False
            # 某一趟遍历如果没有数据交换，则说明已经排好序了，因此不用再进行迭代了
            if flag:
                break
        return ary

    # 2.选择排序SelectionSort


if __name__ == '__main__':
    l = [12, 434, 656, 87, 989, 56]
    res = Sort().bubbleSort(l)
    print(res)

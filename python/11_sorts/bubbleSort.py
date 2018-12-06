# 1.实现冒泡排序算法
#
# Author:Lee

def bubble_sort(data):
    '''冒泡排序算法.
    参数:
        data:待排序数据
    '''
    length = len(data)  # 待排序数据的长度

    if length == 0:  # 如果数据为空，则直接返回
        return

    for i in range(length):
        for j in range(length - i - 1):
            has_done = True  # 排序完成标志位
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                has_done = False  # 有数据交换，表示排序工作还没有完

        if has_done:  # 如果没有数据交换了，则表示排序工作完成，可以提前结束
            return

# 1.实现选择排序算法
#
# Author:Lee

def selection_sort(data):
    '''实现选择排序算法.
    参数:
        data:待排序的数据
    '''
    length = len(data)  # 待排序的数据长度

    if length == 0:  # 如果数据为空，则什么都不做
        return

    for i in range(length):
        min_index = i
        for j in range(i, length):
            if data[j] < data[min_index]:
                min_index = j
        if data[min_index] < data[i]:
            data[min_index], data[i] = data[i], data[min_index]

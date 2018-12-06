# 1.实现插入排序算法
#
# Author:Lee

def insertion_sort(data):
    '''实现插入排序算法.
    参数:
        data:待排序的数据
    '''
    length = len(data)  # 待排序的数据长度

    if length == 0:  # 如果数据为空，则什么都不做
        return

    for i in range(1, length):
        value = data[i]
        j = i - 1
        while j >= 0:
            if data[j] > value:
                data[j + 1] = data[j]
            else:
                break
            j -= 1
        data[j + 1] = value

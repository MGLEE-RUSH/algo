# 1.实现快速排序算法
#
# Author:Lee

def quick_sort(data):
    '''实现快速排序算法.
    参数:
        data:待排序的数据
    '''
    length = len(data)

    if length == 0:  # 如果数据为空，则什么都不做
        return

    quick_sort_achieve(data, 0, length - 1)


def quick_sort_achieve(data, start, end):
    '''实现快速排序的具体实现：分、排.
    参数:
        data:待排序的数据
        start:开始的下标
        end:结束的下标
    '''
    if start >= end:
        return

    index = partition(data, start, end)
    quick_sort_achieve(data, start, index - 1)
    quick_sort_achieve(data, index + 1, end)


def partition(data, start, end):
    '''实现快速排序中的分区操作.
    参数:
        data:待分区的数据
        start:待分区的开始下标
        end:待分区的结束下标
    返回:
        index:pivot在完成分区操作后的下标
    '''
    value = data[end]  # 默认取结束下标的数据为pivot值
    index = start

    for j in range(start, end):
        if data[j] < value:
            data[index], data[j] = data[j], data[index]
            index += 1

    data[index], data[end] = data[end], data[index]

    return index

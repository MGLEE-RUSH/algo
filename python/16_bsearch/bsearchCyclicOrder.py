# 1.在一个循环有序数组中查找指定数值
#
# Author:Lee

def bsearch_cyclic_order(data, value):
    '''在一个循环有序数组中查找指定数值.
    参数:
        data:循环有序数组
        value:指定查找的数值
    返回:
        index:指定查找的数值在循环有序数组中的下标，若没有找到，则返回-1
    '''
    length = len(data)  # 确定数组长度

    if length == 0:  # 如果数组没有数据，则直接返回-1
        return -1

    low = 0
    high = length - 1

    return bsearch_cyclic_order_achieve(data, low, high, value)


def bsearch_cyclic_order_achieve(data, low, high, value):
    '''在一个循环有序数组中查找指定数值的实现.
    参数：
        data:循环有序数组
        low:查找范围的起始下标
        high:查找范围的终止下标
        value:指定查找的数值
    返回:
        index:指定查找的数值在数组中的下标，若没有，则返回-1
    '''
    mid = low + (high - low) // 2

    if data[mid] == value:
        return mid
    else:
        if data[low] <= data[mid]:  # 如果中间点的左边是个标准的从小到大排序的数组
            if data[low] <= value < data[mid]:  # 指定数值在该有序区间
                return bsearch(data, low, mid - 1, value)
            else:
                return bsearch_cyclic_order_achieve(data, mid + 1, high, value)
        else:  # 如果中间点的右边是个标准的从小到大的数组
            if data[mid] < value <= data[high]:
                return bsearch(data, mid + 1, high, value)
            else:
                return bsearch_cyclic_order_achieve(data, low, mid - 1, value)


def bsearch(data, low, high, value):
    '''在有序的数组中，使用二分查找算法查找指定数值
    参数:
        data:已排序的数组
        low:查找范围的起始下标
        high:查找范围的终止下标
        value:指定查找的数值
    返回:
        index:指定查找的数值在数组中的下标，若没有找到，则返回-1
    '''
    while low <= high:
        mid = low + (high - low) // 2
        if data[mid] > value:
            high = mid - 1
        elif data[mid] < value:
            low = mid + 1
        else:
            return mid

# 1.实现二分查找第一个值等于给定值的元素；
# 2.实现二分查找最后一个值等于给定值的元素；
# 3.实现二分查找第一个大于等于给定值的元素；
# 4.实现二分查找最后一个小于等于给定值的元素；
#
# Author:Lee

def bsearch_fist_value(data, value):
    '''使用二分查找第一个值等于给定值的元素.
    参数:
        data:已经完成排序（从小到大）的数组
        value:需要查找的给定值
    返回:
        index:第一个等于给定值的数据在数组中的下标，如果没有找到，则返回-1
    '''
    length = len(data)  # 获取数组的大小

    if length == 0:  # 如果数组没有数据，则返回-1
        return -1

    low = 0
    high = length - 1

    while low <= high:
        mid = low + (high - low) // 2
        if data[mid] < value:
            low = mid + 1
        elif data[mid] > value:
            high = mid - 1
        else:
            if mid == 0 or data[mid - 1] != value:
                return mid
            else:
                high = mid - 1

    return -1


def bsearch_last_value(data, value):
    '''使用二分查找最后一个值等于给定值的元素.
    参数:
        data:已经完成排序（从小到大）的数组
        value:需要查找的给定值
    返回:
        index:最后一个等于给定值的数据在数组中的下标，如果没有找到，则返回-1
    '''
    length = len(data)  # 获取数组的大小

    if length == 0:  # 如果数组没有数据，则返回-1
        return -1

    low = 0
    high = length - 1

    while low <= high:
        mid = low + (high - low) // 2
        if data[mid] < value:
            low = mid + 1
        elif data[mid] > value:
            high = mid - 1
        else:
            if mid == length - 1 or data[mid + 1] != value:
                return mid
            else:
                low = mid + 1

    return -1


def bsearch_first_big(data, value):
    '''使用二分查找第一个大于等于给定值的元素.
    参数:
        data:已经完成排序（从小到大）的数组
        value:需要查找的给定值
    返回:
        index:第一个大于等于给定值的数据在数组中的下标，如果没有找到，则返回-1
    '''
    length = len(data)  # 获取数组的大小

    if length == 0:  # 如果数组没有数据，则返回-1
        return -1

    low = 0
    high = length - 1

    while low <= high:
        mid = low + (high - low) // 2
        if data[mid] < value:
            low = mid + 1
        else:
            if mid == 0 or data[mid - 1] < value:
                return mid
            else:
                high = mid - 1

    return -1


def bsearch_last_small(data, value):
    '''使用二分查找最后一个小于等于给定值的元素.
    参数:
        data:已经完成排序（从小到大）的数组
        value:需要查找的给定值
    返回:
        index:最后一个小于等于给定值的数据在数组中的下标，如果没有找到，则返回-1
    '''
    length = len(data)  # 获取数组的大小

    if length == 0:  # 如果数组没有数据，则返回-1
        return -1

    low = 0
    high = length - 1

    while low <= high:
        mid = low + (high - low) // 2
        if data[mid] > value:
            high = mid - 1
        else:
            if mid == length - 1 or data[mid + 1] > value:
                return mid
            else:
                low = mid + 1

    return -1

# 1.实现归并排序算法
#
# Author:Lee

def merge_sort(data):
    '''实现归并排序算法.
    参数:
        data:待排序的数据
    '''
    length = len(data)

    if length == 0:
        return

    merge_sort_achieve(data, 0, length - 1)


def merge_sort_achieve(data, start, end):
    '''归并排序算法的具体实现：分、合
    参数:
        data:待排序的数据
        start:开始的下标
        end:结束的下标
    '''
    if start >= end:
        return

    mid = (start + end) // 2
    merge_sort_achieve(data, start, mid)
    merge_sort_achieve(data, mid + 1, end)
    merge(data, start, end, start, mid, mid + 1, end)


def merge(data, start, end, lstart, lend, rstart, rend):
    '''实现数据归并.
    参数:
        data:归并后数据存储的数组
        start:归并后数据存储数组的开始下标
        end:归并后数据存储数组的结束下标
        lstart:待归并的左侧数据的开始下标
        lend:待归并的左侧数据的结束下标
        rstart:待归并的右侧数据的开始下标
        rend:待归并的右侧数据的结束下标
    '''
    lindex = lstart  # 左侧数据开始下标
    rindex = rstart  # 右侧数据开始下标
    tmpdata = []  # 临时数据存储数组

    while lindex <= lend and rindex <= rend:
        if data[lindex] < data[rindex]:
            tmpdata.append(data[lindex])
            lindex += 1
        else:
            tmpdata.append(data[rindex])
            rindex += 1

    if lindex > lend:  # 如果是左侧的数据先完全存储入临时存储数组
        for i in range(rindex, rend + 1):  # 将右侧剩余数据存储入临时数组
            tmpdata.append(data[i])
    else:  # 将左侧剩余数据存储入临时数组
        for j in range(lindex, lend + 1):
            tmpdata.append(data[j])

    for index in range(end, start - 1, -1):  # 将临时数组数据拷贝到data数组中去
        data[index] = tmpdata.pop()

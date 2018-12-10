# 1.实现计数排序算法
#
# Author:Lee

def counting_sort(data):
    '''实现计数排序算法.
    假设待排序数据都是非零整数.
    参数:
        data:待排序的数据
    '''
    length = len(data)  # 获取待排序数据长度

    if length == 0:  # 如果数据为空，则什么都不做
        return

    # 遍历数据，找到待排序数据的最大值和最小值
    max_value = data[0]
    min_value = data[0]
    for i in range(length):
        if data[i] > max_value:
            max_value = data[i]
        elif data[i] < min_value:
            min_value = data[i]

    # 对待排序数据进行计数统计处理
    count_dic = {}
    for i in range(length):
        index = data[i] - min_value
        if index in count_dic:
            count_dic[index] += 1
        else:
            count_dic[index] = 1

    # 对计数统计数据进行顺序累加
    for i in range(1, max_value - min_value + 1):
        count_dic[i] = count_dic[i - 1] + count_dic[i]

    # 对数据进行计数排序
    tmp_data = [None for i in range(length)]  # 初始化临时数组

    for i in range(length - 1, -1, -1):  # 将数据排序存储进入临时数组
        index = data[i] - min_value
        tmp_data_index = count_dic[index] - 1
        count_dic[index] -= 1
        tmp_data[tmp_data_index] = data[i]

    for i in range(length):  # 将完成排序的数据拷贝进入正式数组中
        data[i] = tmp_data[i]
